#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

enum STATE{ONE = 0, I, J, K, nONE, nI, nJ, nK};

const int MAXN = 10000 + 10;

STATE state[MAXN];

/*
0 - 3, 1, i, j, k
4 - 7, -1, -i, -j, -k
*/

const STATE transfer[8][3] = {
	{I, J, K},
	{nONE, K, nJ},
	{nK, nONE, I},
	{J, nI, nONE},
	{nI, nJ, nK},
	{ONE, nK, J},
	{K, ONE, nI},
	{nJ, I, ONE}
};

STATE get(char c) {
	return c == 'i' ? ONE : (c == 'j' ? I : J);
}

int main () {
	int cases;
	cin >> cases;

	for (int tc = 1; tc <= cases; tc ++) {
		int L, X;
		string single, str = "";
		cin >> L >> X >> single;

		for (int i = 0; i < X; i ++) {
			str += single;
		}

		state[0] = ONE;
		for (int i = 0; i < str.size(); i ++) {
			STATE nxt = get(str[i]);
			state[i + 1] = transfer[state[i]][nxt];
		}

		int S = L * X;

		int ret = -1;

		for (int i = 0; i <= S; i ++) {
			if (state[i] == I && ret == -1) ret = 0;
			if (state[i] == K && ret == 0 ) ret = 1;
		}

		bool ok = (ret == 1 && state[S] == nONE);

		cout << "Case #" << tc << ": " << (ok ? "YES" : "NO") << endl;
	}
}