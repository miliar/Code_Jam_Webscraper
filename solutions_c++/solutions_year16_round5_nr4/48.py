#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		int N, L;
		cin >> N >> L;

		vector<string> G;

		for (int i = 0; i < N; ++i) {
			string w;
			cin >> w;
			G.push_back(w);
		}

		string B;
		cin >> B;

		bool imp = false;
		for (int i = 0; i < N; ++i) {
			if (G[i] == B)
				imp = true;
		}

		if (imp) {
			printf("Case #%d: IMPOSSIBLE\n", nc);
			continue;
		}

		if (L == 1) {
			printf("Case #%d: %s %s\n", nc, "0", "0?");
			continue;
		}

		string S(L - 1, '?');
		string T = string(L - 1, '1') + "0?";
		for (int i = 0; i < L - 1; ++i) {
			T += "01";
		}

		printf("Case #%d: %s %s\n", nc, S.c_str(), T.c_str());
	}
	return 0;
}
