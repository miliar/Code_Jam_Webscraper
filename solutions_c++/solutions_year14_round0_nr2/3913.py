#include<stdio.h>
int main()
{
	freopen("C:\\Users\\manish\\Desktop\\input.txt","r",stdin);
 	freopen("C:\\Users\\manish\\Desktop\\output.txt","w",stdout);
	int t,j,i;
	double c,f,x,sc,min,sx;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		//double arr[10000];
		scanf("%lf%lf%lf",&c,&f,&x);
		sx=x/(2.0);
		sc=c/(2.0);
		if(sc>=sx)	{printf("Case #%d: %.7lf\n",i+1,sx);continue;}
		j=1;
		while(1)
		{
			sc=(c/(2.0+(j-1)*f))+(x/(2.0+j*f));
			sc+=sx-(x/(2.0+(j-1)*f));
			if(sc>sx)
				{printf("Case #%d: %.7lf\n",i+1,sx);break;}
			sx=sc;
			j++;
		}
		//printf("Case #%d: %.7lf\n",i+1,min);
	}
	return 0;
}
