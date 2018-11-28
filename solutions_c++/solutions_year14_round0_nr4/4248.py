#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main()
{
	freopen("input4_large.in", "r", stdin);
	freopen("output4_large.txt", "w", stdout);
	int t,t1;
	scanf("%d",&t);
	t1=t;
	while(t--)
	{
		int bl;
		int i=0,j=0;
		scanf("%d",&bl);
		double ma[bl],ken[bl],mac1[bl],kenc1[bl],mac2[bl],kenc2[bl];
		for(i=0;i<bl;i++) 
		{
			scanf("%lf",&ma[i]);
			mac1[i]=ma[i];
			mac2[i]=ma[i];
		}
		for(i=0;i<bl;i++) 
		{
			scanf("%lf",&ken[i]);
			kenc1[i]=ken[i];
			kenc2[i]=ken[i];
		}
		sort(ma,ma+bl);
		sort(mac1,mac1+bl);
		sort(mac2,mac2+bl);
		sort(ken,ken+bl);
		sort(kenc1,kenc1+bl);
		sort(kenc2,kenc2+bl);
		int counter1=0,counter2=0;
		for(i=0;i<bl;i++)
		{
			for(j=i;j<bl;j++)
			{
				if(mac1[i]<kenc1[j])
				{
					kenc1[j]=0;
					counter1++;
					break;
				}
			}
		}
		
		for(i=0;i<bl;i++)
		{
			for(j=0;j<bl;j++)
			{
				if((mac2[i]>kenc2[j])&&kenc2[j]!=0)
				{
					counter2++;
					kenc2[j]=0;
					break;
				}
			}
		}
		
		printf("Case #%d: %d %d\n",t1-t,counter2,bl-counter1);
	}
	return 0;
}
