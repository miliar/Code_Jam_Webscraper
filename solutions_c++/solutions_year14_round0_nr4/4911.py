#include<stdio.h>

int partion(float a[],int p,int r){
	float x=a[r],t;
	int i=p-1,j;
	for(j=p;j<=r-1;j++){
		if(a[j]<=x){
			i++;
			t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
	}
	t=a[i+1];
			a[i+1]=a[r];
			a[r]=t;
			return (i+1);
}
void quick(float a[],int p,int r){
	int q;
	if(p < r){
		q=partion(a,p,r);
		quick(a,p,q-1);
		quick(a,q+1,r);
	}
}

int main()
{   freopen("a4.txt","w",stdout);
	int t,k,n,i,j,count,count1;
	float a[1001],b[1001],c[1001];
	scanf("%d",&t);
	k=t;
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%f",&a[i]);
		}
		for(i=0;i<n;i++)
		{
			scanf("%f",&b[i]);
		}
		quick(a,0,n-1);
		quick(b,0,n-1);
		for(i=0;i<n;i++)
		{
			c[i]=b[i];
		}
		 count=0,count1=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i]>b[j] && b[j]!=2)
				{
					count++;
					b[j]=2;
					break;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i]<c[j] && c[j]!=2)
				{
					count1++;
					c[j]=2;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n",k-t,count,n-count1);
	}
	return 0;
}
