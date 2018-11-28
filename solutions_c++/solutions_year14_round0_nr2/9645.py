#include<stdio.h>
int main()
{
	float a[1000];
	float x,c,f,s,sum,t;
	int test,i,j,test1;
	scanf("%d",&test);
	test1=test;
	while(test--)
	{
		t=0;
		sum=0;i=0;
		scanf("%f %f %f",&c,&f,&x);
		s=2.00;
		t=x/s;
		while(sum+c/s+x/(f+s)<t)
		{
			a[i++]=c/s;
			sum=0;
			for(j=0;j<i;j++)
			{
				sum+=a[j];
			}
			t=x/(s+f) +sum;
			s=s+f;
		}
		printf("Case #%d: %0.6f",test1-test,t);
		
	}
	
	return 0;
	
}
