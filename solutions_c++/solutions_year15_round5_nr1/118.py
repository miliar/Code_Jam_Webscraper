#include <bits/stdc++.h>
using namespace std;

const int N = 1000*1000+5;
#define make(a,b) make_pair(a,b)
int S[N], M[N];
int fu[N];
int ile[N];
vector <int> syn[N];
int init(int n)
{
	for (int i=0;i<=n;i++)
	{	
		fu[i] = i;
		ile[i] = 0;
		syn[i].clear();
	}	
}

int fuf(int x)
{
	if ( fu[x] == x ) return x;
	fu[x] = fuf( fu[x] );
	return fu[x];
}

void fuu(int a)
{
	ile[a] ++;
	if ( M[a] != a ) ile[ fuf( M[a] ) ] += ile[a];
	fu[ a ] = fuf( M[a] );
	if ( M[a] != a ) syn[ M[a] ].push_back( a );
}

void usu(int a)
{
	ile[ fuf(a) ] --;
//	printf("nowy %d to %d\n",fuf(a), ile[ fuf(a) ] );
	ile[a] = 0;
	for (int i=0;i<syn[a].size();i++)
		usu( syn[a][i] );
	syn[a].clear();
	fu[a] = a;
}

pair<int,int> tab[N];

int test()
{
	int n,d;
	scanf("%d%d",&n,&d);
	int s0, as, cs, rs, m0, am, cm, rm;
	scanf("%d%d%d%d",&s0,&as,&cs,&rs);
	scanf("%d%d%d%d",&m0,&am,&cm,&rm);
	S[0] = s0;
	M[0] = m0;
	for (int i=1;i<n;i++)
		S[i] = ( S[i-1] * (long long) as + cs ) % rs;
	tab[0] = make( S[0], 0 );
	for (int i=1;i<n;i++)
	{
		M[i] = ( M[i-1] * (long long) am + cm ) % rm;
	}
	M[0] = 0;
	for (int i=1;i<n;i++) M[i] %= i;
//	for (int i=0;i<n;i++) scanf("%d",S+i);
//	for (int i=0;i<n;i++) scanf("%d",M+i);
	for (int i=0;i<n;i++) tab[i] = make( S[i], i );
	sort( tab, tab+n );
	init(n);
	int p = 0;
	int MAX = 0;
	bool OK = 0;
	for(int i=0;i<n;i++)
	{
		fuu( tab[i].second );
//		printf("dodaj %d %d\n",tab[i].second,tab[i].first);
//		printf("ojc %d\n",M[ tab[i].second ] );
		if ( tab[i].second == 0 ) OK = 1;
		while ( tab[i].first - tab[p].first > d )
		{
			if ( tab[p].second == 0 ) OK = 0;
			usu( tab[p].second );
//			printf("usun %d\n",tab[p].second);
			p++;
			}
		MAX = max( MAX, OK*ile[0] );
	}
	return MAX;
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
		printf("Case #%d: %d\n",i,test());
}
