#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>

using namespace std;

const int limit = 10000 + 10;
char str[limit];

struct quaternion {
	int val;
	quaternion() {}
	quaternion(int val) : val(val) {}
	quaternion operator*(const quaternion &RHS)
	{
		const static map<pair<int,int>, int> mul = {
			{{1,1}, 1}, {{1,2}, 2},  {{1,3}, 3},  {{1,4}, 4},
			{{2,1}, 2}, {{2,2}, -1}, {{2,3}, 4},  {{2,4}, -3},
			{{3,1}, 3}, {{3,2}, -4}, {{3,3}, -1}, {{3,4}, 2},
			{{4,1}, 4}, {{4,2}, 3},  {{4,3}, -2}, {{4,4}, -1}
		};

		int res = mul.find(make_pair(abs(val), abs(RHS.val)))->second;
		if (val < 0) res = -res;
		if (RHS.val < 0) res = -res;
		return quaternion(res);
	}
};

bool can_split(int L, int X)
{
	const static map<char, int> IJK = { {'i', 2}, {'j', 3}, {'k', 4} };
	vector<quaternion> pref_left(L*X), pref_right(L*X);

	pref_left[0] = quaternion(IJK.find(str[0])->second);
	for (int i = 1; i < L*X; ++i)
		pref_left[i] = pref_left[i-1] * quaternion(IJK.find(str[i])->second);

	pref_right[L*X - 1] = quaternion(IJK.find(str[L*X - 1])->second);
	for (int i = L*X - 2; i >= 0; --i)
		pref_right[i] = quaternion(IJK.find(str[i])->second) * pref_right[i+1];

	if (pref_left[L*X - 1].val != -1) return false;

	int l = -1;
	for (int i = 0; i < L*X; ++i) {
		if (pref_left[i].val == 2) {
			l = i;
			break;
		}
	}
	int r = -1;
	for (int i = L*X - 1; i >= 0; --i) {
		if (pref_right[i].val == 4) {
			r = i;
			break;
		}
	}
	if (l == -1 || r == -1) return false;
	if (l >= r) return false;
	return true;
}

int main(int argc, char **argv)
{
	int T; cin >> T;
	for (int t = 1; t <= T; ++t) {
		int L, X; cin >> L >> X;
		for (int l = 0; l < L; ++l)
			cin >> str[l];
		for (int x = 1; x < X; ++x)
			for (int l = 0; l < L; ++l)
				str[L*x + l] = str[l];
		if (can_split(L,X))
			cout << "Case #" << t << ": YES" << endl;
		else
			cout << "Case #" << t << ": NO" << endl;
	}
	return 0;
}
