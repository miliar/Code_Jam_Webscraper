#include<stdio.h>

int main()
{
	freopen("C:\\Users\\Fred\\Downloads\\D-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Fred\\Downloads\\D-small-attempt0.out","w",stdout);
	int t,n;
	double *weight1,*weight2;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int winl=0;
		int wint=0;
		scanf("%d",&n);
		weight1=new double[n];
		weight2=new double[n];
		for(int j=0;j<n;j++)
		{
			scanf("%lf",&weight1[j]);
		}
		for(int j=0;j<n;j++)
		{
			scanf("%lf",&weight2[j]);
		}
		for(int j=0;j<n;j++)
			for(int k=j+1;k<n;k++)
				if(weight1[j]>weight1[k])
				{
					weight1[k]=weight1[j]+weight1[k];
					weight1[j]=weight1[k]-weight1[j];
					weight1[k]=weight1[k]-weight1[j];
				}
		for(int j=0;j<n;j++)
			for(int k=j+1;k<n;k++)
				if(weight2[j]>weight2[k])
				{
					weight2[k]=weight2[j]+weight2[k];
					weight2[j]=weight2[k]-weight2[j];
					weight2[k]=weight2[k]-weight2[j];
				}
		int poi1=0,poi2=0;
		for(int j=0;j<n;j++)
		{
			if(weight1[poi1]<weight2[poi2])
				poi1++;
			else
			{
				winl++;
				poi1++;
				poi2++;
			}
		}
		poi1=n-1;
		poi2=n-1;
		for(int j=0;j<n;j++)
		{
			if(weight1[poi1]>weight2[poi2])
			{
					wint++;
					poi1--;
			}
			else
			{
				poi1--;
				poi2--;
			}
		}
		printf("Case #%d: %d %d\n",i+1,winl,wint);
	}
	return 0;
}