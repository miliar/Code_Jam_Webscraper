#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include<iostream>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
int bff[1005];
int circle[1005], vst[1005], n;
int rnd(int idx, int mod){
    return (idx+mod)%mod;
}
int dfs(int len, int now){
    int i, j;
    if(now == len){
        for(i=0;i<len;i++){
            if(circle[rnd(i+1, len)] == bff[circle[i]] || circle[rnd(i-1, len)] == bff[circle[i]])
                ;
            else
                return 0;
        }
        return 1;
    }
    for(i=1;i<=n;i++)if(!vst[i]){
        vst[i] = 1;
        circle[now] = i;
        if(dfs(len, now + 1) == 0)
            vst[i] = 0;
        else
            return 1;
    }
    return 0;
}
int main()
{
    int t,i,j,k;

    freopen("gccs.in","r",stdin);
    freopen("gccs.out","w",stdout);
    scanf("%d\n",&t);
    for(int cnt=1;cnt<=t;cnt++)
    {
        scanf("%d\n",&n);
        for(i=1;i<=n;i++)
            scanf("%d",&bff[i]);
        for(i=n;i>=2;i--){
            memset(vst,0,sizeof(vst));
            if(dfs(i, 0))
                break;
        }
        //for(j=0;j<i;j++)printf("%d ",circle[j]);printf("\n");
        printf("Case #%d: %d\n",cnt, i);
    }
    return 0;
}
