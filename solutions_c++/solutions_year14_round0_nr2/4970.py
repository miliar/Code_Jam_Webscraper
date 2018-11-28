#include <iostream>
using namespace std;
int main()
{	int u,o;
	double c,f,x,p,t1,t2,t;
	scanf("%d",&u);
	for(o=1;o<=u;o++)
	{	scanf("%lf%lf%lf",&c,&f,&x);
		p=2.0;
		t1=0.1;
		t2=0.0;
		t=0.0;
		while(t2<t1)
		{	t1=x/p;
			t2=(c/p)+(x/(p+f));
			if(t2<t1)
		{
			t=t+(c/p);
			p=p+f;
		}
		}
	
	t+=(x/p);
	printf("Case #%d: %0.7lf\n",o,t);
	}
	return 0;
}