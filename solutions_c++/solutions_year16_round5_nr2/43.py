#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include <vector>
#include <cstdlib>
using namespace std;

typedef long double ld;

ld fact[120];

ld comb(int n, int m) {
	return fact[n] / fact[n - m] / fact[m];
}

vector<int> pre;
vector<int> size;

int N, M;
string S;

vector<bool> ava;

int cnt;
ld msize;

ld eval() {
	ld ans = fact[cnt + 1] / (cnt + 1) / msize;
	return ans;
}

int randbig() {
	return rand() * (RAND_MAX + 1) + rand();
}

int RAND_BIG_MAX = RAND_MAX * (RAND_MAX + 1) + RAND_MAX;

int get(vector<ld> pb) {
	ld S = 0;
	for (int i = 0; i < pb.size(); ++i) {
		S += pb[i];
	}

	ld pick = (ld) 1 * randbig() / RAND_BIG_MAX * S;

	for (int i = 0; i < pb.size(); ++i) {
		if (pick <= pb[i] || i == (pb.size() - 1))
			return i;
		pick -= pb[i];
	}
}

vector<int> E[500];
string sample() {
	ava.assign(N, true);

	string ret;

	msize = 1;
	cnt = N;
	for (int i = 0; i < N; ++i) {
		msize *= size[i];
	}

	for (int i = 0; i < N; ++i) {

		vector<int> can;

		for (int i = 0; i < N; ++i) {
			if (ava[i]) {
				if (pre[i] == -1 || !ava[pre[i]])
					can.push_back(i);
			}
		}

		vector<ld> pb;
		for (int i = 0; i < can.size(); ++i) {

			ava[can[i]] = false;

			int ocnt = cnt;
			ld omsize = msize;

			cnt--;
			msize /= size[can[i]];

			pb.push_back(eval());
			ava[can[i]] = true;

			cnt = ocnt, msize = omsize;
		}

		int next = can[get(pb)];
		ava[next] = false;

		ret.push_back(S[next]);
	}

	return ret;
}

void dfs(int u) {
	size[u] = 1;
	for (vector<int>::iterator e = E[u].begin(); e != E[u].end(); ++e) {
		dfs(*e);
		size[u] += size[*e];
	}
}

int main() {
	int T;
	cin >> T;

	fact[0] = 1;
	for (int i = 1; i <= 100; ++i) {
		fact[i] = fact[i - 1] * i;
	}

	for (int nc = 1; nc <= T; ++nc) {
		cerr << nc << endl;
		cin >> N;

		pre.assign(N, 0);
		size.assign(N, 0);

		for (int i = 0; i < N; ++i) {
			E[i].clear();
		}

		for (int i = 0; i < N; ++i) {
			cin >> pre[i];
			--pre[i];

			if (pre[i] >= 0)
				E[pre[i]].push_back(i);
		}

		for (int i = 0; i < N; ++i) {
			if (pre[i] == -1)
				dfs(i);
		}

		cin >> S;

		cin >> M;
		vector<string> words(M);
		for (int i = 0; i < M; ++i) {
			cin >> words[i];
		}

		vector<int> cnt(M, 0);

		for (int i = 0; i < 3000; ++i) {
			string ret = sample();
			for (int j = 0; j < M; ++j) {
				if (ret.find(words[j]) != string::npos)
					cnt[j]++;
			}
		}

		printf("Case #%d: ", nc);
		for (int i = 0; i < M; ++i) {
			printf("%0.10lf ", 1.0 * cnt[i] / 3000);
		}
		puts("");
	}

	return 0;
}
