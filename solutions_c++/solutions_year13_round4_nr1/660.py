#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <iomanip>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long LL;
typedef long double ldb;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <vb> vvb;

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;
const ldb PI = fabs(atan2(0.0, -1.0));
const LL MOD = 1000002013LL;

int n, m;
int from[1111];
int to[1111];
int cnt[1111];
void load()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++)
		scanf("%d%d%d", &from[i], &to[i], &cnt[i]);
}

LL calc(int from, int to)
{
	LL length = to - from;
	return (((2LL * n - length + 1) * length) / 2) % MOD;
}

class Event
{
public:
	int x;
	int from;
	LL cnt;
	int type;

	Event() {};

	Event(int x, int from, LL cnt, int type)
	{
		this->x = x;
		this->from = from;
		this->cnt = cnt;
		this->type = type;
	}
};

bool operator < (const Event &a, const Event &b)
{
	if (a.x != b.x) return a.x < b.x;
	if (a.type != b.type) return a.type > b.type;
	return a.from < b.from;
}

class Item
{
public:
	int from;
	int to;
	LL cnt;

	Item() {};

	Item(int from, int to, LL cnt)
	{
		this->from = from;
		this->to = to;
		this->cnt = cnt;
	}
};

bool operator < (const Item &a, const Item &b)
{
	if (a.from != b.from) return a.from > b.from;
	if (a.to != b.to) return a.to < b.to;
	return a.cnt < b.cnt;
}

#define ends my_ends

void solve(int test)
{
	vector <Event> evs;
	LL wanted = 0;
	for (int i = 0; i < m; i++)
	{
		wanted += (calc(from[i], to[i]) * cnt[i]) % MOD;
		if (wanted >= MOD) wanted -= MOD;
		evs.pb(Event(from[i], to[i], cnt[i], 1));
		evs.pb(Event(to[i], from[i], cnt[i], -1));
	}
	sort(evs.begin(), evs.end());
	multiset <Item> alive;
	LL best = 0;
	for (int i = 0; i < (int)evs.size(); i++)
	{
		Event e = evs[i];
		if (e.type == 1)
			alive.insert(Item(e.x, e.from, e.cnt));
		else
		{
			LL cnt = e.cnt;
			for ( ; cnt > 0 && !alive.empty(); )
			{
				Item item = *alive.begin();
				alive.erase(alive.begin());

				LL pay = min(item.cnt, cnt);
				item.cnt -= pay;
				cnt -= pay;
				if (item.cnt > 0)
					alive.insert(item);
				best += (calc(item.from, e.x) * pay) % MOD;
				if (best >= MOD) best -= MOD;	
			}
		}	
	}

	cerr << wanted << " " << best << endl;
	LL answer = (wanted - best + MOD) % MOD;
	printf("Case #%d: "LLD"\n", test, answer);
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		load();
		solve(test);
	}	
	return 0;
}
