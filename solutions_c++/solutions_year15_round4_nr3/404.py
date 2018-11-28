#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#define pb push_back
#define mp make_pair
#define ll long long
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
char line[555555];
char word[55];
vector< vector< string > > lines;
unordered_map< string, int > M;
int main() {
	int T;
	scanf("%d", &T);
	for(int testc = 1; testc <= T; testc++) {
		int n;
		scanf("%d\n", &n);
		lines.clear();
		M.clear();
		REP(i, n) {
			char x;
			vector< string > words;
			int w = 0;
			while(scanf("%c", &x) == 1) {
				if(x == '\n') {
					word[w] = '\0';
					words.pb(word);
					break;
				}
				if(x == ' ') {
					word[w] = '\0';
					words.pb(word);
					w = 0;
					continue;
				}
				word[w++] = x;
			}
			lines.pb(words);
		}
		REP(i, lines[0].size())
			M[lines[0][i]] |= 1;
		REP(i, lines[1].size())
			M[lines[1][i]] |= 2;
		int ans = 1<<30;
		int k = 0;
		for(auto x : M) {
			if(x.second == 3)
				k++;
		}
		REP(j, 1<<(n-2)) {
			int cans = k;
			unordered_map< string, int > MM;
			REP(i, n-2) {
				int k = i+2;
				REP(x, lines[k].size()) {
					if(j&(1<<i))
						MM[lines[k][x]] |= 1;
					else
						MM[lines[k][x]] |= 2;
				}
			}
			for(pair<string, int> x : MM) {
				int y = M[x.first];
				if(y == 3)
					continue;
				int q = y|x.second;
				if(q == 3)
					cans++;
			}
			ans = min(cans, ans);
		}
		printf("Case #%d: %d\n", testc, ans);
	}
	return 0;
}
