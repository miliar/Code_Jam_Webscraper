#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

bool match(string& S, int n) {
	int L = S.size();
	for (int i=L-1; i>=0; --i) {
		if (S[i] != '?') {
			int c = S[i] - '0';
			if (c != n % 10) return false;
		}
		n /= 10;
	}
	return true;
}

// string C, J;
vector<int> C, J;
int L;

string pad(ll n) {
	vector<char> tmp(L, '0');
	for (int i=L-1; i>=0; --i) {
		tmp[i] = '0' + (int)(n % 10LL);
		n /= 10LL;
	}
	return string(all(tmp));
}


#define QM 15

typedef pair<int,int> i2;
typedef pair<ll,ll> ll2;

ll2 solve() {
	queue< pair<i2,ll2> > q;
	q.push(make_pair(i2(0,0), ll2(0,0)));

	vector< vector<ll> > tmp;

	while (!q.empty()) {
		int ix = q.front().first.first, cm = q.front().first.second;
		ll c_ = q.front().second.first, j_ = q.front().second.second;
		q.pop();

		// printf("(%d, %d, %lld, %lld)...\n", ix,cm, c_, j_);

		if (ix == L) {
			vector<ll> o(3);
			o[0] = abs(c_ - j_);
			o[1] = c_;
			o[2] = j_;
			tmp.push_back(o);
			continue;
		}

		ll c = c_ * 10LL, j = j_ * 10LL;

		ll c0 = 0, j0 = 0;
		if (C[ix] != QM) c0 = C[ix];
		if (J[ix] != QM) j0 = J[ix];

		if (cm == 1) {
			// C < J
			if (C[ix] == QM) c0 = 9;
			if (J[ix] == QM) j0 = 0;
			q.push(make_pair(i2(ix+1,1),ll2(c+c0,j+j0)));
			continue;
		}
		if (cm == -1) {
			// c > j
			if (C[ix] == QM) c0 = 0;
			if (J[ix] == QM) j0 = 9;
			q.push(make_pair(i2(ix+1,-1),ll2(c+c0,j+j0)));
			continue;
		}
		// then cm == 0

		vector<ll2> tmp;
		if (C[ix] == QM) {
			if (J[ix] == QM) {
				// ? ?
				c0 = j0 = 0;
				q.push(make_pair(i2(ix+1,0),ll2(c+c0,j+j0))); // c == j
				c0 = 0; j0 = 1;
				q.push(make_pair(i2(ix+1,1),ll2(c+c0,j+j0))); // c < j
				c0 = 1; j0 = 0;
				q.push(make_pair(i2(ix+1,-1),ll2(c+c0,j+j0))); // c > j
			} else {
				// J[ix] = 0..9
				if (j0 > 0) {
					c0 = j0 - 1;
					q.push(make_pair(i2(ix+1,1),ll2(c+c0,j+j0))); // c < j
				}
				c0 = j0;
				q.push(make_pair(i2(ix+1,0),ll2(c+c0,j+j0))); // c == j
				if (j0 < 9) {
					c0 = j0 + 1;
					q.push(make_pair(i2(ix+1,-1),ll2(c+c0,j+j0))); // c > j
				}
			}
		} else {
			// C[ix] = 0..9
			if (J[ix] == QM) {
				if (c0 > 0) {
					j0 = c0 - 1;
					q.push(make_pair(i2(ix+1,-1),ll2(c+c0,j+j0))); // c > j
				}
				j0 = c0;
				q.push(make_pair(i2(ix+1,0),ll2(c+c0,j+j0))); // c == j
				if (c0 < 9) {
					j0 = c0 + 1;
					q.push(make_pair(i2(ix+1,1),ll2(c+c0,j+j0))); // c < j
				}
			} else {
				int cm;
				if (c0 < j0) cm = 1;
				else if (c0 > j0) cm = -1;
				else cm = 0;
				q.push(make_pair(i2(ix+1,cm),ll2(c+c0,j+j0))); // c == j
			}
		}
	}

	sort(all(tmp));
	// cout << tmp << endl;
	return make_pair(tmp[0][1], tmp[0][2]);
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  	string c,j; cin >> c >> j;
 	L = c.size();
 	C.resize(L); J.resize(L);
 	rep(i,L) {
 		C[i] = c[i] - '0';
 		J[i] = j[i] - '0'; // '?' -> 15
 	}
  	ll2 ans = solve();
 answer:
    cout << "Case #" << (1+_t) << ": " << pad(ans.first) << " " << pad(ans.second) << endl;
  }
}
