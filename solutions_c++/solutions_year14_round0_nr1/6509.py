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

#define MAX 100000
#define INF 2140000000
#define MOD 1000000007

int main() {
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	int test, r1, r2, m1[4][4], m2[4][4], kk = 1;
	cin >> test;

	while (test--) {
		cin >> r1;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> m1[i][j];
			}
		}
		
		cin >> r2;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> m2[i][j];
			}
		}

		vector<int> ans;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (m1[r1-1][i] == m2[r2-1][j]) {
					ans.push_back(m1[r1-1][i]);
				}
			}
		}

		cout << "Case #" << kk++ << ": ";
		if (ans.size() == 1) {
			cout << ans[0] << endl;
		}
		else if (ans.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		}
		else {
			cout << "Bad magician!" << endl;
		}

	}
		
	
	return 0;
}