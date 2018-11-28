#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 0

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

lint md = 1000002013;

int solution(int nTest) {
	int Nr, m;
	scanf("%d%d", &Nr, &m);
	lint N = Nr;
	vector<pair<int, pii> > v;
	lint could = 0;
	For(i, 0, m) {
		int o, e, p;
		scanf("%d%d%d", &o, &e, &p);
		v.pb(mp(o, mp(0, p)));
		v.pb(mp(e, mp(1, p)));
		lint n = e - o;
		lint r = N;
		r *= n;
		r -= n * (n-1)/2;
		r %= md;
		r *= p;
		r %= md;
		could += r;
		could %= md;
	}
	cerr << could << endl;
	priority_queue<pii> q;
	sort(all(v));
	lint sum = 0;
	
	For(i, 0, sz(v)) {
		int t = v[i].second.first;
		int p = v[i].second.second;
		int o = v[i].first;
		if(t == 0) {
			q.push(mp(o, p));
		} else {
			while(p > 0) {
				int topS = q.top().first;
				int topP = q.top().second;
				q.pop();
				if(p >= topP) {
					p -= topP;
					lint n = o - topS;
					lint r = N;
					r *= n;
					r -= (n * (n-1))/2;
					r %= md;
					r *= topP;
					r %= md;
					sum += r;
					sum %= md;
				} else {
					topP -= p;
					lint n = o - topS;
					lint r = N;
					r *= n;
					r -= (n * (n-1))/2;
					r %= md;
					r *= p;
					r %= md;
					sum += r;
					sum %= md;
					q.push(mp(topS, topP));
					p = 0;
				}
			}
		}
	}
	cerr << could << " " << sum << endl;
	cerr << q.size() << endl;
	if(could < sum) {
		could += md;
	}
	cout << could - sum << endl;

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
