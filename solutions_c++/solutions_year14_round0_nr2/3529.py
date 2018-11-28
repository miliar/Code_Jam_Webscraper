#include<cstdio>
using namespace std;
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("out.out","w",stdout);
	int t,x;double a,b,c,d,o;
	scanf("%d",&t);
	for(int ca=1;ca<=t;++ca)
	{
		printf("Case #%d: ",ca);
		scanf("%lf%lf%lf",&a,&b,&c);
		d=c/a-1-2/b;
		if(d<0)
		{
			printf("%.7lf\n",c/2);
			continue;
		}
		x=(int)d+1;d=2;
		o=0;
		for(int i=0;i<x;++i)
		{o+=a/d;d+=b;}
		o+=c/d;
		printf("%.7lf\n",o);
	}
}
