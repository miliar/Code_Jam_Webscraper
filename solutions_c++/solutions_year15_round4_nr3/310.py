#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
using namespace std;

int a[99][1005];
int n[99], e[99];

int main() {
	int testCaseNum;
	cin >> testCaseNum;
	for (int testCase = 1; testCase <= testCaseNum; ++testCase) {
		cerr << testCase << "\n";
		int N;
		cin >> N;
		string line;
		getline(cin, line);
		memset(n, 0, sizeof(n));
		int idcnt = 0;
		map<string,int> hash;
		for (int i = 0; i < N; ++i) {
			getline(cin, line);
			line += " ";
			while (line.size()) {
				int p = line.find(" ");
				string word = line.substr(0, p);
				int wordid;
				if (hash.find(word) != hash.end()) {
					wordid = hash[word];
				} else {
					wordid = hash[word] = idcnt++;
				}
				a[i][n[i]++] = wordid;
				line = line.substr(p + 1);
			}
		}
		
		int ans = 1 << 30;
		e[0] = 0;
		e[1] = 1;
		int **lang = new int*[2];
		lang[0] = new int[idcnt];
		lang[1] = new int[idcnt];
		for (int x = 0; x < 1 << (N - 2); ++x) {
			memset(lang[0], 0, sizeof(int) * idcnt);
			memset(lang[1], 0, sizeof(int) * idcnt);
			for (int xx = x, i = N - 1; i > 1; --i) {
				e[i] = xx % 2;
				xx /= 2;
			}
			int now = 0;
			for (int i = 0; i < N; ++i)
				for (int j = 0; j < n[i]; ++j) {
					lang[e[i]][a[i][j]]++;
					//printf("%d %d %d\n", e[i], a[i][j], lang[e[i]][a[i][j]]);
					if (lang[e[i]][a[i][j]] != 1) continue;
					if (lang[e[i] ^ 1][a[i][j]] > 0) ++now;
				}
			ans = min(ans, now);
		}
		printf("Case #%d: %d\n", testCase, ans);
	}
	return 0;
}