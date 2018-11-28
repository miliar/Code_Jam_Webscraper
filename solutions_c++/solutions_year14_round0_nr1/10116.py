#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdio.h>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>
#include <cstring>

using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define sz(v) (int) v.size()
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	int counter = 1, T, ans1, ans2;
	vector<vector<int> > vec1(4);
	vector<vector<int> > vec2(4);
	cin >> T;
	while (T--) {
		cin >> ans1;
		ans1--;
		FOR(i, 0, 4) {
			vec1[i].resize(4);
			FOR(j, 0, 4) {
				cin >> vec1[i][j];
			}
		}
		cin >> ans2;
		ans2--;
		FOR(i, 0, 4) {
			vec2[i].resize(4);
			FOR(j, 0, 4) {
				cin >> vec2[i][j];
			}
		}
		int count = 0;
		int ans;
		FOR(l, 0, 4) {
			FOR(z, 0, 4) {
				if (vec1[ans1][l] == vec2[ans2][z]) {
					count++;
					ans = vec1[ans1][l];
				}
			}
		}
		cout << "Case #" << counter++ << ": ";
		if (count == 0)
			cout << "Volunteer cheated!" << endl;
		else if (count == 1)
			cout << ans << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
