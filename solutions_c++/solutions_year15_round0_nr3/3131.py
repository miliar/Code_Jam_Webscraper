#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

const string com[] = {"", "1", "i", "j", "k", "-1", "-i", "-j", "-k"};

int mult[9][9] = {
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 1, 2, 3, 4, 5, 6, 7, 8},
	{0, 2, 5, 4, 7, 6, 1, 8, 3},
	{0, 3, 8, 5, 2, 7, 4, 1, 6},
	{0, 4, 3, 6, 5, 8, 7, 2, 1},
	{0, 5, 6, 7, 8, 1, 2, 3, 4},
	{0, 6, 1, 8, 3, 2, 5, 4, 7},
	{0, 7, 4, 1, 6, 3, 8, 5, 2},
	{0, 8, 7, 2, 1, 4, 3, 6, 5}
};

int pow_l(int a, int n) {
	int ans = 1, d = a;
	while (n) {
		if (n & 1) {
			ans = mult[ans][d];
		}
		d = mult[d][d];
		n >>= 1;
	}
	return ans;
}

int get(const string &str) {
	int ans = 1, sz = str.size();
	for (int i = 0; i < sz; i ++) {
		ans = mult[ans][str[i] - 'i' + 2];
	}
	return ans;
}

int gao(int L, int X, const string &str) {
	//cout << com[pl] << "\n";
	string tstr = "";
	for (int i = 0; i < X; i ++) {
		tstr.append(str);
	}

	int pl = get(tstr);	
	if (pl != 5) {
		return 0;
	}

	//cout << "tstr = " << tstr << "\n";
	vector<int> mul;
	int sz = tstr.size();
	int tmp = 1;
	for (int i = 0; i < sz; i ++) {
		tmp = mult[tmp][tstr[i] - 'i' + 2];
		mul.push_back(tmp);
	}
	int p = -1, q = -1;
	for (int i = 0; i < sz; i ++) {
		if (mul[i] == 2) {
			p = i;
			break;
		}
	}
	for (int i = sz - 1; i >= 0; i --) {
		if (mul[i] == 4) {
			q = i;
			break;
		}
	}
	//cout << "p = " << p << ", q = " << q << "\n";
	if (p == -1 || q == -1) {
		return 0;
	}
	return p < q;
}

const string ans[] = {"NO", "YES"};

int main(int argc, char const *argv[]) {
	//for (int i = 1; i <= 8; i ++) {
	//	for (int j = 1; j <= 8; j ++) {
	//		cout << com[mult[i][j]] << "\t";
	//	}
	//	cout << "\n";
	//}
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++) {
		int L, X;
		string str;
		cin >> L >> X;
		cin >> str;
		int res = gao(L, X, str);
		cout << "Case #" << t << ": " << ans[res] << "\n";
	}
	return 0;
}