#include<iostream>
#include<algorithm>
using namespace std;
bool comp(double a,double b)
{
	return a<b;
}
int main()
{
	double naomi[1005],ken[1005],min,temp,naomi1[1005];
	int n,t,j,ans1,ans2,k,minind,i,ind;
	freopen("12.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=1;j<=n;j++)
		{
			scanf("%lf",&naomi[j]);
			naomi1[j]=naomi[j];
		}
		for(j=1;j<=n;j++)
			scanf("%lf",&ken[j]);
		sort(naomi+1,naomi+n+1,comp);
		sort(naomi1+1,naomi1+n+1,comp);
		sort(ken+1,ken+n+1,comp);
		temp=ken[1];
		ans1=0;
		/*
		for(j=1;j<=n;j++)
			printf("%lf ",naomi[j]);
		printf("\n");
		for(j=1;j<=n;j++)
			printf("%lf ",ken[j]);
		printf("\n");
		*/
		for(j=1;j<=n;j++)
		{
			ind=-1;
			for(k=1;k<=n;k++)
			{
				if(naomi1[k]>ken[j])
				{
					ans1++;
					naomi1[k]=-1;
					break;
				}
			}	
		}
		temp=-2.0;
		ans2=0;
		for(j=1;j<=n;j++)
		{
			min=2.0;
			minind=-1;
			ind=-1;
			temp=-2.0;
			for(k=1;k<=n;k++)
			{
			//	printf("%lf %lf %d %d\n",naomi[j],ken[k],j,k);
				if(ken[k]<min&&ken[k]>0)
				{
					min=ken[k];
					minind=k;
				}
				
				if(naomi[j]<ken[k])
				{
					
					if(temp<0)
					{
						temp=ken[k]-naomi[j];
						ind=k;
					}
					else
					{
						if(temp>ken[k]-naomi[j])
						{
							temp=ken[k]-naomi[j];
							ind=k;
						}
					}
				}
			}
		//	printf("%lf %lf %d\n",ken[k],naomi[j],min);
			if(ind>0)
			{
				ken[ind]=-1.0;
			}	
			else
			{
				ans2++;
				ken[minind]=-1.0;
			}
		}
		
		printf("Case #%d: %d %d\n",i,ans1,ans2);
	}
	return 0;
}

