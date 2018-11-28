#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *fp;
	fp=fopen("op.txt","w");
	long long int t,n,i,j,temp;
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		long long int A[10]={0};
		scanf("%lld",&n);
		if(n==0)
		{
			fprintf(fp,"Case #%lld: INSOMNIA\n",i);
			continue;
		}
		long long int k=1;
		while(1)
		{
			temp=n*k;
			int p=1;
			while(temp>0)
			{
				A[temp%10]=1;
				temp/=10;
			}
			for(j=0;j<10;j++)
			{
				if(A[j]==0)
				{
					p=0;
					break;
				}
			}
		//	for(j=0;j<10;j++)
		//	printf("%lld ",A[j]);
		//	printf("\n");
			if(p==1)
			break;
			k++;
		}
		fprintf(fp,"Case #%lld: %lld\n",i,n*k);
	}
	return 0;
}
