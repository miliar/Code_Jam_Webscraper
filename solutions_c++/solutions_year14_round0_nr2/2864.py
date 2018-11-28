#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
#define ll long long int
int main()
	{
	int t, i;
	double c, f, x, total, p, nt, n;
	scanf("%d", &t);
	for(i=1;i<=t;i++)
		{
		scanf("%lf%lf%lf", &c, &f, &x);
		p=0.0;
		total=x/2;
		n=2.0;
		while(true)
			{
			p+=(c/n);
			n+=f;
			nt=p+x/n;
			if(nt>total)
				break;
			total=nt;
			}
		printf("Case #%d: %.7lf\n", i, total);
		}
	return 0;
	}