#include<stdio.h>
#include<algorithm>
#include<string.h>
int A[10001];
bool V[10001];
int N,M;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int t,i,j;
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&N,&M);
		for(i=1;i<=N;i++) scanf("%d",&A[i]);
		memset(V,0,sizeof(V));
		std::sort(A+1,A+1+N);
		int Ans=0;
		for(i=N;i>=1;i--)
		{
			if(V[i]) continue;
			V[i]=1;
			for(j=i-1;j>=1;j--)
			{
				if(V[j]) continue;
				if(A[i]+A[j]<=M)
				{
					V[j]=1;
					break;
				}
			}
			Ans++;
		}
		printf("Case #%d: %d\n",t,Ans);
	}
}
