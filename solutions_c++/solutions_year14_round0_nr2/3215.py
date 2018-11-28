#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
	freopen("out.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int t,c,f,x;
	scanf("%d",&t);	
	for(int T=0;T<t;T++)
	{
		double c,f,x,n,m,tmp,sp;
		scanf("%lf%lf%lf",&c,&f,&x);
		sp=2;
		n=x/2;
		m=x/2;
		tmp=0;
		while(n>=m)
		{
			n=m;
			tmp+=c/sp;
			sp+=f;
			m=tmp+x/sp;
		}
		printf("Case #%d: %.7lf",T+1,n);
		
		printf("\n");
	}
	return 0;
}
