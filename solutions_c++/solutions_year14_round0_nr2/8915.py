#include <stdio.h>
main()
{
	int k,j,i,t;
	scanf("%d",&t);
	double c[100],f[100],x[100],u,v;
	for(k=0;k<t;k++)
	{
		scanf("%lf %lf %lf",&c[k],&f[k],&x[k]);
	}
	for(i=0;i<t;i++)
	{
		j=2;
		u=x[i]/2.0;
		v=c[i]/2.0+x[i]/(2.0+f[i]);

    	while(u>v)
    	{
		//	printf("%lf %lf\n",u,v);
    		u=v;
    		v=v+c[i]/(2.0+f[i]*(j-1))+x[i]/(2.0+f[i]*j)-x[i]/(2.0+f[i]*(j-1));
    		
    		j++;
    	}
    
    	printf("Case #%d: %.7lf \n",i+1,u);
    }

}




















