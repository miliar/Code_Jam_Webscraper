#include <stdio.h>
#include <string>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
#define all(v) v.begin(), v.end()
#define REP(i, n) for(int i=0; i<(int)(n); ++ i) 
#define uniquify(v) {sort(all(v));(v).erase(unique(all(v)), (v).end());}

#define PROBLEM "A"
#define INSTANCE "large"
#define CONSOLE false

int N, M;
int st[1000], ed[1000], amt[1000];

vector<pair<int, int>> X;

struct maxheap {
	map<int, long long> M;
	void push(int v, int amt) {
		M[v] += amt;
	}
	vector<pair<int, long long> > pop(int amt) {
		vector<pair<int, long long> > ret;
		while(amt > 0) {
			pair<int, long long> entry = *M.rbegin();

			long long t = std::min<long long>(entry.second, amt);
			ret.push_back( make_pair(entry.first, t) );
			M[entry.first] -= t;
			amt -= t;
			if(M[entry.first] == 0) {
				M.erase(entry.first);
			}
		}
		return ret;
	}
};

long long cost(long long d) {
	if(d == 1) return N;
	long long val =  d * N - (d * (d+1) / 2);
	return val % 1000002013;
}

long long go() {
	sort(all(X), [](pair<int, int> &A, pair<int, int> &B) {
		if(A.first != B.first) return A.first < B.first;
		return A.second > B.second;
	});

	long long orig = 0;
	for(int i=0; i<M; ++i) {
		orig += (long long)amt[i] * cost(ed[i] - st[i]);
		orig %= 1000002013;
	}

	maxheap passengers;
	long long ans = 0;
	for(pair<int, int> e : X) {
		int at = e.first;
		int man = e.second;
		if(man > 0) {
			passengers.push(at, man);
		}
		else {
			vector<pair<int, long long>> ret = passengers.pop(-man);
			for(pair<int, long long> &entry : ret) {
				ans += entry.second * cost(at - entry.first);
				ans %= 1000002013;
			}
		}
	}
	long long tt =  orig - ans;
	tt += 1000002013;
	tt %= 1000002013;
	return tt;
}

int main() {
	int T;
	if(!CONSOLE) {
		freopen(PROBLEM "-" INSTANCE ".in", "r", stdin);
		freopen(PROBLEM "-" INSTANCE ".out", "w", stdout);
	}

	cin >> T;

	for(int tt=1; tt<=T; ++tt) {
		cin >> N >> M;
		X.clear();
		REP(i, M) {
			cin >> st[i] >> ed[i] >> amt[i];
			X.push_back(make_pair(st[i], amt[i]));
			X.push_back(make_pair(ed[i], -amt[i]));
		}
		cout << "Case #" << tt << ": ";
		cout << go() % 1000002013 << endl;
	}

	return 0;
}
