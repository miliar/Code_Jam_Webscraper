#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxN = 1111;

int inp[maxN];
int N, Ntests, ID_test;

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> Ntests;
	while (Ntests) {
		Ntests--;
		cin >> N;
		int i, maxP = 0;
		for (i = 1; i <= N; i++) {
			cin >> inp[i];
			maxP = max(maxP, inp[i]);
		}
		int res = int(1e9)+111;
		if (maxP == 0) 
			res = 0;
		else {
			for (i = 1; i <= maxP; i++) {
				int tmp = 0;
				for (int j = 1; j <= N; j++)
					tmp += (inp[j]/i)-1+bool(inp[j]%i);
				res = min(res, tmp+i);
			}
		}
		cout << "Case #" << (++ID_test) << ": " << res << endl;
	}
	return 0;
}