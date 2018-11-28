#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef map<int, int> mii;

int T;
int L, X;
const int MAX_L = 10000;
string str;
int val[MAX_L];
int sig[MAX_L];

int valtable[4][4] = {
	0, 1, 2, 3,
	1, 0, 3, 2,
	2, 3, 0, 1,
	3, 2, 1, 0
};
int sigtable[4][4] = {
	1, 1, 1, 1,
	1, -1, 1, -1,
	1, -1, -1, 1,
	1, 1, -1, -1
};

void solve()
{
	memset(val, 0, sizeof(val));
	memset(sig, 0, sizeof(sig));
	int tmp = 0;
	int sign = 1;
	for (int x = 0; x < X; ++x) {
		for (int l = 0; l < L; ++l) {
			int v = str[l] - 'i' + 1;
			sign = sign * sigtable[tmp][v];
			tmp = valtable[tmp][v];
			val[L * x + l] = tmp;
			sig[L * x + l] = sign;
			//cout << tmp << "," << sign << " ";
		}
	}

	int LX = L * X;
	if (val[LX-1] != 0 || sig[LX-1] != -1) {
		printf("NO");
		return;
	}

	for (int i = 0; i < LX - 2; ++i) {
		for (int j = i + 1; j < LX - 1; ++j) {
			if (val[i] == 1 && sig[i] == 1 && val[j] == 3 && sig[j] == 1) {
				printf("YES");
				return;
			}
		}
	}
	printf("NO");
	return;
}

int main()
{
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> L >> X;
		cin >> str;
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
	return 0;
}