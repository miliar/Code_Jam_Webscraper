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
typedef pair < lint , lint > pll;
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

const int MAXN = 2041;

int start_day[MAXN];
int start_strength[MAXN];
int cnt_step[MAXN];
int leftb[MAXN];
int rightb[MAXN];
int delta_day[MAXN];
int delta_dist[MAXN];
int delta_strength[MAXN];

struct Event
{
	lint day, from, to, strength;
	int type;
	Event(lint day, lint from, lint to, lint strength, int type):day(day),
		from(from),
		to(to),
		strength(strength),
		type(type)
	{}


	bool operator < (const Event &oth) const 
	{
		if (day != oth.day)
			return day < oth.day;
		return type < oth.type;
	}
};

struct Node;
typedef Node * tNode;


struct Node
{
	tNode left, right;
	lint leftb, rightb;
	int same;
	lint val;


	void push()
	{
		if (same && left)
		{
			left->same = right->same = same;
			left->val = right->val = val;
		}
	}

	lint Max(lint l, lint r)
	{
		if (same && l <= leftb && rightb <= r)
		{
			return val;
		}
		if (l > rightb || leftb > r)
			return -1;
		push();
		return max(left->Max(l, r), right->Max(l, r)); 
	}

	lint Min(lint l, lint r)
	{
		if (same && l <= leftb && rightb <= r)
		{
			return val;
		}
		if (l > rightb || leftb > r)
			return LINF;
		push();
		return min(left->Min(l, r), right->Min(l, r)); 
	}

	void Upd()
	{
		if (left)
		{
			if (left->same && right->same && left->val == right->val)
			{
				same = 1;
				val = left->val;
			}
			else
				same = 0;
		}
	}

	void rebuild(lint l, lint r, lint new_val)
	{
		/*if (!this)
		{
			int xxxx = -1;
		}*/
		if (same && l <= leftb && rightb <= r)
		{
			val = max(val, new_val);
			return ;
		}
		if (l > rightb || leftb > r)
			return ;
		push();
		left->rebuild(l, r, new_val);
		right->rebuild(l, r, new_val);
		Upd();
	}
};

Node arr[1000 * 1000 * 4];
int last = 0;
tNode make_node(int l, int r, vector<pll> &p)
{
	tNode res = &(arr[last++]);
	res->val = 0;
	res->same = 1;
	res->leftb = p[l].first;
	res->rightb = p[r].second;
	res->left = res->right = NULL;
	if (l != r)
	{
		int m = (l + r) >> 1;
		res->left = make_node(l, m, p);
		res->right = make_node(m + 1, r, p);
	}
	return res;
}




bool solve()
{
	int n;
	cin >> n;

	for (int i = 0; i < n; ++ i)
	{
		cin >> start_day[i] >> cnt_step[i] >>
			leftb[i] >> rightb[i] >> start_strength[i] >> 
			delta_day[i] >> delta_dist[i] >> 
			delta_strength[i];
	}
	vector<Event> events;
	for (int i = 0; i < n; ++ i)
	{
		lint left = leftb[i];
		lint right = rightb[i];
		lint strength = start_strength[i];
		lint day = start_day[i];

		for (int step = 0; step < cnt_step[i]; ++ step)
		{
			events.push_back(Event(day, left, right, strength, 0));
			events.push_back(Event(day, left, right, strength, 1));
			left += delta_dist[i];
			right += delta_dist[i];
			day += delta_day[i];
			strength += delta_strength[i];
		}
	}
	vector<lint> interv;
	for (int i = 0; i < sz(events); ++ i)
	{
		interv.push_back(events[i].from + 0);
		//interv.push_back(events[i].from + 1);
		//interv.push_back(events[i].from - 1);
		interv.push_back(events[i].to + 0);
		//interv.push_back(events[i].to + 1);
		//interv.push_back(events[i].to - 1);
	}
	interv.push_back(INF);
	interv.push_back(-INF);
	sort(all(interv));
	interv.erase(unique(all(interv)), interv.end());
	vector<pll> ppp;
	for (int i = 0; i < sz(interv) - 1; ++ i)
	{
		ppp.push_back(pii(interv[i], interv[i]));
		if (interv[i] + 1 < interv[i + 1])
			ppp.push_back(pii(interv[i] + 1, interv[i + 1] - 1));
	}
	
	tNode root = make_node(0, sz(ppp) - 1, ppp);
	int ans = 0;
	sort(all(events));
	for (int i = 0; i < sz(events); ++ i)
	{
		if (events[i].day == 3)
		{
			int xxxxx = -1;
		}
		if (events[i].type == 0)
		{
			if (root->Min(events[i].from, events[i].to - 1) < events[i].strength)
				++ ans;
		}
		else
		{
			root->rebuild(events[i].from, events[i].to - 1, events[i].strength);
		}
	}

	cout << ans;

	return false;
}

int main()
{
	prepare("input_txt");

	int T;
	cin >> T;
	for (int i = 0; i < T; ++ i)
	{
		cout << "Case #" << i + 1 << ": ";
		while (solve())
		{
	
		}
		cout << endl;
	}

	return 0;
}
