#include <stdio.h>

int T;

void solve(int c)
{
	int N, i;
	char cc;
	long long sum=0, curr=0, need=0;
	scanf("%d ", &N);

	for(i=0; i<=N; i++)
	{
		scanf("%c", &cc);
		curr=cc-'0';
		if(sum<i && curr!=0)
		{
			need+=(i-sum);
			sum+=(i-sum);
		}
		sum+=curr;
	}

	printf("Case #%d: %lld\n", c, need);
}

int main()
{
	int i;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d", &T);
	for(i=1; i<=T; i++)
		solve(i);

	return 0;
}