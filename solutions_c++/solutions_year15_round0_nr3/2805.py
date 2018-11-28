#include<stdio.h>

int mat[5][5] = { 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 0, 2, -1, 4, -3, 0, 3, -4, -1, 2, 0, 4, 3, -2, -1 };
bool flag;
int i, N, L, p, T, A[200000], j, k, one, two, three, check[200000],pos;
char B[200000];

int abs(int x){
	if (x < 0)return -x;
	return x;
}

int main(){
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (p = 1; p <= T; p++){
		scanf("%d %d ", &N, &L);
		scanf("%s", &B);
		flag = false;
		pos = 0;
		for (i = 0; i < N; i++){
			if (B[i] == 'i')A[i] = 2;
			if (B[i] == 'j')A[i] = 3;
			if (B[i] == 'k')A[i] = 4;
		}
		one = 1;
		for (i = 0; i < L; i++){
			for (j = 0; j < N; j++){
				A[(i*N) + j] = A[j];
				if (one < 0)one = -mat[abs(one)][A[j]];
				else one = mat[one][A[j]];
				if (one == 2)check[pos++] = (i*N) + j;
			}
		}
		N *= L;
		for (i = 0; i < pos; i++){
			two = 1;
			for (j = check[i]+1; j < N; j++){
				if (two < 0){
					two = -mat[abs(two)][A[j]];
				}
				else two = mat[two][A[j]];
				if (two != 3)continue;
				for (k = 1; k <= 4; k++){
					if (mat[4][k] == one&&k == 4){
						flag = true;
						break;
					}
				}
				if (flag)break;
			}
			if (flag)break;
		}
		printf("Case #%d ", p);
		if (flag)printf("YES\n");
		else printf("NO\n");
	}
}