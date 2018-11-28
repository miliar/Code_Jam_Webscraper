//author: whd

#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <queue>
#include <set>
#include <map>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;
typedef long long big;

typedef pair<int, int> pii;

int n, m;
int ps[] = { 0, 0, 3, 2, 5, 2, 7, 2, 3, 2, 7 };
typedef map<vector<int>, vector<string> > maptype;
maptype dic1, dic2;
int get_remainder(const string& num, int base, bool first) {
	int res = 0;
	for (int i = 0; i < num.size(); i++) {
		res *= base;
		res += num[i] - '0';
		res %= ps[base];
	}
	if (first) {
		for (int i = 0; i < num.size(); i++) {
			res *= base;
			res %= ps[base];
		}
	}
//	cerr << num << " " << base << " " << res << endl;
	return res;
}

void dfs(maptype &dic, bool first) {
	int nn = n / 2;
	for (int st = 0; st < (1 << nn); st++) {
		string num;
		for (int i = 0; i < nn; i++)
			num += ('0' + (st >> i & 1));
		if (first && num[0] != '1')
			continue;
		if (!first && num.back() != '1')
			continue;
		vector<int> remainders;
		for (int base = 2; base <= 10; base++)
			remainders.push_back(get_remainder(num, base, first));
		dic[remainders].push_back(num);
	}
}

vector<int> opposite(const vector<int>& rem) {
	vector<int> res(rem.size());
	for (int i = 0; i < rem.size(); i++)
		res[i] = (ps[i + 2] - rem[i]) % ps[i + 2];
	return res;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cas, cass;
	scanf("%d", &cas);
	vector<string> ans;
	for (cass = 1; cass <= cas; cass++) {
		printf("Case #%d:\n", cass);
		scanf("%d%d", &n, &m);
		dfs(dic1, true);
		dfs(dic2, false);
		int sum = 0;
		for (auto &kvpair : dic1) {
			auto &rem1 = kvpair.first;
			auto rem2 = opposite(rem1);
			if (ans.size() < m && dic2.count(rem2)) {
				const auto &kvpair2 = dic2.find(rem2);
				for (auto &str1 : kvpair.second) {
					for (auto &str2 : kvpair2->second) {
						if (ans.size() < m)
							ans.push_back(str1 + str2);
					}
				}
			}
		}
		for (int i = 0; i < ans.size(); i++) {
//			for (int j = 2; j <= 10; j++)
//				printf("%d", get_remainder(ans[i], j, false));
			printf("%s", ans[i].c_str());
			for (int j = 2; j <= 10; j++)
				printf(" %d", ps[j]);
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
}

