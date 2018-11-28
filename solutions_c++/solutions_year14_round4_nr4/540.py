#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

const int N = 10;
const int Z = 26;

string s[N];
int n, m;
set<int> choose[N];
int ans, num;
string ts[N];
int tn;

struct node {
	int son[30];
} nodes[N * 20];

int tree() {
	int numnode = 1;
	for (int i = 0; i < Z; ++i) nodes[0].son[i] = -1;
	for (int i = 0; i < tn; ++i) {
		int now = 0;
		string str = ts[i];
		for (int j = 0; j < str.length(); ++j) {
			int sonnum = str[j] - 'A';
			if (nodes[now].son[sonnum] < 0) {
				nodes[now].son[sonnum] = numnode;
				for (int t = 0; t < Z; ++t) nodes[numnode].son[t] = -1;
				++numnode;
			}
			now = nodes[now].son[sonnum];
		}
	}
	return numnode;
}

void calc() {
	int sum = 0;
	for (int i = 0; i < m; ++i) {
		tn = 0;
		for (set<int>::iterator iter = choose[i].begin(); iter != choose[i].end(); ++iter) {
			ts[tn++] = s[*iter];
		}
		//for (int j = 0; j < tn; ++j) cout << ts[j] << ' ';
		//cout << endl;
		sum += tree();
	}
	//cout << sum << endl;
	if (sum > ans) {
		ans = sum;
		num = 1;
	} else if (sum == ans) ++num;
}

void dfs(int k) {
	if (k == n) {
		for (int i = 0; i < m; ++i) {
			if (choose[i].empty()) return;
		}
		calc();
		return;
	}
	for (int i = 0; i < m; ++i) {
		choose[i].insert(k);
		dfs(k + 1);
		choose[i].erase(k);
	}
}

int main() {
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		cin >> n >> m;
		for (int i = 0; i < n; ++i) cin >> s[i];
		for (int i = 0; i < m; ++i) choose[i].clear();
		choose[0].insert(0);
		ans = num = 0;
		dfs(1);
		cout << "Case #" << test << ": " << ans << ' ' << num * m << endl;
	}
	return 0;
}