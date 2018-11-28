#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <utility>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <bitset>
#include <time.h>
#include <iterator>

using namespace std;

int K, L, S, go[10], Max = 0;
string a, b;
double sum, cnt;

void gen(int t = 0) {
	if (t == S) {
		string res = "";
		for (int i = 0; i < S; i++)
			res += a[go[i]];
		int temp = 0;
		for (int i = 0; i < S; i++) {
			if (i + L - 1 < S) {
				bool ok = 1;
				for (int j = i; j <= i + L - 1; j++) {
					if (res[j] != b[j - i])
						ok = 0;
				}
				if (ok)
					sum++, temp++;
			}
		}
		Max = max(Max, temp);
		cnt++;
	}
	else {
		for (int c = 0; c < K; c++) {
			go[t] = c;
			gen(t + 1);
		}
	}
}

int main() {
	freopen("B-small-attempt0 (1).IN", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> K >> L >> S;
		cin >> a >> b;
		vector<bool> used(30, 0);
		for (int i = 0; i < (int)a.size(); i++)
			used[a[i] - 'A'] = 1;
		bool ok = 1;
		for (int i = 0; i < (int)b.size(); i++) {
			if (!used[b[i] - 'A'])
				ok = 0;
		}
		if (!ok) {
			cout << "Case #" << t << ": " << 0 << endl;
		}
		else {
			cnt = sum = Max = 0;
			gen();
			cout << fixed << setprecision(15) << "Case #" << t << ": " << Max - sum / cnt << endl;
		}
	}
	return 0;
}