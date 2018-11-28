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

double D[205][205][205];
bool used[205][205][205];
vector<double> p;
int k, n;

double rec(int pos, int yes, int no){
	if (yes < 0 || no < 0) return 0;
	if (pos == k){
		if (yes == 0 && no == 0) return  1;
		return 0;
	}

	if (yes == 0 && no == 0) return 1;

	double res = 0.0;


	if (!used[pos + 1][yes - 1][no]){
		used[pos + 1][yes - 1][no] = true;
		D[pos + 1][yes - 1][no] = rec(pos + 1, yes - 1, no);
	}

	if (!used[pos + 1][yes][no-1]){
		used[pos + 1][yes][no - 1] = true;
		D[pos + 1][yes][no - 1] = rec(pos + 1, yes, no - 1);
	}

	res += (1.0 - p[pos]) * D[pos + 1][yes][no - 1];
	res += (p[pos] * D[pos + 1][yes - 1][no]);


	return res;
}

//double calculate(int mask, vector<double> &pp_yes, vector<double> &pp_no, int count = 0, int o_mask = 0, int pt = 0){
//	if (!(mask & (1 << pt))) return calculate(mask, pp_yes, pp_no, pt + 1);
//	if (if ()
//}

int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("numbers.in", "r", stdin); freopen("numbers.out", "w", stdout);
#endif
	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt){
		mems(used, 0);
		
		cin >> n >> k;
		p.resize(n);
		forn(i, 0, n)cin >> p[i];


		//vector<double> pp_yes(1 << n);
		//vector<double> pp_no(1 << n);

		//for (int i = 0; i < (1 << n); ++i){
		//	int count = 0;
		//	for (int j = 0; j < n; ++j){
		//		if (i&(1 << j))count++;
		//	}

		//	if (count * 2 == k){
		//		pp_yes[i] = 1.0;
		//		pp_no[i] = 1.0;
		//		for (int j = 0; j < n; ++j){
		//			if (i&(1 << j)){
		//				pp_yes[i] *= p[j]; pp_no[i] *= (1 - p[j]);
		//			}
		//		}
		//	}
		//}

		//for (int i = 0; i < (1 << n); ++i){
		//	int count = 0;
		//	for (int j = 0; j < n; ++j){
		//		if (i&(1 << j))count++;
		//	}

		//	if (count == k){
		//		res = max(res, calculate(i, pp_yes, pp_no));
		//	}
		//}

		sort(all(p));
		vector<double> i_p = p;

		double res = 0.0;
		for (int i = 0; i <= k; ++i){
			
				vector<double> tmp;

				for (int j = 0; j < i; ++j){
					tmp.push_back(i_p[j]);
				}

				for (int j = 0; j < (k-i); ++j){
					tmp.push_back(i_p[i_p.size() - 1 - j]);
				}

				mems(used, 0);

				p = tmp;

				res = max(res, rec(0, k / 2, k / 2));
		
		}
		
		//for (int i = 0; i < (1 << n); ++i){
		//	int count = 0;
		//	for (int j = 0; j < n; ++j){
		//		if (i&(1 << j))count++;
		//	}

		//	if (count == k){
		//		vector<double> tmp;
		//		mems(used, 0);

		//		for (int j = 0; j < n; ++j){
		//			if (i&(1 << j))tmp.push_back(i_p[j]);
		//		}

		//		p = tmp;
		//		double rr = rec(0, k / 2, k / 2);
		//			res = max(res, rr);
		//	}
		//}
		//res = rec(0, 0, 0);
		//cout << "Case #" << tt + 1 << ": "<<;
		printf("Case #%d: %.15f\n", tt + 1, res);
	}
	return 0;
}
