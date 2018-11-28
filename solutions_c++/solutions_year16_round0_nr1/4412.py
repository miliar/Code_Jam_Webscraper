#include<cstdio>
#include <cstring>

using namespace std;

long long n,x;
int T,i,nr,ok,u,k,j;
int ap[11];

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);k=0;
   while(T>0)
    {
        --T;++k;
        scanf("%lld",&n);
        if(n == 0) {printf("CASE #%d: INSOMNIA\n",k);continue;}
        memset(ap,0,sizeof(ap));
        ok=0;i=1;nr=0;
        while(ok == 0)
        {
            x=i*n;
            while(x > 0)
            {
                u=x%10;
                if(ap[u] == 0) {++nr;ap[u]=1;}
                x=x/10;
            }
            if(nr == 10) break;
            ++i;
        }
        printf("CASE #%d: %lld\n",k,n*i);
    }
    return 0;
}
