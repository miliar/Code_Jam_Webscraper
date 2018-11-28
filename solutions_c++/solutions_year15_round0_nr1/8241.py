#include<stdio.h>
int main()
{
	int test_case;
	scanf("%d",&test_case);
	for(int j=1;j<=test_case;j++)	
	{	
		int n;
		char a[10000]={48};
		scanf("%d",&n);
		scanf("%s",a);		
		int addi=0;
		int sumi=0;
		for(int i=0;i<=n;i++)
		{
			sumi+=int(a[i]-48);
		}	
		int sum=0;	
		for(int i=0;i<=n;i++)
		{				
			if(sum<i)
			{
				addi=(i-sum);
				sum+=addi;
			}
			sum+=int(a[i]-48);
		}
		printf("Case #%d: %d\n",j,sum-sumi);
	}
	return 0;
}	
											
