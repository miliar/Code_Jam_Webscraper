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

int T;
double C, F, X;
double ans;

int main() {
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> C >> F >> X;
		ans = X/2.0;
		double d = 2.0, s = 0.0;
		for (int i=0; ; i++) {
			s += C/d;
			if (ans > s + X/(d+F)) {
				ans = s + X/(d+F);
			} else {
				break;
			}
			d += F;
		}
		printf("Case #%d: %.7lf\n", t+1, ans);
	}
	return 0;
}

