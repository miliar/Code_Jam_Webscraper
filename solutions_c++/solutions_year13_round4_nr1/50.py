#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

const int mod =	1000002013;

int n, m;

long long was, ans;

set <pair <int, pair <int, int> > > s;

vector <pair <int, pair <int, int> > > q;

void load() {
	was = 0, ans = 0;
	q.clear();
	s.clear();

	cin >> m >> n;

	for (int i = 0;i < n;i++) {
		long long o, e, p;
	 	cin >> o >> e >> p;

	 	long long l = e - o;
	 	was += (l * 1ll * m % mod - (l * 1ll * (l + 1)) / 2 % mod + mod) % mod * p % mod;
	 	was %= mod;

	 	q.push_back (make_pair (o, make_pair (0, p)));
	 	q.push_back (make_pair (e, make_pair (1, p))); 
	}
}

void solve(int test) {
	sort (q.begin(), q.end());

	for (int i = 0;i < (int)q.size();i++) {
		if (q[i].second.first == 0) {
			s.insert (make_pair (-q[i].first, make_pair (q[i].second.second, i)));
			continue;
		}

		 	pair <int, pair <int, int > > cur = *s.begin();
		 	s.erase (cur);

		 	int t = q[i].second.second;

		 	//cerr << t << " " << cur.second.first << endl;

		 	while (t > 0) {
		 	 	long long w = min (cur.second.first, t);

		 	 	cur.second.first -= w;
		 	 	t -= w;

		 	 	long long l = q[i].first + cur.first;

		 	 	ans += (l * 1ll * m % mod - (l * 1ll * (l + 1)) / 2 % mod + mod) % mod * w % mod;
		 	 	ans %= mod;

		 	   	if (cur.second.first > 0) {
		 	   	 	s.insert (cur);
		 	   	 	break;
		 	   	}

		 	   	cur = *s.begin();
		 	   	s.erase (cur);
		 	}

		 	if (cur.second.first > 0) {
		 	 	s.insert (cur);
		 	}
   	}

   	printf ("Case #%d: %d\n", test, (was - ans + 0ll  + mod) % mod);
}

int main() {
 	freopen ("a.in", "r", stdin);
 	freopen ("a.out", "w", stdout);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		load();
 		solve(i);
 	}

 	return 0;
}