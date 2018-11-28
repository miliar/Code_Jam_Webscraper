#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;
double Ken[1001],Naomi[1001];
int main() {
    int T,tc = 0;
#ifndef ONLINE_JUDGE
    freopen("D-large.in", "r" , stdin);
    freopen("output.txt" , "w" , stdout);
#endif // ONLINE_JUDGE
    scanf("%d",&T);
    while(T--) {
        int n;
        scanf("%d",&n);
        for(int i = 1; i <= n; ++i) scanf("%lf",&Naomi[i]);
        for(int i = 1; i <= n; ++i) scanf("%lf",&Ken[i]);
        sort(Ken+1,Ken+n+1);
        sort(Naomi+1,Naomi+n+1);
        int cur = 1,num = 0;
        for(int i = 1; i <= n; ++i)
        {
            while(Ken[cur] < Naomi[i] && cur < n) ++cur;
            if(Ken[cur] > Naomi[i] && cur <= n) ++num,++cur;
        }
        cur = n;int x = 0;
        for(int i = n ; i >= 1; --i){
            while(Naomi[i] < Ken[cur] && cur > 0) --cur;
            if(cur > 0){
                if(Naomi[i] > Ken[cur]) ++x;
                -- cur ;
            }
        }
        printf("Case #%d: %d %d\n",++tc,x,n-num);
    }
    return 0;
}
