#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

ifstream fin("dijkstra.in");
ofstream fout("dijkstra.out");

const int mt[][4] = {{1, 2, 3, 4},
	                {2,-1, 4,-3},
					{3,-4,-1, 2},
					{4, 3,-2,-1}};

void solve() {
	int len, num;
	ll tmp;
	string s;
	fin >> len >> tmp >> s;
	num = tmp;
	len *= num;

	vector<int> v, pref, rpref;
	for (int i = 0; i < num; i++)
		for (char c : s)
			v.push_back(c - 'i' + 2);
	
	int start = -1, end = -1;
	pref.push_back(1); // identity
	rpref.push_back(1);
	for (int i = 0; i < len; i++) {
		int res = mt[abs(pref.back()) - 1][v[i] - 1];
		if (pref.back() < 0) res *= -1;
		pref.push_back(res);
//		cout << res << ' ';

		if (res == 2) {
			start = i;
			break;
		}
	}
//	cout << "\n";
	for (int i = len - 1; i >= 0; i--) {
		int a = v[i];
		int res = mt[a - 1][abs(rpref.back()) - 1];
		if (rpref.back() < 0) res *= -1;
		rpref.push_back(res);
//		cout << res << ' ';

		if (res == 4) {
			end = i;
			break;
		}
	}
//	cout << "\n\n";
	if (start == -1 || end == -1 || end - start < 2) {
		fout << "NO\n";
		return;
	}
	int jv = 1;
	for (int i = start + 1; i < end; i++) {
		int njv = mt[abs(jv) - 1][v[i] - 1];
		if (jv < 0) njv *= -1;
		jv = njv;
	}
	fout << (jv == 3 ? "YES\n" : "NO\n");
}

int main() {
	int n;
	fin >> n;
	for (int i = 0; i < n; i++) {
		fout << "Case #" << i+1 << ": ";
		solve();
	}
}

