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

int solve(stack<int>&data)
{
	int n=data.size();
	int ret=0;
	stack<int>aux;
	while(aux.size()!=n)
	{
		if(aux.empty() || (aux.top()==data.top()))
		{
			aux.push( data.top() );
			data.pop();
		}
		else
		{
			while(!aux.empty())
			{
				data.push( aux.top()^1 );
				aux.pop();
			}
			ret++;
		}
	}
	return ret+(aux.top()==0);
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
		string st;
		cin >> st;
		stack<int>data;
		for(int i=st.size()-1; i>=0; i--)
		{
			data.push( st[i]=='+'?1:0 );
		}
		printf("Case #%d: %d\n", t, solve(data));
	}
 	return 0;
}

