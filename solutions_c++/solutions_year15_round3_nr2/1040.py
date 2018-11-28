#include <bits/stdc++.h>

using namespace std;

char Ks[10], Ls[10], cur[10];
int K, L, S;
int matches, maxMatch, ways;

void dfs(int len) {
    if (len > S) {
//    	fprintf(stderr, "%s\n", cur + 1);
		int match = 0;
	    for (int i = 1; i + L - 1 <= S; ++i) {
	        bool ok = true;
	        for (int j = 1; j <= L; ++j)
	            if (cur[i + j - 1] != Ls[j]) {
                   ok = false;
                   break;
                }
            if (ok) {
                ++match;
            }
        }
        maxMatch = max(maxMatch, match);
        matches += match;
       	ways++;
//       	fprintf(stderr, "%d %d %d\n", maxMatch, matches, ways);
    } else {
        for (int i = 1; i <= K; ++i) {
            cur[len] = Ks[i];
            dfs(len + 1);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d %d", &K, &L, &S);
        scanf("%s", Ks + 1);
        scanf("%s", Ls + 1);
		maxMatch = 0;
		matches = 0;
		ways = 0;
		dfs(1);
		double avg = double(matches) / ways;
		double answer = maxMatch - avg;
		//fprintf(stderr, "max = %d\n", maxMatch);
		//fprintf(stderr, "avg = %.8lf\n", avg);
		//fprintf(stderr, "way = %d\n", ways);
		printf("Case #%d: %.10lf\n", t, answer);
    }
}
