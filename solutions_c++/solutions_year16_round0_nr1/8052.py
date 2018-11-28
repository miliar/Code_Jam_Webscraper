#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<queue>
#include<vector>
using namespace std;
#define LL long long

int dig[15];
void solve(LL s){
    while(s>0){
        int r=(int)s%10;
        s=s/(LL)10;
        dig[r]=1;
    }
}
bool ok(){
    int i;
    for(i=0;i<=9;++i){
        if(dig[i]==0)break;
    }
    if(i==10)return true;
    else return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    LL n;
    LL inf=(1e+7)+5;
    int t;scanf("%d",&t);
    int cas=0;
    while(t--){
        scanf("%lld",&n);
        cas++;
        printf("Case #%d: ",cas);
        memset(dig,0,sizeof(dig));
        LL res=1;
        int fg=0;
        for(LL i=1;i<=inf;++i){
            res=(LL)i*n;
            solve(res);
            if(ok()){
                fg=1;
                printf("%lld\n",res);
                break;
            }
        }
        if(fg==0)printf("INSOMNIA\n");
    }
    return 0;
}
