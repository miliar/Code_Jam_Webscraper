#include<stdio.h>
#include<algorithm>
using namespace std;
int n, K, C[1010000], p[1010000], D[1010000][2];
struct A{
	int num, ck;
	bool operator<(const A &p)const{
		return num < p.num;
	}
}w[1010000];
int main(){
	int TC, TT, i, aa, bb, cc, x, cnt,Res, S;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%d: ", TT);
		scanf("%d%d", &n, &K);
		scanf("%d%d%d%d", &C[0],&aa,&bb,&cc);
		for (i = 1; i < n; i++)C[i] = (C[i - 1] * aa + bb) % cc;
		scanf("%d%d%d%d", &p[0], &aa, &bb, &cc);
		for (i = 1; i < n; i++)p[i] = (p[i - 1] * aa + bb) % cc;
		for (i = 1; i < n; i++)p[i] %= i;
		cnt = 0;
		for (i = 0; i < n; i++){
			x = i;
			D[i][0] = D[i][1] = C[i];
			while (x){
				x = p[x];
				D[i][0] = min(D[i][0], D[x][0]);
				D[i][1] = max(D[i][1], D[x][1]);
			}
			if (D[i][1] - D[i][0] > K)continue;
			w[cnt].num = D[i][1] - K; w[cnt].ck = 1; cnt++;
			w[cnt].num = D[i][0] + 1; w[cnt].ck = -1; cnt++;
		}
		sort(w, w + cnt);
		Res = 0, S = 0;
		for (i = 0; i < cnt; i++){
			S += w[i].ck;
			if (i == cnt - 1 || w[i].num != w[i + 1].num){
				if (Res < S)Res = S;
			}
		}
		printf("%d\n", Res);
	}
}