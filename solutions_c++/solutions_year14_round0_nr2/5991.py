#include<cstdio>
using namespace std;
typedef long double ld;
int main()
{
	int T;
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for (int tt=1;tt<=T;++tt)
	{
	  printf("Case #%d: ",tt);
	  ld c,f,x,p=2.0,t=0.0;
	  scanf("%Lf%Lf%Lf",&c,&f,&x);
	  while (x>c&&x/p>x/(p+f)+c/p)
	  {
	  	t+=c/p;
	  	p+=f;
	  }
	  t+=x/p;
	  printf("%.7Lf\n",t);
	}
}
