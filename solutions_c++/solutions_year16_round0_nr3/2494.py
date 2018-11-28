#include <bits/stdc++.h>
#ifdef DEBUG
#define D(x...) fprintf(stderr,x) 
#else
#define D(x...)
#endif
using namespace std;
int T, N, J, j;
long long P[11][34];
vector<int> V;
bool digit[34];
bool check(int x)
{
	digit[0]=true;
	digit[N-1]=true;
	for(int n=0; n<N-1; n++)
	{
		if(x& (1<<n))
		{
			digit[n+1]=true;
		}
	}
	for(int b=2; b<=10; b++)
	{
		long long X=0;
		for(int i=0; i<N; i++)
		{
			if(digit[i])
			{
				X+= P[b][i];
			}
		}
		bool found=false;
		for(int i=2; i<=sqrt(X); i++)
		{
			if(X%i==0)
			{
				found=true;
				V.push_back(i);
				break;
			}
		}
		if(!found)
		{
			return 0;
		}
	}
	return 1;
}
int main ()
{
	freopen("infile.txt", "r", stdin);
	freopen("outfile.txt", "w", stdout);
	printf("Case #1:\n");
	scanf("%d", &T);
	scanf("%d %d", &N, &J);
	for(int n=2; n<=10; n++)
	{
		P[n][0]=1;
		for(int i=1; i<33; i++)
		{
			P[n][i] = P[n][i-1]*n;
		}
	}
	for(int x=0; x<1<<N-1; x++)
	{
		for(int i=0; i<34; i++)
		{
			digit[i]=false;
		}
		V.clear();
		if(check(x))
		{
			D("%d\n", x);
			for(int i=N-1; i>=0; i--) 
			{
				printf("%d", digit[i]);
			}
			for(auto v: V)
			{
				printf(" %d", v);
			}
			printf("\n");
			j++;
		}
		if(j==J)
		{
			return 0;
		}
	}
}