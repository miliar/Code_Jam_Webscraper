#include <cstdio>

long double t,c,f,x,tx;

int main()
{
	int nt;
	scanf(" %d",&nt);
	for(int i=1; i<=nt; i++)
	{
		tx = 2.;
		t = 0.;
		printf("Case #%d: ",i);
		scanf(" %Lf %Lf %Lf",&c,&f,&x);
		while(c/tx+x/(tx+f)<x/tx)
		{
			t+=c/tx;
			tx+=f;
		}
		printf("%.7Lf\n",t+x/tx);
	}
	return 0;
}
