#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef long long lng;
typedef unsigned long long ulng;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, PII> PIII;
typedef pair<lng, PII> PLII;
#define FAIL ++*(int*)0
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define RR 151
#define X first
#define Y second
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "B"

map<vector<int>, int> dist;

bool check(const vector<int> &a) {
	int max_id = int(max_element(all(a)) - a.begin());
	for (int i = 0; i + 1 < max_id; ++i)
		if (a[i] > a[i + 1])
			return false;
	for (int i = sz(a) - 1; i - 1 > max_id; --i)
		if (a[i - 1] < a[i])
			return false;
	return true;
}

int bf(vector<int> state) {
	dist.clear();
	priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> pq;
	pq.push(mp(0, state));
	dist[pq.top().Y] = 0;
	while (!pq.empty()) {
		int curd = pq.top().X;
		vector<int> cur = pq.top().Y;
		pq.pop();
		if (curd != dist[cur])
			continue;
		if (check(cur)) {
			/*for (int i = 0; i < sz(cur); ++i)
				cout << cur[i] << ' ';
			cout << endl;*/
			return curd;
		}
		for (int i = 0; i + 1 < sz(cur); ++i) {
			swap(cur[i], cur[i + 1]);
			if (!dist.count(cur)) {
				dist[cur] = curd + 1;
				pq.push(mp(curd + 1, cur));
			}
			swap(cur[i], cur[i + 1]);
		}
	}
	return INF;
}

struct RSQ {
	int n;
	int tr[1000];

	void clear(int n) {
		this->n = n;
		clr(tr, 0);
	}

	void update(int i, int dx) {
		for (; i < n; i |= i + 1)
			tr[i] += dx;
	}

	int get(int i) {
		int res = 0;
		for (; i >= 0; i = (i & (i + 1)) - 1)
			res += tr[i];
		return res;
	}

	int get(int l, int r) {
		return get(r) - get(l - 1);
	}
};

int n;
vector<int> a;
RSQ rsq;

int doit(vector<int>::iterator begin, vector<int>::iterator end, bool rev = false) {
	if (begin >= end)
		return 0;
	if (rev) reverse(begin, end);
	rsq.clear(n);
	int res = 0;
	for (vector<int>::iterator it = end - 1; ; --it) {
		res += rsq.get(*it - 1);
		rsq.update(*it, +1);
		if (it == begin)
			break;
	}
	if (rev) reverse(begin, end);
	return res;
}

int ddoit(vector<int> na) {
	int max_id = int(max_element(all(na)) - na.begin());
	int res = doit(na.begin(), na.begin() + max_id) + doit(na.begin() + max_id + 1, na.end(), true);
	res = min(res, doit(all(na)));
	res = min(res, doit(all(na), true));
	{
		vector<int> a = na;
		int min_id = int(min_element(all(a)) - a.begin());
		a.erase(a.begin() + min_id, a.begin() + min_id + 1);
		res = min(res, doit(all(a)) + min(min_id, sz(na) - min_id - 1));
		res = min(res, doit(all(a), true) + min(min_id, sz(na) - min_id - 1));
	}
	{
		vector<int> a = na;
		int add = 0;
		for (int i = max_id - 1; i >= 0; --i) {
			swap(a[i], a[i + 1]);
			++add;
			res = min(res, doit(a.begin(), a.begin() + i) + doit(a.begin() + i + 1, a.end(), true) + add);
		}
	}
	{
		vector<int> a = na;
		int add = 0;
		for (int i = max_id + 1; i < n; ++i) {
			swap(a[i - 1], a[i]);
			++add;
			res = min(res, doit(a.begin(), a.begin() + i) + doit(a.begin() + i + 1, a.end(), true) + add);
		}
	}
	return res;
}

void solve() {
	cin >> n;
	a.resize(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	vector<int> b = a;
	sort(all(b));
	for (int i = 0; i < n; ++i) {
		a[i] = int(lower_bound(all(b), a[i]) - b.begin());
		//cout << a[i] << ' ';
	}
	//cout << endl;

	//int res = ddoit(a);
	int res = bf(a);
	printf("%d\n", res);

	/*int ans = bf(a);
	if (res != ans) {
		cerr << "FAIL" << endl;
		cerr << "NEED: " << ans << endl;
		cerr << "HAVE: " << res << endl;
		exit(13);
	}*/
}

//#define DEBUG
#define SMALL
//#define LARGE

void stress() {
	for (n = 1; n <= 10; ++n) {
		vector<int> a;
		for (int i = 0; i < n; ++i)
			a.push_back(i);
		cerr << n << endl;
		do {
			int res = ddoit(a);
			int ans = bf(a);
			if (res != ans) {
				cerr << "FAIL" << endl;
				cerr << "NEED: " << ans << endl;
				cerr << "HAVE: " << res << endl;
				cout << n << endl;
				for (int i = 0; i < n; ++i)
					cout << a[i] << ' ';
				cout << endl;
				exit(13);
			}
		} while(next_permutation(all(a)));
	}
}

int main() {
#ifdef SMALL                                   
    freopen(TASK "-small-attempt2.in", "r", stdin);
    freopen(TASK "-small-attempt2.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	//stress();

	int T;
	char buf[32];
	gets(buf);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
