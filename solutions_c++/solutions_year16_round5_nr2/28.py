#include<cmath>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 105;

const int BAR = 20000;

int n;

vector<int> ch[N];

int size[N];

long double cnt[N], ccnt[N];

const int M = 5;

string buf[M];

long double fac[N];

char map[N];

void init() {
	fac[0] = 0;
	for (int i = 1; i < N; ++i) {
		fac[i] = fac[i - 1] + log(i);
	}
}

long double binom(int n, int m) {
	return fac[n] - fac[m] - fac[n - m];
}

void calc(int u) {
	size[u] = 0;
	ccnt[u] = 0;
	for (int i = 0; i < (int)ch[u].size(); ++i) {
		int v = ch[u][i];
		calc(v);
		size[u] += size[v];
		ccnt[u] = ccnt[u] + cnt[v] + binom(size[u], size[v]);
	}
	++size[u];
	cnt[u] = ccnt[u];
}

string randomSample() {
	int top = 0;
	char buf[N];
	vector<int> cur;
	cur.push_back(0);
	while (cur.size()) {
		long double sum = 0;
		int ss = 0;
		for (int i = 0; i < (int)cur.size(); ++i) {
			int u = cur[i];
			ss += size[u];
			sum = sum + cnt[u] + binom(ss, size[u]);
		}
		long double p = (long double)rand() / RAND_MAX;
		for (int i = 0; i < (int)cur.size(); ++i) {
			int u = cur[i];
			long double q = exp(binom(ss - 1, size[u] - 1) - binom(ss, size[u]));
			if (p > q) {
				p -= q;
			} else {
				p = 0;
				swap(cur[i], cur[cur.size() - 1]);
				break;
			}
		}
		int u = cur.back();
		cur.pop_back();
		for (int i = 0; i < (int)ch[u].size(); ++i) {
			cur.push_back(ch[u][i]);
		}
		if (u) {
			buf[top++] = map[u];
		}
	}
	buf[top] = '\0';
	return buf;
}

int main() {
	init();
	int T;
	scanf("%d", &T);
	while (T--) {
		static int id = 0;
		printf("Case #%d: ", ++id);
		cerr << id << endl;
		scanf("%d", &n);
		for (int i = 0; i <= n; ++i) {
			ch[i].clear();
		}
		for (int i = 1; i <= n; ++i) {
			int fa;
			scanf("%d", &fa);
			ch[fa].push_back(i);
		}
		scanf("%s", map + 1);
		calc(0);
		int m;
		scanf("%d", &m);
		for (int i = 0; i < m; ++i) {
			cin >> buf[i];
			cnt[i] = 0;
		}
		for (int i = 0; i < BAR; ++i) {
			string s = randomSample();
			for (int j = 0; j < m; ++j) {
				if (s.find(buf[j]) != string::npos) {
					++cnt[j];
				}
			}
		}
		for (int i = 0; i < m; ++i) {
			printf("%.4f%c", (double)cnt[i] / BAR, i == m - 1 ? '\n' : ' ');
		}
	}
	return 0;
}
