#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <memory.h>
#include <stack>
#include <iomanip>
#include <sstream>
#include <cmath>
using namespace std;

typedef long long int ll;

int main (int argc, char * const argv[]){
    #ifdef LOCAL
        freopen("B-large.in", "r", stdin);
        freopen("B-large.out", "w", stdout);
    #endif // LOCAL

    int ntest;
    while(cin>>ntest){
        double price, up_rate, goal;
        for(int tt=0; tt<ntest; tt++){
            cin >> price >> up_rate >> goal;
            double rate = 2;
            double ans = goal / rate;
            double cur_spend_time = 0;

            while(cur_spend_time < ans){
                cur_spend_time = cur_spend_time + price / rate;
                rate += up_rate;
                ans = min(ans, cur_spend_time + goal / rate);
            }
            printf("Case #%d: %.7f\n", tt+1, ans);

        }

    }




    return 0;
}
