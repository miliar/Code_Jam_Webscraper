#include<cstdio>
long long p;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,tc,n,i;
    long long m,t;
    scanf("%d",&T);
    for(tc=1;tc<=T;++tc){
        scanf("%d",&n);
        printf("Case #%d: ",tc);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        p = 0ll;
        m = 0ll;
        while(p < (1ll << 10) -1){
            m += n;
            t = m;
            while(t){
                i = t%10;
                p |= 1ll << i;
                t /= 10;
            }
        }
        printf("%lld\n",m);
    }
    return 0;
}
