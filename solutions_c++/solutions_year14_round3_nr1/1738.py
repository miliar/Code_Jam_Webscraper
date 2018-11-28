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
#include <fstream>

using namespace std;

int solve(int P, int Q) {
	int ans = -1;
	int cnt = 0;
	while (P != 0) {
		if (Q % 2 != 0) {
			break;
		}
		Q /= 2;
		++cnt;
		if (P >= Q) {
			if (ans < 0) {
				ans = cnt;
			}
			P -= Q;
		}
	}
	if (P != 0) {
		ans = -1;
	}
	return ans;
}

int main() {
	FILE* in = fopen("A-small-attempt0.in", "r");
	ofstream out("A-small-attempt0.out");

	int T;
	fscanf(in, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		int P, Q;
		fscanf(in, "%d/%d", &P, &Q);
		int ans = solve(P, Q);
		if (ans > 0) {
			out << "Case #" << t << ": " << ans << endl;
		}
		else {
			out << "Case #" << t << ": " << "impossible" << endl;
		}
	}

	return 0;
}
