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

void solve(int x)
{
	if(x==0)
	{
		printf("INSOMNIA\n");
		return;
	}
	set<int>num;
	int n=x;
	while(num.size()!=10)
	{
		int aux=n;
		while(aux>0)
		{
			num.insert(aux%10);
			aux/=10;
		}
		if(num.size()<10)
			n+=x;
	}
	printf("%d\n", n);
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
		int x;
		scanf("%d", &x);
		printf("Case #%d: ", t);
		solve(x);
	}
 	return 0;
}

