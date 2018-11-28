#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

const int MAXN = 105;

int mem[MAXN][MAXN], row[MAXN], col[MAXN], T, N, M;

int main() {
	scanf("%d", &T);
	for(int t = 1 ; t <= T ; t++) {
		scanf("%d %d", &N, &M);
		for(int i = 0 ; i < N ; i++)
			for(int j = 0 ; j < M ; j++)
				scanf("%d", &mem[i][j]);
		for(int i = 0 ; i < N ; i++) {
			row[i] = mem[i][0];
			for(int j = 0 ; j < M ; j++)
				row[i] = max(row[i], mem[i][j]);
		}
		for(int j = 0 ; j < M ; j++) {
			col[j] = mem[0][j];
			for(int i = 0 ; i < N ; i++)
				col[j] = max(col[j], mem[i][j]);
		}
		int ans = 1;
		for(int i = 0 ; i < N ; i++)
			for(int j = 0 ; j < M ; j++)
				if (mem[i][j] != min(col[j], row[i]))
					ans = 0;
		if (ans)
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
}
