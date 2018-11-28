#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);
	int tc;
	double c,x,f,q,r,s,t,p;
	scanf("%d",&tc);
	for(int b=1;b<=tc;b++)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		q=0.0;
		t=x/2;
		r=c/2;
		s=x/(2+f);
		p=2+f;
		while((r+s)<t)
		{
			q=q+r;
			t=s;
			r=c/p;
			p+=f;
			s=x/p;
		}
		q+=t;
		printf("Case #%d: %.7lf\n",b,q);
	}
	return 0;
}
