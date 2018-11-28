#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int _cn,_cc;
        long long n,N,p,m,pp,k;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%lld %lld",&n,&p);
                if (p==1)
                {
                  printf("Case #%d: 0 0\n",_cc);
                  continue;
                }
                N=1;
                N<<=n;
                if (p==N)
                {
                  printf("Case #%d: %lld %lld\n",_cc,N-1,N-1);
                  continue;
                }
                m=N>>1;
                pp=p;
                k=0;
                while (pp>0)
                {
                  pp-=m;
                  m>>=1;
                  ++k;
                }
		printf("Case #%d: %lld",_cc,(1ll<<k)-2);
                m=N>>1;
                pp=N-p;
                k=0;
                while (pp>0)
                {
                  pp-=m;
                  m>>=1;
                  ++k;
                }
                printf(" %lld\n",N-(1ll<<k));
	}
	return 0;
}
