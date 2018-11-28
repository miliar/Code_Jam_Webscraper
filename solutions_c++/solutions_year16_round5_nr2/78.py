#include <bits/stdc++.h>
using namespace std;

int TC, N, M, a[105], ans[105];
string S, q[105];
vector<int> v[105], heads, order;
vector< vector<int> > orders;

vector<int> dfs(int x) {
	vector< vector<int> > orders;
	for (int i = 0; i < v[x].size(); i++) {
		orders.push_back(dfs(v[x][i]));
	}
	vector<int> shuf, res;
	res.push_back(x);
	for (int i = 0; i < orders.size(); i++) for (int j = 0; j < orders[i].size(); j++) shuf.push_back(i);
	random_shuffle(shuf.begin(), shuf.end());
	int idx[orders.size()];
	memset(idx, 0, sizeof(idx));
	for (int i = 0; i < shuf.size(); i++) {
		res.push_back(orders[shuf[i]][idx[shuf[i]]]);
		idx[shuf[i]]++;
	}
	return res;
}

int main() {
	srand(77);
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) scanf("%d", &a[i]);
		cin >> S;
		memset(ans, 0, sizeof(ans));
		scanf("%d", &M);
		for (int i = 0; i < M; i++) cin >> q[i];
		for (int i = 0; i < N; i++) v[i].clear();
		heads.clear();
		for (int i = 0; i < N; i++) {
			if (a[i] > 0) v[a[i] - 1].push_back(i);
			else heads.push_back(i);
		}
		for (int t = 0; t < 10000; t++) {
			random_shuffle(heads.begin(), heads.end());
			for (int i = 0; i < N; i++) random_shuffle(v[i].begin(), v[i].end());
			orders.clear();
			//printf("started dfs\n");
			for (int i = 0; i < heads.size(); i++) {
				orders.push_back(dfs(heads[i]));
			}
			//printf("finished dfs\n");
			vector<int> shuf, res;
			for (int i = 0; i < orders.size(); i++) for (int j = 0; j < orders[i].size(); j++) shuf.push_back(i);
			random_shuffle(shuf.begin(), shuf.end());
			int idx[orders.size()];
			memset(idx, 0, sizeof(idx));
			for (int i = 0; i < shuf.size(); i++) {
				res.push_back(orders[shuf[i]][idx[shuf[i]]]);
				idx[shuf[i]]++;
			}
			string s;
			for (int i = 0; i < res.size(); i++) s += S[res[i]];
			for (int i = 0; i < M; i++) ans[i] += (s.find(q[i]) != -1);
		}
		printf("Case #%d: ", tc);
		for (int i = 0; i < M; i++) printf("%.4lf ", (double)ans[i] / 10000);
		printf("\n");
		fprintf(stderr, "Solved %d\n", tc);
	}
}
