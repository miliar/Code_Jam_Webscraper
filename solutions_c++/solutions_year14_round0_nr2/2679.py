#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	scanf("%d",&tc);
	int co=1;
	while(tc--)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double start=2.0000000;
		double res=0;
		while(x/start>(c/start+x/(start+f)))
		{
			res+=c/start;
			start=start+f;
		}
		res+=x/start;
//		cout<<res<<endl;
		printf("Case #%d: %.7lf\n",co,res);
		co++;
	}
	return 0;
}
