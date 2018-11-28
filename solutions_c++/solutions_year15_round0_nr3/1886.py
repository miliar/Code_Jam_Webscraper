#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

const int MAX_N = 1000 + 10;
int a[MAX_N], n;
string S;

int sign[4][4] = { { 1, 1, 1, 1 }, { 1, -1, 1, -1 }, { 1, -1, -1, 1 }, { 1, 1,
		-1, -1 } };
int mult[4][4] = { { 0, 1, 2, 3 }, { 1, 0, 3, 2 }, { 2, 3, 0, 1 },
		{ 3, 2, 1, 0 } };

struct Quaterion {
	int sign; //1,-1
	int idx;
	Quaterion(int sign, int idx) :
			sign(sign), idx(idx) {
	}

	bool operator==(const Quaterion&o) const {
		return sign == o.sign && idx == o.idx;
	}

	bool operator!=(const Quaterion&o) const {
		return sign != o.sign || idx != o.idx;
	}
};

Quaterion operator*(Quaterion a, Quaterion b) {
	return Quaterion(a.sign * b.sign * sign[a.idx][b.idx], mult[a.idx][b.idx]);
}

const Quaterion I(1, 1), J(1, 2), K(1, 3);

int main() {
	int T;
	cin >> T;
	for (int it = 1; it <= T; ++it) {
		int L, X;
		cin >> L >> X;
		cin >> S;
		if (X >= 16) {
			int over = X - 16;
			X -= over / 16 * 16;
		}
		string T = S;
		for (int j = 0; j < X - 1; ++j) {
			S += T;
		}

		vector<Quaterion> qs;
		for (int i = 0; i < S.size(); ++i) {
			qs.push_back(Quaterion(1, string("ijk").find(S[i]) + 1));
		}

		Quaterion ret(1, 0);
		for (int i = 0; i < qs.size(); ++i) {
			ret = ret * qs[i];
		}

		Quaterion need = I * J * K;

		bool ok = false;
		Quaterion cur(1, 0);
		int pre = -1;
		int suf = -1;

		if (ret != need) {
			goto end;
		}

		for (int i = 0; i < qs.size(); ++i) {
			cur = cur * qs[i];
			if (cur == I) {
				pre = i;
				break;
			}
		}

		cur = Quaterion(1, 0);
		for (int i = qs.size() - 1; i >= 0; --i) {
			cur = qs[i] * cur;
			if (cur == K) {
				suf = i;
				break;
			}
		}
		if (pre != -1 && suf != -1 && pre + 1 < suf) {
			ok = true;
		}

		end: {
			printf("Case #%d: %s\n", it, ok ? "YES" : "NO");
		}
	}
}
