#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(),"r",stdin);
		freopen((s + ".out").c_str(),"w",stdout);
	}
#endif
}
	

void read(vector< string > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(s.substr(1, sz(s) - 2));
		cin >> s;
	}
}
void read(string &s)
{
	cin >> s;
	s = s.substr(1, sz(s) - 2);
}

void read(vector< int > &a)
{
	string s;
	cin >> s;
	cin >> s;
	while (s != "}")
	{
		a.push_back(atoi(s.c_str()));
		cin >> s;
	}
}

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool in(int x, int y, int n, int m)
{
	if (x < 0 || y < 0 || x >= n + 2 || y >= m + 2)
		return false;
	return true;;
}

struct Event
{
	int time, type, id;
	Event(int time, int type, int id):time(time), type(type), id(id){}

	bool operator < (const Event &oth) const
	{
		return mp(mp(time, type), id) < mp(mp(oth.time, oth.type), oth.id);
	}

};

bool solve()
{
	int n,m;
	cin >> n >> m;
	vector< vector<int> > a(n, vector<int>(m, 0));
	for (int i = 0; i < n; ++ i)
		for (int j = 0; j < m; ++ j)
			cin >> a[i][j];

	//hor
	vector<int> h(n);
	for (int i = 0; i < n; ++ i)
	{
		int cur = 0;
		for (int j = 0; j < m; ++ j)
			cur = max(cur, a[i][j]);
		h[i] = cur;
	}
	//vert
	vector<int> v(m, 0);
	for (int j = 0; j < m; ++ j)
	{
		for (int i = 0; i < n; ++ i)
			v[j] = max(v[j], a[i][j]);
	}
	vector< Event > e;
	for (int i = 0; i < n; ++ i)
		e.push_back(Event(-h[i], 0, i));
	
	for (int i = 0; i < m; ++ i)
		e.push_back(Event(-v[i], 1, i));

	sort(all(e));
	vector< vector<int> > b(n, vector<int> (m, INF));

	for (int i = 0; i < sz(e); ++ i)
	{
		int x, y, dx, dy, color = -e[i].time;
		if (e[i].type == 0)
		{
			x = e[i].id;
			dx = 0;
			y = 0;
			dy = 1;
		}
		else
		{
			x = 0;
			y = e[i].id;
			dx = 1;
			dy = 0;
		}

		while (x < n && y < m)
		{
			b[x][y] = min(b[x][y], color);
			x += dx;
			y += dy;
		}
	}

	if (a != b)
		cout << "NO";
	else
		cout << "YES";

	return false;
}

int main()
{
	prepare("input_txt");
	int T;
	cin >> T;
	int id = 0;
	while (T--)
	{
		cout << "Case #" << ++ id << ": " ;
	solve();
		cerr << "Case #" << id << ": " << endl ;
		cout << endl;
	}
	return 0;
}
