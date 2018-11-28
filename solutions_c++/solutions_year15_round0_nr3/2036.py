#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))


enum {
	QUAT_1 = 0,
	QUAT_I = 1,
	QUAT_J = 2,
	QUAT_K = 3,

	QUAT_NEG_1 = 4,
	QUAT_NEG_I = 5,
	QUAT_NEG_J = 6,
	QUAT_NEG_K = 7
};

const int QUAT_MULTI_TABLE[][4] = {
	{QUAT_1, QUAT_I, QUAT_J, QUAT_K},
	{QUAT_I, QUAT_NEG_1, QUAT_K, QUAT_NEG_J},
	{QUAT_J, QUAT_NEG_K, QUAT_NEG_1, QUAT_I},
	{QUAT_K, QUAT_J, QUAT_NEG_I, QUAT_NEG_1}
};

int calc(int lhs, int rhs)
{
	bool neg = false;

	if(lhs > QUAT_K) {
		neg = !neg;
		lhs -= 4;
	}
	if(rhs > QUAT_K) {
		neg = !neg;
		rhs -= 4;
	}

	lhs = QUAT_MULTI_TABLE[lhs][rhs];
	if(neg) {
		if(lhs < QUAT_NEG_1)
			lhs += 4;
		else
			lhs -= 4;
	}

	return lhs;
}

bool solve()
{
	int T, X;
	string ijk_str;

	cin >> T >> X;
	cin >> ijk_str;

	string tmp = ijk_str;
	rep(i, X - 1)
		ijk_str += tmp;

	vector<int> ijk_data(ijk_str.size());
	vector<vector<int>> memo(ijk_str.size(), vector<int>(ijk_str.size() + 2));
	rep(i, ijk_str.size()) {
		switch(ijk_str[i]) {
			case 'i': ijk_data[i] = QUAT_I; break;
			case 'j': ijk_data[i] = QUAT_J; break;
			case 'k': ijk_data[i] = QUAT_K; break;
			default: throw 0;
		}
	}
	rep(i, ijk_data.size()) {
		int tmp = ijk_data[i];
		memo[i][i+1] = tmp;
		For(j, i + 2, ijk_data.size() + 1) {
			tmp = calc(tmp, ijk_data[j-1]);
			memo[i][j] = tmp;
		}
	}
	For(i, 1, ijk_data.size()) {
		if(memo[0][i] != QUAT_I)
			continue;
		For(j, i + 1,ijk_data.size()) {
			if(memo[i][j] != QUAT_J)
				continue;
			if(memo[j][ijk_data.size()] == QUAT_K) {
				return true;
			}
		}
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << (solve() ? "YES" : "NO") << endl;
}
