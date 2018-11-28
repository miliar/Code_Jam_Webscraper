#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<iostream>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#define ULL unsigned long long
#define LL long long
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("check.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        LL n;
        scanf("%lld",&n);
        printf("Case #%d: ",cas++);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        int seen=0,j;
        for(j=1;;j++){
            LL t=1LL*j*n;
            while(t){
                seen|=1<<(t%10);
                t/=10;
            }
            if(seen==(1<<10)-1) break;
        }
        printf("%lld\n",1LL*n*j);
    }
    return 0;
}
