#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

int main() {
	int tc;
	cin >> tc;
	for(int t = 0; t < tc; t++) {
		int n1, n2;
		vi v1(16), v2(16);
		cin >> n1;
		for(int i = 0; i < 16; i++) cin >> v1[i];
		cin >> n2;
		for(int i = 0; i < 16; i++) cin >> v2[i];
		set<int> s;
		for (int i = (n1 - 1) * 4; i < n1 * 4; i++) s.insert(v1[i]);
		int zahl = -1;
		for (int i = (n2 - 1) * 4; i < n2 * 4; i++) {
			if (s.find(v2[i]) != s.end()) {
				if (zahl == -1) {
					zahl = v2[i];
				} else {
					zahl = -2;
					break;
				}
			}
		}
		if (zahl == -1) {
			printf("Case #%d: Volunteer cheated!\n", t + 1);
		} else if (zahl == -2) {
			printf("Case #%d: Bad magician!\n", t + 1);
		} else {
			printf("Case #%d: %d\n", t + 1, zahl);
		}
	}
}


