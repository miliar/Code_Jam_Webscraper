#include<cstdio>
int main()
{
	int t,t0;
	scanf("%d",&t);
	for(t0=1;t0<=t;t0++)
	{
		printf("Case #%d: ",t0);
		long double c,f,x,sp=2.0l,ti=0.0l;
		scanf("%Lf%Lf%Lf",&c,&f,&x);
		if(x<=c)printf("%.7Lf\n",x*0.5l);
		else
		{
			while(x/(sp+f)<(x-c)/sp)
			{
				ti+=c/sp;
				sp+=f;
			}
			ti+=x/sp;
			printf("%.7Lf\n",ti);
		}
	}
	return 0;
}
