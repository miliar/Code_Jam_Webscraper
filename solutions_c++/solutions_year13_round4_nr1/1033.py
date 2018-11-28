#include <iostream>
#include <cstdio>
#include <cmath>
#include <deque>
#include <map>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <memory.h>
#include <list>
#include <complex>
#include <sstream>

using namespace std;

struct Point{
    bool start;
    int coord;
    int quantity;
}temp;

struct ticket{
    int from;
    int quantity;
    bool operator <(const ticket &t) const{
        return this->from > t.from;
    }
}tick;

multiset<ticket> priority;

bool comparator(const Point &a, const Point &b){
    if(a.coord != b.coord){
        return a.coord < b.coord;
    }
    else
        return a.start > b.start;
}

long long calcPayment(long long N, long long k){
    long long result1 = N * (N + 1) / 2;
    long long result2 = (N - k) * (N - k + 1) / 2;
    return result1 - result2;
}

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
    int TestNumbers;
    scanf("%d",&TestNumbers);

    for(int test = 0; test < TestNumbers; test++)
    {
        vector<Point> points;
        printf("Case #%d: ", test + 1);

        long long N;
        int M;
        scanf("%lld%d",&N,&M);
        long long result = 0;
        for(int i = 0; i < M; i++){
            int o,e;
            long long q;
            scanf("%d%d%lld",&o,&e,&q);
            temp.start = true;
            temp.coord = o;
            temp.quantity = q;
            points.push_back(temp);
            temp.start = false;
            temp.coord = e;
            result += calcPayment(N, e - o) * q;
            points.push_back(temp);
            if(e < o)
                return 0;
        }
        sort(points.begin(), points.end(), comparator);

        long long shouldPay = 0;
        int balance = 0;
        for(int i = 0; i < points.size(); i++){
            int currentCoord = points[i].coord;

            while((points[i].coord == currentCoord) && (points[i].start))
            {
                tick.from = points[i].coord;
                tick.quantity = points[i].quantity;
                priority.insert(tick);
                balance += tick.quantity;
                //printf("Enter at %d: %lld\n", currentCoord, points[i].quantity);
               // printf("Balance %d\n", priority.size());
                i++;
            }
            long long out = 0;
            while(points[i].coord == currentCoord && (!points[i].start)){
                out += points[i].quantity;
                i++;
            }
            balance -= out;
            //printf("Exit at %d: %lld\n", currentCoord, out);
            //printf("Balance %d\n", balance);
            while(out){
                tick = (*priority.begin());
                priority.erase(priority.begin());
                //printf("Erase from queue %d\n",tick.quantity);
                if(tick.quantity <= out)
                {
                    out -= tick.quantity;
                    shouldPay += calcPayment(N, currentCoord - tick.from) * tick.quantity;
                }
                else{
                    tick.quantity -= out;
                    priority.insert(tick);
                    //printf("Back to queue %d\n",tick.quantity);
                    shouldPay += calcPayment(N, currentCoord - tick.from) * out;
                    out = 0;
                }
            }
            //printf("Balance %d\n", priority.size());
            i--;
        }
        printf("%lld", result - shouldPay);

        printf("\n");
    }
    return 0;
}

