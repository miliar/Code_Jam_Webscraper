#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
using namespace std;
#define inf 0x3fffffff
double ans;
double C,F,X;
void dfs(int n,double t){
    double now=t+X/(2+F*(n-1));
    if(now>ans) return ;
    ans=now;
    dfs(n+1,t+C/(2+F*(n-1)));
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,cas=0; scanf("%d",&T);
    while(T--){
        scanf("%lf%lf%lf",&C,&F,&X);
        ans=inf;
        dfs(1,0);
        printf("Case #%d: %lf\n",++cas,ans);
    }
    return 0;
}
