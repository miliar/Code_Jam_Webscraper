#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second

 
#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};	
//////////////////////

const int N = 1010;

int n;

void main2( int test )
{
	scanf("%d",&n);
	ll qtd = 0;
	ll ans = 0;
	for(int i=0;i<=n;++i)
	{
		int x; scanf("%1d",&x);
		if(qtd<=i)
		{
			ans+=(i-qtd);
			qtd+=(i-qtd);
		}
		qtd+=x;
	}
	printf("Case #%d: %lld\n",test,ans);
}

int main()
{
	//ios::sync_with_stdio(0);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i) main2(i);
	return 0;
}