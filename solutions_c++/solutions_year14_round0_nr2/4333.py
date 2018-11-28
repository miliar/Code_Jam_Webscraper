#include<stdio.h>
int main()
{
	int i,j=0,k,T,v=0,m=0,z;
	double C,F,X,y=2.000,sum1=0.0000,sum2=0.000,a[100000],t1,t2,t3,t4,b,d,w,sum0=0.000,sum3=0.0000;
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%lf",&C);
		//printf("value of C is %f\n",C);
		scanf("%lf",&F);
		//printf("value of F is %f\n",F);
		scanf("%lf",&X);
		//printf("value of X is %f\n",X);
		t1=C/2;
		//printf("value of t1 is %f\n",t1);
		t4=X/2;
		//printf("value of t2 is %f\n",t2);
		if(t1>=t4)
		{
			v=1;
			printf("Case #%d: %.7f\n",i+1,t4);;
		}
		else
		{
			a[0]=t1;
			y=y+F;
			w=X/y;                                                  //w is the time of owning x after 1 form
			//printf("value of y is %f\n",y);
			if(t4<=(t1+w))
			{
				v=1;
				//printf("value of v is %d\n",v);
				printf("Case #%d: %.7f\n",i+1,t4);
			}
			j++;
		}
		while(v!=1)
		{    
		    if(m>0)
		    {
		    	y=y-F;
		    }
		    //printf("value of y is %f\n",y);
			t2=C/y;
			//printf("value of t2 is %f\n",t2);
			a[j]=t2;
			//printf("value of aj is %f\n",a[j]);
			y=y+F;
			b=X/y;
			if(m==0)
			{
				sum0=a[0]+w;
			    sum3=a[0]+a[1]+b;
			    if(sum0<=sum3)
			    {
			    	printf("Case #%d: %.7f\n",i+1,sum0);
				    v=1;
			    }
			}
			//printf("value of y is %f\n",y);
			
			//printf("value of b is %f\n",b);
			j++;
			t3=C/y;
			//printf("value of t3 is %f\n",t3);
			y=y+F;
			//printf("value of y is %f\n",y);
			d=X/y;
			//printf("value of d is %f\n",d);
			a[j]=t3;
			//printf("value of aj is %f\n",a[j]);
			for(k=0;k<(j+1);k++)
			sum1=sum1+a[k];
			//printf("value of sum1 is %f\n",sum1);
			for(k=0;k<j;k++)
			sum2=sum2+a[k];
			//printf("value of sum2 is %f\n",sum2);
			sum1=sum1+d;
			//printf("value of sum1 is %f\n",sum1);
			sum2=sum2+b;
			//printf("value of sum2 is %f\n",sum2);
			if(sum1>sum2&&v!=1)
			{
				if(sum2>t4)
				printf("Case #%d: %.7f\n",i+1,t4);
				else
				printf("Case #%d: %.7f\n",i+1,sum2);
				v=1;
			}
			m++;
			sum1=0.0000;
			sum2=0.0000;
			//printf("/*******************************/\n");
		}
		//printf("value of m is %d\n",m);
		v=0;
		m=0;
		j=0;
		y=2.00000;
	}
	return 0;
}

