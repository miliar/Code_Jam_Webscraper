#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue>
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 

using namespace std; 

typedef long long ll; 
typedef pair<int, int> pii;

#define INF 1000000000
#define pb push_back 
#define itr iterator 
#define sz size() 
#define mp make_pair

long long s[1100000];
long long m[1100000];
int n, d, s0, A, C, R;

vector<int> adj[1100000];
int vals[2100000];

void gen(long long* S, int s0, int a, int c, int r) {
	S[0] = s0;
	for (int i = 1; i < n; i++) {
		S[i] = (S[i-1] * a + c) % r;
	}
}

void dfs(int v, int small, int big) {
	small = min(small, (int)s[v]);
	big = max(big, (int)s[v]);

	int minimal = max(0, big - d);
	int maximal = small;

	if (maximal >= minimal) {
		//fprintf(stderr, "%d %d\n", maximal, minimal);
		vals[minimal]++;
		vals[maximal+1]--;
	}

	for (int k : adj[v]) {
		dfs(k, small, big);
	}
}

int t, teste;
int main() {
	for (scanf("%d", &t); t; t--) {
		printf("Case #%d: ", ++teste);
		fprintf(stderr, "%d\n", teste);

		scanf("%d %d", &n, &d);
		memset(vals,0,sizeof(vals));
		for (int i = 0; i < n; i++) adj[i].clear();
		
		scanf("%d %d %d %d", &s0, &A, &C, &R);
		gen(s, s0, A, C, R);
		scanf("%d %d %d %d", &s0, &A, &C, &R);
		gen(m, s0, A, C, R);

		for (int i = 1; i < n; i++) {
			m[i] = m[i] % i;
			adj[m[i]].push_back(i);
		}

		fprintf(stderr, "hi\n" );

		dfs(0, s[0], s[0]);

		fprintf(stderr, "hi\n" );

		int ans = 0;
		int tot = 0;
		for (int mm = 0; mm <= 1000000; mm++) {
			tot += vals[mm];
			ans = max(ans, tot);
		}

		printf("%d\n", ans);
	}
}