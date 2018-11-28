#include<stdio.h>
int main()
{
//	freopen("A-large.in","r",stdin); 
//	freopen("A-large.txt","w",stdout); 
	int T,i,j,Sm,S[1005],cha,sum=0,max=0;
	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		sum=0;max=0;
		scanf("%d",&Sm);
		getchar();
		for(j=0;j<=Sm;j++)
		{
			S[j]=getchar()-'0';
		}
		for(j=0;j<=Sm;j++)
		{
			max=max>j-sum?max:j-sum;
			sum+=S[j];
		}
		printf("Case #%d: %d\n",i+1,max);
		
	}
}
