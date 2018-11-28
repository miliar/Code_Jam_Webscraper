#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <assert.h>
#include <queue>

using namespace std;

string doit(int P, int R, int S)
{
	if (P == 0 && R == 0 && S == 0) {
		return "";
	} else if (P == 0 && R == 1 && S == 0) {
		return "R";
	} else if (P == 0 && R == 0 && S == 1) {
		return "S";
	} else if (P == 1 && R == 0 && S == 0) {
		return "P";
	} else if (P == 0 && R == 1 && S == 1) {
		return "RS";
	} else if (P == 1 && R == 0 && S == 1) {
		return "PS";
	} else if (P == 1 && R == 1 && S == 0) {
		return "PR";
	} else {
		int pBig = (P + 1) / 2;
		int pSmall = P / 2;
		int rBig = (R + 1) / 2;
		int rSmall = R / 2;
		int sBig = (S + 1) / 2;
		int sSmall = S / 2;
		if (P % 2 == 0) {
			return doit(P / 2, rBig, sSmall) + doit(P / 2, rSmall, sBig);
		} else if (R % 2 == 0) {
			return doit(pBig, R / 2, sSmall) + doit(pSmall, R / 2, sBig);
		} else if (S % 2 == 0) {
			return doit(pBig, rSmall, S / 2) + doit(pSmall, rBig, S / 2);
		} else {
			return "Error1";
		}
	}
}

void test()
{
	int N, R, P, S;
	cin >> N >> R >> P >> S;

	vector<int> D(3, 0);
	D[0] = P;
	D[1] = R;
	D[2] = S;

	int minCount = min(R, min(P, S));
	int maxCount = max(R, max(P, S));
	if (maxCount - minCount != 1) {
		cout << "IMPOSSIBLE";
		return;
	}

	string res = doit(P, R, S);
	cout << res;
}

int main()
{
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
