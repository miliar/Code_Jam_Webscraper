#include<cstdio>
#include<algorithm>

using namespace std;
int main()
{
	int t,l=1,n;
	
	scanf("%d",&t);
	while(l<=t)
	{
		double arr1[1009],arr2[1009];
		int hash[1009]={0};
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",arr1+i);
		for(int i=0;i<n;i++)
			scanf("%lf",arr2+i);
			
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		
		int count=0;
		
		for(int i=0;i<n;i++)
		{
			int j;
			for(j=0;j<n;j++)
			{
				if(arr1[i] > arr2[j])
				{
					if(hash[j]==0)
					{
						count++;
						hash[j]=1;
						break;
					}
				}
				else
				{
					for(int k=n-1;k>=0;k--)
						if(hash[k]==0)
						{
							hash[k]=1;
							break;
						}
							
					break;
				}
				
			}
			
		}
		int hash2[1009]={0};
		int count2=0;
		for(int i=0;i<n;i++)
		{
			int j;
			for(j=0;j<n;j++)
			{
				if(arr2[j]>arr1[i] && hash2[j]==0)
				{
					hash2[j]=1;
					count2++;
					break;
				}
			}
			
		}
		printf("Case #%d: %d %d\n",l,count,n-count2);
		
		l++;
	}
	return 0;
}
