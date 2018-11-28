#include<stdio.h>
#include<algorithm>
#include<map>
#include<string>
using namespace std;
map<string, int>Map;
int TT, TC, n, w[21][1010], C[21], cnt, Res;
int D[5000][2];
char p[30100], pp[2010];
void DFS(int a, int r){
	int i;
	if (a == n + 1){
		Res = min(Res, r);
		return;
	}
	if (a != 2){
		for (i = 1; i <= C[a]; i++){
			D[w[a][i]][0]++;
			if (D[w[a][i]][0] == 1 && D[w[a][i]][1])r++;
		}
		DFS(a + 1, r);
		for (i = 1; i <= C[a]; i++){
			D[w[a][i]][0]--;
			if (!D[w[a][i]][0] && D[w[a][i]][1])r--;
		}
	}
	if (a != 1){
		for (i = 1; i <= C[a]; i++){
			D[w[a][i]][1]++;
			if (D[w[a][i]][1] == 1 && D[w[a][i]][0])r++;
		}
		DFS(a + 1, r);
		for (i = 1; i <= C[a]; i++){
			D[w[a][i]][1]--;
			if (!D[w[a][i]][1] && D[w[a][i]][0])r--;
		}
	}
}
int main(){
	int i, j, cc;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d", &n);
		Map.clear();
		gets(p);
		cnt = 0;
		for (i = 1; i <= n; i++){
			gets(p);
			C[i] = 0;
			for (j = 0; p[j]; j++){
				cc = 0;
				while (p[j] != ' ' && p[j]){
					pp[cc++] = p[j];
					j++;
				}
				pp[cc] = 0;
				if (!Map[pp]){
					Map[pp] = ++cnt;
				}
				C[i]++;
				w[i][C[i]] = Map[pp];
				if (!p[j])break;
			}
		}
		Res = cnt;
		DFS(1, 0);
		printf("%d\n", Res);
	}
}