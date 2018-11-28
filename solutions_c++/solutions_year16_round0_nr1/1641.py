#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;
typedef long long LL;

LL n,m;
bool v[10];

bool sol(LL x){
    //memset(v,0,sizeof(v));
    for(;x;x/=10) v[x%10] = true;
    bool f = true;
    for(int i = 0;i < 10;i++) f &= v[i];
    return f;
}

int main(){
    int i,j,cas;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&cas);
    for(int T=1;T<=cas;T++){
        scanf("%I64d",&n);
        memset(v,0,sizeof(v));
        printf("Case #%d: ",T);
        if(n){
            for(m=n;;m+=n){
                if(sol(m)) break;
            }
            printf("%I64d\n",m);
        }else puts("INSOMNIA");

    }


    return 0;
}
