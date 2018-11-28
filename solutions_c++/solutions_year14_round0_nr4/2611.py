#include<stdio.h>
#include<algorithm>
using namespace std;
void program(int xxxx)
{
	printf("Case #%d: ",xxxx);
	
	int n;
	scanf("%d",&n);
	
	double a[n],b[n];
	
	for(int i=0;i<n;i++)
	{
		scanf("%lf",&a[i]);
	}
	
	for(int i=0;i<n;i++)
	{
		scanf("%lf",&b[i]);
	}
	sort(a,a+n);
	sort(b,b+n);
	int index=n;
	
	int count=0;
	//deceitful
	for(int i=n-1;i>=0;i--)
	{
		while(index>0)
		{
			index--;
			//printf("%lf %lf\n",a[i],b[index]);
			if(a[i]>b[index]) { count++; break;}
		}
	}
	
	printf("%d ",count);
	
	index=n;
	count=n;
	//normal
	for(int i=n-1;i>=0;i--)
	{
		while(index>0)
		{
			index--;
			//printf("%lf %lf\n",b[i],a[index]);
			if(b[i]>a[index])  { count--; break;}
		}
	}
	
	printf("%d",count);
	
	printf("\n");	
	
}
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
		program(i+1);
	
	return 0;
}
