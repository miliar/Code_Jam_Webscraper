#include <cstdio>
#include <cstring>
using namespace std;
long long m,k;
int v[15],n;

int ok()
{
    for (int i=0;i<=9;i++)
        if (!v[i])
            return 0;
    return 1;
}

int main()
{
    int t,i,j;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    scanf("%d",&t);
    for (i=1;i<=t;i++) {
        memset(v,0,sizeof(v));
        scanf("%d",&n);
        for (j=1;j<=50000;j++) {
            m=1LL*j*n;
            k=m;
            while (k) {
                v[k%10]=1;
                k/=10;
            }
            if (ok()) {
                printf("Case #%d: %lld\n",i,m);
                break;
            }
        }
        if (j>50000)
            printf("Case #%d: INSOMNIA\n",i);
    }
    return 0;
}
