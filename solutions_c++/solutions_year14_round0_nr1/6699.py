#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;
typedef pair<int, int> P;
typedef long long ll;

int n;
int a[16][16], b[16][16];
int first, second;
int cnt = 1;
int res;

int main() {
	cin >> n;
	while (n--) {
		vector<int> ans;
		//input
		cin >> first; first--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> a[i][j];
			}
		}
		cin >> second; second--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> b[i][j];
			}
		}
		//solve
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[first][i] == b[second][j]) {
					ans.push_back(a[first][i]);
					break;
				}
			}
		}
		//output
		//cout << ans.size() << endl;
		if (ans.size() == 1) {
			printf("Case #%d: %d\n", cnt, ans[0]);
		} else if (ans.size() > 1) {
			printf("Case #%d: Bad magician!\n", cnt);
		} else {
			printf("Case #%d: Volunteer cheated!\n", cnt);
		}
		cnt++;
	}
	return 0;
}

