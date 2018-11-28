#include <iostream>
#include <iomanip>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define pb push_back
#define mp make_pair

vector<int> codes;
bool g[8][8];

void tostradd(int a, string &s) {
	string tmp = "";
	while(a != 0) {
		tmp += (char)('0' + a % 10);
		a /= 10;
	}

	for(int i = tmp.size() - 1; i >= 0; i--) {
		s += tmp[i];
	}
}

void solve(int n, int m) {
	codes.resize(n);
	for(int i = 0 ; i < 8; i++) for(int j = 0 ; j < 8; j++) g[i][j] = false;

	for(int i = 0; i < n; i++) {
		cin >>codes[i];
	}

	for(int i = 0; i < m; i++) {
		int a, b;
		cin >>a >>b;
		a--, b--;
		g[a][b] = true;
		g[b][a] = true;
	}

	vector<int> order;
	for(int i = 0; i < n; i++) order.pb(i);

	string ans = ""; for(int i = 0; i < n; i++) ans += "99999";

	do {
		string cur = "";
		bool ok = true;
		vector<int> back; for(int i = 0; i < n; i++) back.pb(-1);
		back[1] = 0;

		for(int i = 0; i < n; i++) {
			int v = order[i];
			tostradd(codes[v], cur);

			if(i == 0) continue;

			int j = i - 1;
			while(j >= 0 && !g[order[j]][v]) j = back[j];
			if(j < 0) {
				ok = false;
				break;
			}

			back[i] = j;
		}

		if(ok && cur < ans)
			ans = cur;
	} while(std::next_permutation(order.begin(), order.end()));

	cout <<ans <<endl;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;

	cin >>T;

	for(int t = 0; t < T; t++) {
		int n, m;
		cin >>n >>m; 
		cout <<"Case #" <<t + 1 <<": ";
		solve(n, m);
	}
	return 0;
}