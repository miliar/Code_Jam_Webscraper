#include<bits/stdc++.h>
using namespace std;
void work(int a);
int book[10]={0},Count=0;
int main()
{
	int n,N,i,j;
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		memset(book,0,sizeof(book));
		Count=0;
		scanf("%d",&N);
		printf("Case #%d: ",i);
		if(N==2*N)
		{
			printf("INSOMNIA\n");
			continue;
		}
		for(j=1;;j++)
		{
			work(j*N);
			if(Count==10)
			{
				printf("%d\n",j*N);
				break;
			}
		}
	}
}

void work(int a)
{
	int t;
	while(a>0)
	{
		t=a%10;
		if(!book[t])
		{
			book[t]=1;
			Count++;
		}
		a/=10;
	}
}
