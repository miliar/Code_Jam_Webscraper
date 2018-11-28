#include<iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,T;
	cin>>T;
	for (int ca=1;ca<=T;ca++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double cur=2;
		double ans=0;
		while (true)
		{
			if ((x/cur)<=(c/cur+x/(cur+f)))
			{
				ans+=x/cur;
				break;
			}
			ans+=c/cur;
			cur+=f;
		}
		printf("Case #%d: %.7lf\n",ca,ans);
	}
	return 0;
}