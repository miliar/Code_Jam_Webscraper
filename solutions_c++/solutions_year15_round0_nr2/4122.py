#include <iostream>     // std::cout
#include <algorithm>    // std::lower_bound, std::upper_bound, std::sort
#include <vector>       // std::vector
#include <cstdio>
#include <cstring>
typedef long long LL;
using namespace std;

int n,m;
char str[1111];
int num[1111];

bool input(){
    scanf("%d",&n);
    for(int i=0; i<n; i++)scanf("%d",&num[i]);
}
int dp[1111][1111];

int dpr(int a, int b){
    int &res=dp[a][b];
    if(a<=b)return res=0;
    res=a;
    for(int i=1; i<a; i++)
        res=min(res, 1+dpr(i,b)+dpr(a-i,b));
    return res;
}

void solve(){
    int res=1000000;
    for(int k=1; k<1000; k++){
        int sum=0;
        for(int i=0; i<n; i++)
            sum+= dpr(num[i],k);
        res=min(res,k+sum);
    }
    static int cas=1;
    printf("Case #%d: %d\n",cas++,res);
}

int main () {
    int zz=1;
    memset(dp,-1,sizeof dp);
    scanf("%d",&zz);
    while(zz--){
        input();
        solve();
    }
    return 0;
}
/*
011
011

011
110

*/
