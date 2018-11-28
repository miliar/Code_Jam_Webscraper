#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

typedef long long ll;
typedef long double ld;

int arr[110][110];
vector<map<int, int> > rows, cols;

int cnt = 0;
void update(int i, int j) {
	if (arr[i][j] == -1)
		return;
	cnt++;
	rows[i][arr[i][j]]--;
	if (rows[i][arr[i][j]] == 0)
		rows[i].erase(arr[i][j]);
	cols[j][arr[i][j]]--;
	if (cols[j][arr[i][j]] == 0)
		cols[j].erase(arr[i][j]);
	arr[i][j] = -1;
}

int main() {
#ifndef ONLINE_JUDGE
//	freopen("Qual/B-small-attempt0.in", "rt", stdin);
//	freopen("B.out","wt",stdout);
	freopen("Qual/B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif
	int tt;
	cin >> tt;
	for (int ii = 0; ii < tt; ++ii) {
		cout << "Case #" << ii + 1 << ": ";
		int r, c;
		cnt = 0;
		cin >> r >> c;
		rows.clear();
		rows.resize(r);
		cols.clear();
		cols.resize(c);
		for (int i = 0; i < r; ++i) {
			for (int j = 0; j < c; ++j) {
				cin >> arr[i][j];
				rows[i][arr[i][j]]++;
				cols[j][arr[i][j]]++;
			}
		}
		bool valid = 0;
		int v = 1;
		while (v < 200) {
			for (int i = 0; i < r; ++i) {
				if (rows[i].size() == 1 && rows[i].begin()->first == v) {
					for (int j = 0; j < c; ++j) {
						update(i, j);
					}
				}
			}
			for (int j = 0; j < c; ++j) {
				if (cols[j].size() == 1 && cols[j].begin()->first == v) {
					for (int i = 0; i < r; ++i) {
						update(i, j);
					}
				}
			}
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					if (arr[i][j] == v)
						goto invalid;
				}
			}
			++v;
		}

		cout << "YES" << endl;
		continue;

		invalid: cout << "NO" << endl;
	}
	return 0;
}
