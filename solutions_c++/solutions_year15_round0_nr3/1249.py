#include <cstdio>
#include <map>
#include <list>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int L;
long long X;
char in[100005];
int in2[100005];
int suf[100005];
int pre[100005];
int loop[4];
int mat[4][4] = {
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4}};

int mul(int x, int y){
	if ((x >= 4) ^ (y >= 4)) return (mat[x % 4][y % 4] + 4) % 8;
	else return mat[x % 4][y % 4];
}

bool solve(){
	scanf("%d%lld%s", &L, &X, in);
	int n = L;
	int code[2] = {0, 0};

	for (int i = 0; i < L; i++) in2[i] = in[i] - 'h';
	suf[L] = 0;
	for (int i = L - 1; i >= 0; i--) suf[i] = mul(in2[i], suf[i + 1]);
	pre[0] = in2[0];
	for (int i = 1; i < L; i++) pre[i] = mul(pre[i - 1], in2[i]);
	loop[0] = 0;
	for (int i = 1; i < 4; i++) loop[i] = mul(loop[i - 1], suf[0]);

	if (X > 8){
		for (int i = 0; i < n; i++){
			for (int k = 0; k < 4; k++){
				if (mul(loop[k], pre[i]) != 1) continue;
				for (int j = 0; j < n; j++){
					for (int l = 0; l < 4; l++){
						if (mul(suf[j], loop[l]) != 3) continue;
						if (mul((i + 1 == n ? 0 : suf[i + 1]), mul(loop[(X - k - l - 2) % 4], (j == 0 ? 0 : pre[j - 1]))) == 2) return true;
					}
				}
			}
		}
	}
	else{
		n = (int) L * X;
		for (int i = 0; i < n; i++) in2[i] = in[i % L] - 'h';
		suf[n] = 0;
		for (int i = n - 1; i >= 0; i--) suf[i] = mul(in2[i], suf[i + 1]);

		for (int i = 0; i < n; i++){
			code[0] = mul(code[0], in2[i]);
			if (code[0] == 1){
				code[1] = 0;
				for (int j = i + 1; j < n - 1; j++){
					code[1] = mul(code[1], in2[j]);
					if (code[1] == 2){
						if (suf[j + 1] == 3) return true;
					}
				}
			}
		}
	}
	return false;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: %s\n", t, solve() ? "YES" : "NO");
	}
	return 0;
}
