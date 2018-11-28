#include<cstdio>
int main()
{
	double x,c,f,time;
	short int t,c_no=0;
	scanf("%hd",&t);
	while(t--)
	{
		c_no++;
		scanf("%lf%lf%lf",&c,&f,&x);
		//printf("%lf %lf %lf\n",c,f,x);
		double r=2.0;
		time=0.0;
		while(((c/r)+(x/(r+f)))<(x/r))
		{
			time+=c/r;
			r+=f;
		}
		time+=x/r;
		printf("Case #%hd: %.7lf\n",c_no,time);
	}
	return 0;
}
