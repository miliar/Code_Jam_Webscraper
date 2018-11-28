#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int TC, T, n, w[1001], M, w2[1001];
int p[21][21], q[21][21], Res;
bool v[1001];
void Do()
{
	int i, j, c = 0;
	for (i = 1; i <= n; i++){
		for (j = i + 1; j <= n; j++){
			if (!q[w2[i]][w2[j]])c++;
		}
	}
	if (Res > c)Res = c;
}
void DFS2(int a, int p){
	if (a == n + 1){
		Do();
	}
	int i;
	for (i = p; i >= 1; i--){
		if (v[i])continue;
		v[i] = true;
		w2[a] = i;
		DFS2(a + 1, i - 1);
		v[i] = false;
		w2[a] = 0;
	}
}
void DFS(int a, int p){
	int i;
	for (i = p; i <= n; i++){
		if (!v[i]){
			v[i] = true;
			w2[a] = i;
			if (i == n)DFS2(a + 1, n - 1);
			else DFS(a + 1, i + 1);
			v[i] = false;
			w2[a] = 0;
		}
	}
}
int main()
{
	int i, j, t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
		Res = 999999999;
		printf("Case #%d: ", T);
		scanf("%d", &n);
		M = 0;
		for (i = 1; i <= n; i++){
			scanf("%d", &w[i]);
			w2[i] = w[i];
			v[i] = false;
		}
		sort(w2 + 1, w2 + n + 1);
		for (i = 1; i <= n; i++){
			for (j = 1; j <= n; j++){
				q[i][j] = 0;
				if (w[j] == w2[i]){
					w[j] = i;
				}
			}
		}
		for (i = 1; i <= n; i++){
			for (j = i + 1; j <= n; j++){
				q[w[i]][w[j]] = 1;
			}
		}
		DFS(1, 1);
		printf("%d\n", Res);
	}
}