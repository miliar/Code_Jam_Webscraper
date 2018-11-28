#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cmath>
#define LL long long
#define maxn 1<<16
#define INF 0x3f3f3f3f
using namespace std;
LL n,m,len,beg,dp[maxn];
char str[1500];
LL flip(int x,LL y){
    LL res=0;
    LL tmp=y;
    int rec[15];
    for(int i=0;i<=x;++i){
        if(y&(1<<i)){
            rec[x-i]=0;
        }else{
            rec[x-i]=1;
        }
    }
    for(int i=0;i<=x;++i){
        if(rec[x-i]==1) res+=(1<<i);
    }
    for(int i=x+1;i<len;++i){
        if(y&(1<<i)) res+=(1<<i);
    }
    return res;
}
int main()
{
    freopen("sdata.in","r",stdin);
    freopen("data.out","w",stdout);
    int id=0;
    int t;
    scanf("%d",&t);
    while(t--){
        memset(dp,INF,sizeof(dp));
        len=0;
        //cout<<'i'<<endl;
        scanf("%s",str);
        len=strlen(str);
        //cout<<len<<endl;
        beg=0;
        for(int i=0;i<len;++i)
            if(str[i]=='+') beg+=(1<<i);
        //cout<<beg<<endl;
        dp[beg]=0;
        //cout<<len<<endl;
        for(int i=0;i<(1<<len);++i){
            bool hav=0;
            for(int j=0;j<len;++j){
                if(!(i&(1<<j))) hav=1;
                //cout<<hav<<endl;
                if(!hav) continue;
                int p=flip(j,i);
                //cout<<j<<' '<<p<<endl;
                dp[p]=min(dp[p],dp[i]+1);
            }
        }
        int all=(1<<len)-1;
        printf("case #%d: %d\n",++id,dp[all]);
    }
    return 0;
}
