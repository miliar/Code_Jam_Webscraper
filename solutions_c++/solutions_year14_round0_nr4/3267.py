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
	for (int t = 0; t < tc; t++) {
		int n;
		cin >> n;
		vector<double> v1(n), v2(n);
		for(int i = 0; i < n; i++) cin >> v1[i];
		for(int i = 0; i < n; i++) cin >> v2[i];
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int war = n;
		int p1 = n - 1, p2 = n - 1;
		while (p1 >= 0) {
			if (v2[p2] > v1[p1]) {
				war--;
				p2--;
				p1--;
			} else {
				p1--;
			}
		}
		p1 = 0;
		p2 = 0;
		int bg = n - 1;
		int dw = 0;
		for (int i = 0; i < n; i++) {
			if (v1[p1] < v2[p2]) {
				p1++;
			} else {
				p1++;
				p2++;
				dw++;
			}
		}
		printf("Case #%d: %d %d\n", t + 1, dw, war);
	}
}


