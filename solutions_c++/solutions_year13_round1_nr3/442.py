/*
 ID: ahmedfarag111
 LANG: C++
 TASK: codejama
 */

#include <iostream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
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
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define SZ(v) (int)v.size()

#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;

const int oo = (int) 1e9;
const double PI = 3.141592653589793;
const double eps = 1e-9;

#define MX 101
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int T, r, n, m, k, ks[MX], per[MX], prob[200];

#define SMALL

int main() {
	freopen("C.in", "rt", stdin);
#ifdef SMALL
	freopen("C-small-1-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	cout << "Case #1:" << endl;
	cin >> T;

	cin >> r >> n >> m >> k;

	while (r--) {
		for (int i = 0; i < k; ++i) {
			cin >> ks[i];
		}
		int ind = 0;
		for (int i = 2; i <= m; ++i) {
			for (int j = 0; j < n; ++j) {
				per[ind++] = i;
			}
		}
		double maxi = -1;
		int res[MX];
		do{
//			for (int i = 0; i < n; ++i) {
//				cout << per[i] << " ";
//			}
//			cout << endl;
			memset(prob, 0, sizeof prob);
			for (int i = 0; i < (1<<n); ++i) {
				int prod = 1;
				for (int j = 0; j < n; ++j) {
					if((i >> j) & 1)
						prod *= per[j];
				}
//				cout << prod << " -<" <<endl;
				prob[prod] ++;
			}
			double p = 1;
			for (int i = 0; i < k; ++i) {
				p *= ( double)prob[ks[i]] / ( double)(1 << n);
			}
//			cout << p << " -- " << endl;
			if(p > maxi)
			{
				maxi = p;
				for (int i = 0; i < n; ++i) {
					res[i] = per[i];
				}

			}
		}while(next_permutation(per, per + ind));

		for (int i = 0; i < n; ++i) {
			cout << res[i];

		}
		cout << endl;
	}
	return 0;
}
