/// David Mateus Batista <david.batista3010@gmail.com>
/// Computer Science - Federal University of Itajuba - Brazil

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define DINF (double)1e+30
#define EPS (double)1e-9
#define PI (double)acos(-1.0)
#define RAD(x) (double)(x*PI)/180.0
#define PCT(x,y) (double)x*100.0/y
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define F first
#define S second
#define D(x) x&(-x)
#define reset(a,b) memset(a, b, sizeof(a))
#define debug(x,y) cout << x << y << endl
#define gcd(x,y) __gcd(x, y)
#define lcm(x,y) (x*y)/gcd(x,y)
#define bitcount(x) __builtin_popcount(x)
#define llbitcount(x) __builtin_popcountll(x)

enum {North, East, South, West};
//{0, 1, 2, 3}
//{Up, Right, Down, Left}

int mi[] = {-1, 0, 1, 0, -1, 1, 1, -1};
int mj[] = {0, 1, 0, -1, 1, 1, -1, -1};

void bin(int x, int n)
{
	for(int i=n-1; i>=0; i--)
		printf("%d", ((x&(1<<i))!=0));
}

ll val(int x, int b, int n)
{
	ll ret=0;
	for(int i=n-1; i>=0; i--)
		ret=(ret*b)+((x&(1<<i))!=0);
	return ret;
}

ll valid(ll x)
{
	ll sq=sqrt(x);
	for(ll i=3; i<=sq; i+=2)
		if(x%i==0)
			return i;
	return 0;
}


void solve(int n, int m)
{
	for(int i=(1<<n)-1; m>0; i--)
	{
		if(!(i&(1<<0)) || !(i&(1<<(n-1))))
			continue;
		bool flag=true;
		vector<ll>aux;
		for(int j=2; j<=10 && flag; j++)
		{
			ll x=val(i, j, n);
			ll y=valid(x);
			if(y)
				aux.pb(y);
			else
				flag=false;
		}
		if(flag)
		{
			bin(i, n);
			printf(" ");
			for(int j=0; j<aux.size(); j++)
			{
				j>0?printf(" "):NULL;
				printf("%lld", aux[j]);
			}
			printf("\n");
			m--;
		}
	}
}

void init()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//cout << "[FREOPEN]" << endl;
	return;
}

int main()
{
	//init();
	int tt;
	scanf("%d", &tt);
	for(int t=1; t<=tt; t++)
	{
		int n, m;
		scanf("%d %d", &n, &m);
		printf("Case #%d:\n", t);
		solve(n, m);
	}
 	return 0;
}

