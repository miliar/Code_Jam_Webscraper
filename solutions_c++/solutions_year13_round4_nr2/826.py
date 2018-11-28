/*
 TASK:B
 LANG:C++
 Muhammad Magdi Muhammad
 Email: moh_magdi@acm.org
 */
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define OO ((int)1e9)
#define MAX 100000

typedef long long ll;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
int I, J;
inline bool valid(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

using namespace std;

#define SMALL
//#define LARGE
int T;
vector<int> solve(vector<int> arr, int N, int P) {
	if (N == 0) {
		vector<int> res;
		rep(i,arr.size()) {
			res.pb(arr[i]);
		}
		return res;
	}
	int c = 0, m = arr.size();
	vector<int> t(m);
	for (int i = 0; i < m; i += 2) {
		t[c] = min(arr[i], arr[i + 1]);
		t[m / 2 + c] = max(arr[i], arr[i + 1]);
		c++;
	}
	return solve(t, N - 1, P);
}

/*
 vector<int> arr;
 rep(i,(1<<N))
 arr.pb(i);
 vector<int> best((1 << N), OO);
 vector<int> wost((1 << N), 0);
 do {
 vector<int> fs = solve(arr, N, P);
 rep(i,fs.size()) {
 int c = fs[i];
 best[c] = min(best[c], i);
 wost[c] = max(wost[c], i);
 }
 } while (next_permutation(all(arr)));
 rep(i,best.size()) {
 cout << i << " best " << best[i] << " ,worst " << wost[i] << endl;
 }
 */

ll v(int ind, int N) {
	ll res = 0;
	ll cnt = ind;
	for (int i = 0; i <= N; ++i) {
		if (i)
			cnt = (cnt - 1) / 2;
		if (cnt > 0)
			res |= (1LL << (N - i - 1));
	}
	return res;
}
ll w(int ind, int N) {
	ll res = 0;
	ll cnt = (1LL << N) - ind - 1;
	for (int i = 0; i < N; ++i) {
		if (i)
			cnt = (cnt - 1) / 2;
		if (cnt == 0)
			res |= (1LL << (N - i - 1));
	}
	return res;
}

int main() {
	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	cin >> T;
	rep(tt,T) {
		printf("Case #%d: ", tt + 1);
		ll N, P;
		cin >> N >> P;
//		vector<int> arr;
//		rep(i,(1<<N))
//			arr.pb(i);
//		vector<int> best((1 << N), OO);
//		vector<int> wost((1 << N), 0);
//		do {
//			vector<int> fs = solve(arr, N, P);
//			rep(i,fs.size()) {
//				int c = fs[i];
//				best[c] = min(best[c], i);
//				wost[c] = max(wost[c], i);
//			}
//		} while (next_permutation(all(arr)));
//		rep(i,best.size()) {
//			cout << i << " best " << best[i] << " ,worst " << wost[i] << endl;
//			cout << i << " best " << w(i,N) << " ,worst " << v(i,N) << endl;
//		}
		ll s = 0, e = (1LL << N)-1;
		while (s < e) {
			ll md = (s + (e - s) / 2) + 1;
			if (v(md, N) < P) {
				s = md;
			} else {
				e = md - 1;
			}
		}
		cout << s << " ";
		s = 0, e = (1LL << N)-1;
		while (s < e) {
			ll md = (s + (e - s) / 2) + 1;
			if (w(md, N) < P) {
				s = md;
			} else {
				e = md - 1;
			}
		}
		cout << s << endl;
//		cerr << tt << endl;
	}
	return 0;
}
//end

