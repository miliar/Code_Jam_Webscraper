//#define _CRT_SECURE_NO_WARNINGS
//#include <iostream>
//#include <fstream>
//#include <cstdio>
//#include <map>
//#include <unordered_map>
//#include <string>
//#include <iomanip>
//#include <vector>
//#include <memory.h>
//#include <queue>
//#include <set>
//#include <unordered_set>
//#include <stack> 
//#include <algorithm>
//#include <math.h>
//#include <sstream>
//#include <functional>
//#include <bitset>
//using namespace std;
//#define mems(A, val) memset(A, val, sizeof(A))
//#define mp(a, b) make_pair(a, b)
//#define all(B) (B).begin(), (B).end()
//#define forn(it, from, to) for(int it = from; it < to; ++it)
//#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
//#define sz(a) (int)a.size()
//#define pb push_back
//const int MAXN = 35 * 1000;
//const double EPS = 1e-9;
//typedef long long LL;
//
//double D[205][205][205];
//bool used[205][205][205];
//vector<double> p;
//int k, n;
//
//double rec(int pos, int yes, int no){
//	if (pos == n){
//		if (yes == no && yes + no == k) return 1.0;
//		return 0.0;
//	}
//
//	double res = 0.0;
//	if (!used[pos + 1][yes + 1][no]){
//		used[pos + 1][yes + 1][no] = true;
//		D[pos + 1][yes + 1][no] = rec(pos + 1, yes + 1, no);
//	}
//
//	if (!used[pos + 1][yes][no+1]){
//		used[pos + 1][yes][no + 1] = true;
//		D[pos + 1][yes][no + 1] = rec(pos + 1, yes, no + 1);
//	}
//
//	res = max(res, (1.0 - p[pos]) * D[pos + 1][yes][no + 1] + p[pos] * D[pos + 1][yes + 1][no]);
//
//	if (!used[pos + 1][yes][no]){
//		used[pos + 1][yes][no] = true;
//		D[pos + 1][yes][no] = rec(pos + 1, yes, no);
//	}
//
//	res = max(res, D[pos + 1][yes][no]);
//
//	return res;
//}
//
////double calculate(int mask, vector<double> &pp_yes, vector<double> &pp_no, int count = 0, int o_mask = 0, int pt = 0){
////	if (!(mask & (1 << pt))) return calculate(mask, pp_yes, pp_no, pt + 1);
////	if (if ()
////}
//
//int main(int argc, char* argv[]) {
//
//#ifdef _DEBUG
//	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
//#else
//	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
//	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
//#endif
//	int ttt;
//	cin >> ttt;
//	forn(tt, 0, ttt){
//		mems(used, 0);
//		
//		cin >> n >> k;
//		p.resize(n);
//		forn(i, 0, n)cin >> p[i];
//		double res = 0.0;
//
//		//vector<double> pp_yes(1 << n);
//		//vector<double> pp_no(1 << n);
//
//		//for (int i = 0; i < (1 << n); ++i){
//		//	int count = 0;
//		//	for (int j = 0; j < n; ++j){
//		//		if (i&(1 << j))count++;
//		//	}
//
//		//	if (count * 2 == k){
//		//		pp_yes[i] = 1.0;
//		//		pp_no[i] = 1.0;
//		//		for (int j = 0; j < n; ++j){
//		//			if (i&(1 << j)){
//		//				pp_yes[i] *= p[j]; pp_no[i] *= (1 - p[j]);
//		//			}
//		//		}
//		//	}
//		//}
//
//		//for (int i = 0; i < (1 << n); ++i){
//		//	int count = 0;
//		//	for (int j = 0; j < n; ++j){
//		//		if (i&(1 << j))count++;
//		//	}
//
//		//	if (count == k){
//		//		res = max(res, calculate(i, pp_yes, pp_no));
//		//	}
//		//}
//
//		sort(all(p));
//		res = rec(0, 0, 0);
//		//res = rec(0, 0, 0);
//		//cout << "Case #" << tt + 1 << ": "<<;
//		printf("Case #%d: %.15f\n", tt + 1, res);
//	}
//	return 0;
//}

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 35 * 1000;
const double EPS = 1e-9;
typedef long long LL;

bool comp(char l, char r) {
	if (l == 'P' && r == 'R') return true;
	if (l == 'R' && r == 'S') return true;
	if (l == 'S' && r == 'P') return true;

	if (r == 'P' && l == 'R') return false;
	if (r == 'R' && l == 'S') return false;
	if (r == 'S' && l == 'P') return false;
}

bool play(string s) {
	if (s.size() == 1) return true;
	string res = "";
	for (int i = 0; i < s.size(); i += 2) {
		if (s[i] == s[i + 1]) return false;
		if (comp(s[i], s[i + 1])) {
			res.push_back(s[i]);
		}
		else {
			res.push_back(s[i + 1]);
		}
	}

	return play(res);
}
int r_t, s_t, p_t;

char v[100000];
bool dfs(char cur, int left, int right) {
	if (r_t < 0 || s_t < 0 || p_t < 0) return false;
	if (left == right) {
		v[left] = cur;
		return true;
	}
	int m = (left + right) / 2;
	if (cur == 'P') {
		r_t--;
		//p_t--;
		return dfs('P', left, m) && dfs('R', m + 1, right);
	}
	if (cur == 'R') {
		//r_t--;
		s_t--;
		return dfs('R', left, m) && dfs('S', m + 1, right);
	}
	if (cur == 'S') {
		//s_t--;
		p_t--;
		return dfs('P', left, m) && dfs('S', m + 1, right);
	}
}

void good_sort(string &t, int l, int r){
	if (l == r) return;
	int m = (l + r) >> 1;
	good_sort(t, l, m);
	good_sort(t, m+1, r);

	bool need_swap = false;
	int delt = (r-l + 1) / 2;
	for (int i = l; i <= m; ++i){
		if (t[i] > t[i + delt]){
			need_swap = true;
			break;
		}
	}

	if (need_swap){
		for (int i = l; i <= m; ++i){
			swap(t[i], t[i + delt]);
		}
	}
}

int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
#endif
	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt) {
		int n, r, p, s;

		cin >> n >> r >> p >> s;

		bool good = false;
		string ans = "Z";
		r_t = r, s_t = s, p_t = p -1;
		if (dfs('P', 0, (1 << n) - 1)) {
			string tmp = "";
			for (int i = 0; i < (1 << n); ++i) {
				tmp.push_back(v[i]);
			}
			good_sort(tmp, 0, (1 << n) - 1);
			ans = min(ans, tmp);
			good = true;
		}
		r_t = r - 1, s_t = s, p_t = p;

		if (dfs('R', 0, (1 << n) - 1)) {
			string tmp = "";
			for (int i = 0; i < (1 << n); ++i) {
				tmp.push_back(v[i]);

			}
			good_sort(tmp, 0, (1 << n)-1);
			ans = min(ans, tmp);
			good = true;
		}
		r_t = r, s_t = s-1, p_t = p;

		if (dfs('S', 0, (1 << n) - 1)) {
			string tmp = "";
			for (int i = 0; i < (1 << n); ++i) {
				tmp.push_back(v[i]);

			}
			good = true;
			good_sort(tmp, 0, (1 << n) - 1);
			ans = min(ans, tmp);
		}
		cout << "Case #" << tt + 1 << ": ";
		if (good)cout << ans << endl; else
		cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}