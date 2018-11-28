#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;
int n,m;

int T;
typedef pair<int,char>ic;
int main(){
    freopen("/Users/Masoud/Desktop/A-large.in.txt", "r", stdin);
    freopen("/Users/Masoud/Desktop/out.txt", "w", stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%d",&n);
        priority_queue<ic>pq;
        int sum=0;
        for(int i =0;i<n;i++){
            int cnt;
            scanf("%d",&cnt);
            pq.push({cnt,(i+'A')});
            sum+=cnt;
        }
        printf("Case #%d:",t);
        while (!pq.empty()) {
            ic f1 = pq.top();
            pq.pop();
            int mx = max(pq.top().first,f1.first-1);
            if(mx <= (sum-1)/2){
                printf(" %c",f1.second);
                f1.first--;
                sum--;
                if (f1.first) {
                    pq.push(f1);
                }
            }else{
                ic f2 = pq.top();
                pq.pop();
                printf(" %c%c",f1.second,f2.second);
                f1.first--;
                f2.first--;
                sum-=2;
                if (f1.first) {
                    pq.push(f1);
                }
                if (f2.first) {
                    pq.push(f2);
                }
            }
        }
        printf("\n");
    }
    return 0;
}

