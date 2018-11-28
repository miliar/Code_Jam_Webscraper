#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
int ri() { int a; scanf( "%d", &a ); return a; }
char sbuf[100005];
string rs() { scanf( "%s", sbuf ); return sbuf; }

/*-------------------------------------------------------*/



int main() {
	freopen("C:\\Users\\Administrator\\Desktop\\A-small-attempt0.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\output.txt","wt",stdout);

	int T = ri();
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		int N = ri();
		vector<pair<char, int>> words[N];
		for (int i = 0; i < N; ++i) {
			string s = rs();
			int count = 0;
			char ch = ' ';
			for (int j = 0; j < s.size(); ++j) {
				if (s[j] == ch) {
					count++;
				} else {
					if (j != 0)
						words[i].push_back(make_pair(ch, count));
					ch = s[j];
					count = 1;
				}
			}
			words[i].push_back(make_pair(ch, count));
		}
		int M = words[0].size();
		int res = 0;
		bool fail = false;
		for (int j = 1; j < N; ++j) {
			if (words[j].size() != M) {
				fail = true;
				break;
			}
		}
		for (int i = 0; i < M; ++i) {
			char ch = words[0][i].first;
			int sum = 0;
			for (int j = 0; j < N; ++j) {
				if (ch != words[j][i].first) {
					fail = true;
					break;
				}
				sum += words[j][i].second;
			}
			if (fail) break;
			else {
				int mid = sum / N;
				int ssum = 0;
				for (int j = 0; j < N; ++j) {
					ssum += abs(words[j][i].second - mid);
				}
				mid = sum / N + 1;
				int ssum2 = 0;
				for (int j = 0; j < N; ++j) {
					ssum2 += abs(words[j][i].second - mid);
				}
				res += min(ssum, ssum2);
			}
		}
		if (fail) printf("Fegla Won\n");
		else printf("%d\n", res);
	}
	return 0;
}
