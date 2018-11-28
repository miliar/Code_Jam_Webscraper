#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int t,n;
	float tmp;
	//bool hash[1000];
	double a1[1000],a2[1000];
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{	
			scanf("%f",&tmp);
			a1[i]=tmp;
		}
		for(int i=0;i<n;i++)
		{	
			scanf("%f",&tmp);
			a2[i]=tmp;
		}
		int y=0,z=0;
		sort(a1,a1+n);
		sort(a2,a2+n);
	/*	for(int i=0;i<n;i++)
			hash[i]=true;*/
		int l=n;
		for(int i=n-1;i>=0 && l>0;i--)
		{
			for(int j=l-1;j>=0;j--)
			{
				if(a1[i]>a2[j])
				{
					y++;
					l=j;
					break;
				}
			}
		}
		l=n;
		for(int i=n-1;i>=0 && l>0;i--)
		{
			for(int j=l-1;j>=0;j--)
			{
				if(a2[i]>a1[j])
				{
					z++;
					l=j;
					break;
				}
			}
		}
		z=n-z;
		printf("Case #%d: %d %d\n",k,y,z);
	}
	return 0;
}