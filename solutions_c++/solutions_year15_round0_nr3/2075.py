#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cstdlib>
#include <cassert>

using namespace std;

typedef long long ll;
typedef double db;
typedef long double ldb;
typedef string str;

#define forn(i, n) for(int i = 0; i < n; ++i)
#define INF 1e+9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define X first
#define Y second
#define ms(x) memset(x, 0, sizeof(x))
#define ms1(x) memset(x, -1, sizeof(x))
#define sz(x) ( (int) x.size() )
#define len(x) ( (int) x.length() )
#define ALL(x) x.begin(), x.end()
#define pii pair<int, int>
#define pdd pair<double, double>

int cnt = 0;

struct num{
	int sig, val;

	num() { sig = val = 0; }

	num(int sig, int val){
		this->sig = sig;
		this->val = val;
	}

	num operator * (const num &o) const{
		int sig = o.sig ^ this->sig;
		if (o.val == val) return num(sig ^ 1, 0);
		if (val == 0) return num(sig, o.val);
		if (o.val == 0) return num(sig, val);
		if (val == 1){
			if (o.val == 2) return num(sig, 3);
			return num(sig ^ 1, 2);
		}
		if (val == 2){
			if (o.val == 1) return num(sig ^ 1, 3);
			return num(sig, 1);
		}
		if (val == 3){
			if (o.val == 1) return num(sig, 2);
			return num(sig ^ 1, 1);
		}
	}
};

int toInt(char ch){
	if (ch == '1') return 0;
	if (ch == 'i') return 1;
	if (ch == 'j') return 2;
	return 3;
}

void solve(int cnt){
	bool ans = false;
	int l, x;
	cin >> l >> x;
	string s;
	cin >> s;
	string orig = s;
	forn(i, x - 1) s += orig;
	num cur(0, 0);
	int ccc = 0;
	forn(i, len(s)){
		int now = toInt(s[i]);
		cur = cur * num(0, now);
		if (cur.sig == 0 && cur.val == 1 && ccc == 0) {
			ccc++;
			cur = num(0, 0);
		}
		if (cur.sig == 0 && cur.val == 2 && ccc == 1){
			ccc++;
			cur = num(0, 0);
		}
	}
	if (cur.sig == 0 && cur.val == 3) ccc++;
	if (ccc == 3) ans = true;
	printf("Case #%d: ", cnt);
	if (ans) printf("YES");
	else printf("NO");
	printf("\n");
}
int main(){
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	while(t--) solve(++cnt);
#ifdef _DEBUG
	cout << fixed << setprecision(15) << clock() * 1. /  CLOCKS_PER_SEC;
#endif
	return 0;
}
