/*#include<stdio.h>
#define SZ 20
int w[SZ][SZ], C[SZ][SZ][SZ], D[SZ][SZ], a, b;
void Do(int x, int y, int ck){
	if (y && w[x][y] == w[x][y - 1]){
		D[x][y] += ck;
		D[x][y - 1] += ck;
	}
	if (y == b - 1 && w[x][y] == w[x][0]){
		D[x][y] += ck;
		D[x][0] += ck;
	}
	if (x && w[x][y] == w[x-1][y]){
		D[x][y] += ck;
		D[x-1][y] += ck;
	}
}
void Add(){
	int i, j, k, c = 0;
	for (i = 0; i < b; i++){
		for (j = 0; j < a; j++){
			for (k = 0; k < b; k++){
				if (w[j][k] != w[j][(k + i) % b])break;
			}
			if (k != b)break;
		}
		if (j == a)c++;
	}
	C[a][b][c]++;
	for (i = 0; i < a; i++){
		for (j = 0; j < b; j++){
			if (w[i][j] == 3 && w[i][(j + 1) % b] != 3){
				while (1){
				}
			}
		}
	}
	for (i = 0; i < a; i++){
		for (j = 0; j < b; j++){
			if (w[i][j] == 3)break;
		}
		if (j != b)break;
	}
	if (i == a){
		for (i = 0; i < a; i++){
			for (j = 0; j < b; j++){
				printf("%d ", w[i][j]);
			}
			printf("\n");
		}
		printf("\n");
	}
}
void DFS(int x, int y){
	int i;
	if (x == a){
		for (i = 0; i < b; i++)if (D[x - 1][i] != w[x - 1][i])break;
		if (i != b)return;
		Add();
		return;
	}
	if (y == b){
		for (i = 0; i < b; i++){
			if (D[x][i] > w[x][i] || D[x][i] + 1 < w[x][i])break;
		}
		if (i != b)return;
		if (x == 0){
			DFS(x + 1, 0);
			return;
		}
		for (i = 0; i < b; i++){
			if (D[x - 1][i] != w[x - 1][i])break;
		}
		if (i != b)return;
		DFS(x + 1, 0);
		return;
	}
	w[x][y] = 1;
	Do(x, y, 1);
	DFS(x, y + 1);
	Do(x, y, -1);
	w[x][y] = 2;
	Do(x, y, 1);
	DFS(x, y + 1);
	Do(x, y, -1);
	w[x][y] = 3;
	Do(x, y, 1);
	DFS(x, y + 1);
	Do(x, y, -1);
}
void Do(int n, int m){
	a = n, b = m;
	DFS(0, 0);
}
int main(){
	int i, j, TT, TC, S;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (i = 2; i <= 3; i++){
		for (j = 3; j <= 15; j++){
			Do(i, j);
		}
	}
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d%d", &a, &b);
		S = 0;
		for (i = 1; i <= b; i++){
			if (b%i == 0)S += C[a][b][i] / (b / i);
		}
		printf("%d\n", S);
	}
}*/
#include<stdio.h>
int cnt, n, m;
long long D[110][20], D2[110][20], Mod = 1000000007;
struct A{
	int a, b;
}w[5];
void Add(int a, int b){
	w[cnt].a = a, w[cnt].b = b;
	cnt++;
}
int gcd(int a, int b){
	return b ? gcd(b, a%b) : a;
}
void DP(){
	int i, j, k, x, t, g;
	for (i = 1; i <= n; i++){
		for (j = 1; j <= 12; j++)D[i][j] = D2[i][j] = 0;
		for (j = 0; j < cnt; j++){
			if (w[j].a == i){
				D[i][w[j].b]++;
				D2[i][w[j].b]++;
			}
			if (w[j].a + 2 == i){
				D[i][w[j].b]++;
				D2[i][w[j].b]++;
			}
			if (w[j].a + 2 > i)continue;
			x = i - (w[j].a + 2);
			for (k = 1; k <= 12; k++){
				if (!D[x][k])continue;
				g = gcd(k, w[j].b);
				t = k*w[j].b / g;
				D[i][t] = (D[i][t] + D2[x][k] * g) % Mod;
				D2[i][t] = (D2[i][t] + D2[x][k] * g) % Mod;
			}
		}
		if (i == 2){
			D[i][1]++;
		}
		if (i > 2){
			for (j = 1; j <= 12; j++){
				D[i][j] = (D[i][j] + D2[i - 2][j]) % Mod;
			}
		}
	}
}
int main(){
	int TT, TC, i, j;
	long long Res;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d%d", &n, &m);
		cnt = 0;
		if (m % 1 == 0)Add(1, 1);
		if (m % 3 == 0)Add(2, 3);
		if (m % 6 == 0)Add(2, 6);
		if (m % 4 == 0)Add(3, 4);
		DP();
		Res = 0;
		for (i = 1; i <= 12; i++)Res = (Res + D[n][i]) % Mod;
		printf("%lld\n", Res);
	}
}