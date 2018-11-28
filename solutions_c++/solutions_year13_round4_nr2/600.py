#include <stdio.h>
#include <string>
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

#define PROBLEM "B"
#define INSTANCE "small"
#define CONSOLE false

int N;
long long P;

void shu(vector<int> &a, int S, int T) {
	vector<int> win, lose;
	for(int k=S; k<T; k += 2) {
		int L, W;
		lose.push_back( L = max(a[k], a[k+1]) );
		win.push_back( W = min(a[k], a[k+1]) );
	}
	int k = S;
	for(int x : win) a[k++] = x;
	for(int x : lose) a[k++] = x;
}

bool round1(long long k) {
	int num = 1<<N;

	vector<int> tour;
	tour.push_back(k);
	for(int j=0; j<k; ++j) tour.push_back(j);
	for(int j=k+1; j<(1<<N); ++j) tour.push_back(j);

	int sz = num;
	REP(iter, N) {
		for(int st = 0; st < num; st += sz) {
			shu(tour, st, st + sz);
		}
		sz /= 2;
	}
	int v = find(all(tour), k) - tour.begin();
	return v < P;
}

long long go() {
	long long l = 0, r = (1LL << N) - 1;
	long long ans1;
	while(l <= r) {
		long long k = (l+r) / 2;
		if( round1(k) ) {
			ans1 = k;
			l = k+1;
		}
		else r = k-1;
	}
	return ans1;
}

bool round2(long long k) {
	int num = 1<<N;

	vector<int> tour;
	tour.push_back(k);
	for(int j = num - 1; j >= 0; -- j) {
		if(j!=k)
			tour.push_back(j);
	}

	int sz = num;
	REP(iter, N) {
		for(int st = 0; st < num; st += sz) {
			shu(tour, st, st + sz);
		}
		sz /= 2;
	}
	int v = find(all(tour), k) - tour.begin();
	return v < P;
}

long long go2() {
	long long l = 0, r = (1LL << N) - 1;
	long long ans1;
	while(l <= r) {
		long long k = (l+r) / 2;
		if( round2(k) ) {
			ans1 = k;
			l = k+1;
		}
		else r = k-1;
	}
	return ans1;
}


int main() {
	int T;
	freopen(PROBLEM "-" INSTANCE ".in", "r", stdin);
	if(!CONSOLE) {
		freopen(PROBLEM "-" INSTANCE ".out", "w", stdout);
	}

	cin >> T;

	for(int tt=1; tt<=T; ++tt) {
		cout << "Case #" << tt << ": ";
		cin >> N >> P;

		cout << go() << ' ';
		cout << go2() << ' ';
		cout << endl;
	}

	return 0;
}
