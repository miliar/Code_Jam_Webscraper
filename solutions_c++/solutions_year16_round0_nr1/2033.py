#include<cstdio>
#include<cstring>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

typedef long long LL;

int n;
bool bz[10];

int T;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%I64d",&n);
		if (!n) {printf("INSOMNIA\n"); continue;}
		
		memset(bz,0,sizeof(bz));
		for(LL i=n; ; i+=n)
		{
			LL ii=i;
			for(; ii; ii/=10) bz[ii%10]=1;
			
			bool pd=1;
			fo(j,0,9) if (!bz[j]) {pd=0; break;}
			if (pd) {printf("%I64d\n",i); break;}
		}
	}
}