#include <bits/stdc++.h>
using namespace std;

const int N = 1000*1000+5;

int MAX[N], MIN[N];
int war[N];
int sum[N];

#define make(a,b) make_pair(a,b);
#define x first
#define y second

int test()
{
	int n,k;
	scanf("%d%d",&n,&k);
	for (int i=k-1;i<n;i++)
		scanf("%d",sum+i);
	if ( sum[k-1] < 0 ) for (int i=0;i<n;i++) sum[i] *= -1;
	for (int i=0;i<k;i++) MAX[i] = MIN[i] = 0;
	for (int i=0;i<k;i++)
		war[i] = 0;
	for (int i=k;i<n;i++)
	{
		war[i] = war[i-k] + sum[i] - sum[i-1];		
		MAX[ (i-k)%k ] = max( MAX[ (i-k)%k ], war[i] ); 
		MIN[ (i-k)%k ] = min( MIN[ (i-k)%k ], war[i] ); 
	}
	int linia = 0;
	for (int i=0;i<k;i++)
		linia = max( linia, MAX[i] );
	int mini = linia;
	for (int i=0;i<k;i++)
		mini = min( mini, MIN[i] );
	long long suma = sum[k-1];
	for (int i=0;i<k;i++)
	{
		int w = MIN[i] - mini;
		suma += w;
		MIN[i] -= w;
		MAX[i] -= w;
	}	
	linia = mini;
	for (int i=0;i<k;i++)
		linia = max( linia, MAX[i] );
	suma %= k;
	for (int i=0;i<k;i++)
		suma -= linia - MAX[i];	
	return linia - mini + (int)( suma > 0 );
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
		printf("Case #%d: %d\n",i,test());
}
