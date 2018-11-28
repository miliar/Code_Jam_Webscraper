#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}

int solve() {
	int k, c, s; cin >> k >> c >> s;
	if (c == 1 && s == k) {
		for(int i = 1; i <= s; ++i) cout << " " << i;
		return 0;
	}
	if (c * s < k) {
		cout << "IMPOSSIBLE";
		return 0;
	}
	vector<long long> pp;
	pp.push_back(1);
	for(int i = 1; i <= c; ++i) {
		pp.push_back(pp[i - 1] * k);
	}
	int d = 1;
	while (d <= k) {
		long long res = 0;
		for(int i = 0; i < c; ++i) {
			res += pp[c - 1 - i] * (min(d - 1 + i, k - 1));
		}
		cout << " " << res + 1; 
		d += c;
	}


	return 0;
}

int main() {
	int t; cin >> t;
	for(int x = 1; x <= t; ++x){
		cout << "Case #" << x << ":"; solve();//result 
		cout << endl;
	}
	return 0;
}
