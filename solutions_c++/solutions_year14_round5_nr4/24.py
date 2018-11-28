#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;
FILE *in; FILE *out;

const int MAX = 82;
const int INF = 1000000001;

int n;
int a[MAX];
vector <int> v[MAX];
bool vis[MAX][MAX][2];
int dyn[MAX][MAX][2];
bool used[MAX][MAX];


int all(int idx) {
    int best = 0;
    for (int i = 0; i < (int)v[idx].size(); i++) {
        if (used[idx][v[idx][i]] || used[v[idx][i]][idx])
            continue;
        used[idx][v[idx][i]] = used[v[idx][i]][idx] = true;
        best = max(best, all(v[idx][i]));
        used[idx][v[idx][i]] = used[v[idx][i]][idx] = false;
    }
    return a[idx] + best;
}

int recurse(int idx1, int idx2, int who) {
    if (vis[idx1][idx2][who])
        return dyn[idx1][idx2][who];
    
    int ans = -INF;
    if (who == 0) {
        bool cont = false;
        for (int i = 0; i < (int)v[idx1].size(); i++) {
            if (used[idx1][v[idx1][i]] || used[v[idx1][i]][idx1])
                continue;

            int cur = a[v[idx1][i]];
            int sv = a[v[idx1][i]]; a[v[idx1][i]] = 0;
            used[idx1][v[idx1][i]] = used[v[idx1][i]][idx1] = true;
            cur -= recurse(v[idx1][i], idx2, !who);
            used[idx1][v[idx1][i]] = used[v[idx1][i]][idx1] = false;
            a[v[idx1][i]] = sv;
            ans = max(ans, cur);
            cont = true;
        }
        if (!cont)
            return -all(idx2);
    }
    else {
        bool cont = false;
        for (int i = 0; i < (int)v[idx2].size(); i++) {
            if (used[idx2][v[idx2][i]] || used[v[idx2][i]][idx2])
                continue;

            int cur = a[v[idx2][i]];
            int sv = a[v[idx2][i]]; a[v[idx2][i]] = 0;
            used[idx2][v[idx2][i]] = used[v[idx2][i]][idx2] = true;
            cur -= recurse(idx1, v[idx2][i], !who);
            used[idx2][v[idx2][i]] = used[v[idx2][i]][idx2] = false;
            a[v[idx2][i]] = sv;
            ans = max(ans, cur);
            cont = true;
        }
        if (!cont)
            return -all(idx1);
    }
    
    vis[idx1][idx2][who] = true;
    return dyn[idx1][idx2][who] = ans;
}

void solve(int testNum) {
    for (int i = 0; i < MAX; i++)
        v[i].clear();

    fscanf(in, "%d", &n);
    for (int i = 0; i < n; i++)
        fscanf(in, "%d", &a[i]);
    for (int i = 0; i < n - 1; i++) {
        int o;
        fscanf(in, "%d", &o); o--;
        v[i].push_back(o);
        v[o].push_back(i);
    }
    
    int ans = -INF;
    for (int s1 = 0; s1 < n; s1++) {
        int worst = INF;
        for (int s2 = 0; s2 < n; s2++) {
            memset(vis, 0, sizeof(vis));

            int cur = a[s1];
            int sv1 = a[s1]; a[s1] = 0;
            cur -= a[s2];
            int sv2 = a[s2]; a[s2] = 0;
            cur += recurse(s1, s2, 0);
            a[s2] = sv2, a[s1] = sv1;
            worst = min(worst, cur);
        }
        ans = max(ans, worst);
    }
    fprintf(out, "%d\n", ans);
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("Willow.in", "rt");
	out = fopen("Willow.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solve(test);
	}
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
