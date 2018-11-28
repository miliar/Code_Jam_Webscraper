#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
#include<map>
#include<queue>
#include<bitset>
#include<string>
#include<stdlib.h>
#include<sstream>
#define pb push_back
using namespace std;
int cs,tt,used[1<<22],n;
double dp[1<<22];
char s[222];
double go(int x){
    int i,j;
    if(x==(1<<n)-1)return 0;
    if(used[x]==tt)return dp[x];
    double res=0;
    for(i=0;i<n;i++){
        int cnt=0;
        j=i;
        while((x>>j)&1){
            cnt++;
            j++;
            if(j==n)j=0;
        }
        int y=x|(1<<j);
        res+=go(y)+n-cnt;
    }
    res/=n;
    used[x]=tt;
    dp[x]=res;
    return dp[x];
}
int main(){
    int T,i,j,k;
    scanf("%d",&T);
    while(T--){
        tt++;
        scanf("%s",s);
        n=strlen(s);
        int now=0;
        for(i=0;i<n;i++){
            if(s[i]=='X')now|=1<<i;
        }
        printf("Case #%d: %.15lf\n",++cs,go(now));
    }
    return 0;
}

