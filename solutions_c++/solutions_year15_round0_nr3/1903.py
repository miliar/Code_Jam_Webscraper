#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <array>
#include <climits>
#include <bitset>
#include <cassert>
#include <unordered_map>

#ifdef _MSC_VER
#include <agents.h>
#endif

#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define UNIQUE(v) (v).erase(unique(ALL(v)), (v).end())
#define MP make_pair
#define MT make_tuple

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;

int x[4][4] = {
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4},
};

int calc(int a, int b){
	int tmp = (a & 4) ^ (b & 4);
	return tmp ^ x[a & 3][b & 3];
}

int ch[256];

int get(string &s, int idx, int x, int y, int end = 0, int rev = 0){
	if (!end) end = s.size();

	int st = x;
	FOR(i, idx, end){
		if(!rev) st = calc(st, ch[s[i]]);
		else st = calc(ch[s[i]], st);
		if (st == y) return i + 1;
	}
	return -st;
}

int get_ch(string &s, int y, int rev = 0){
	int n = s.size();
	int cnt[10] = {};

	int st = 0;
	rep(i, 10){
		if (cnt[st]) break;
		cnt[st] = 1;
		st = get(s, 0, st, y, 0, rev);
		if (st > 0) return i*n + st;
		st = -st;
	}

	return -1;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);
	cout.setf(ios::fixed);
	cout.precision(20);

	rep(i, 4) ch["1ijk"[i]] = i;

	int t;
	cin >> t;
	for (int cn = 1; cn <= t; ++cn){
		ll L, X;
		cin >> L >> X;
		string s;
		cin >> s;
		string t = s;
		reverse(ALL(t));

		ll a = get_ch(s, ch['i']);
		ll b = get_ch(t, ch['k'], 1);

		// small
		//t = "";
		//rep(i, X) t += s;
		//s = t;
		//reverse(ALL(t));

		//bool sok = false;
		//a = get_ch(s, ch['i']);
		//b = get_ch(t, ch['k'], 1);
		//sok = -get(s, a, 0, -1, X*L - b) == 2;

		//cout << "Case #" << cn << ": " << (sok ? "YES" : "NO") << endl;
		//continue;
		// small-end

		bool ok = false;
		if (a > 0 && b > 0 && a + b < L*X){
			int aa = 0;
			if (a/L+b/L == X-1){
				aa = -get(s, a, aa, -1, L - b%L);
			}
			else{
				aa = -get(s, a%L, ch['1'], -1);
				if (a%L == 0) aa = 0;
				int n = (X  - (a + L - 1) / L - (b + L - 1) / L)%4;
				int res = -get(s, 0, ch['1'], -1);
				rep(i, n) aa = calc(aa, res);
				int bb = -get(t, b%L, ch['1'], -1, 0, 1);
				if (b%L == 0) bb = 0;
				aa = calc(aa, bb);
			}
			if (aa == ch['j']) ok = true;
		}

		cout << "Case #" << cn << ": " << (ok?"YES":"NO") << endl;
	}

}
