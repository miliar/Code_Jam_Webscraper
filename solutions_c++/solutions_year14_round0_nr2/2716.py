#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
using namespace std;
const double eps=1e-8;
int TT,tot,u; double C,F,X,V,T,ans;
int main()
{	//freopen("B.in","r",stdin);
	//freopen("B_big.out","w",stdout);
	for (scanf("%d",&TT);TT;TT--)
	{	printf("Case #%d: ",++tot);
		scanf("%lf%lf%lf",&C,&F,&X); V=2.0; ans=X/V;
		T=0.0;
		for (;;)
		{	T+=C/V; V+=F;
			if (ans>T+(X/V)+eps) ans=T+(X/V)+eps;
				else break;
			}
		printf("%.7lf\n",ans);
		}
	return 0;
}
