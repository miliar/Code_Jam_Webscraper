#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

int lef[15][40][100];
int out[100];

int N = 500, L = 32, have = 0;
int cal(long long a, int base){
	int b = 0;
	for(int k = 2; k < 90; k++){
		b = 0;
		for(int i = L - 1; i >= 0; i--){
			if(a & (1<<i)) b += lef[base][i][k];
		}
		if(b % k == 0) return k;
	}
	return -1;
}

int main() {
	int T;
	scanf("%d%d%d", &T, &L, &N);
	for(int i = 2; i <= 10; ++i){
		for(int k = 2; k < 100; ++k){
			lef[i][0][k] = 1;
			for(int j = 1; j < 40; j++){
				lef[i][j][k] = lef[i][j - 1][k] * i % k;
			}
		}
	}
	printf("Case #1:\n");
	for(int i = 0; ; i++){
		long long now = (1ll<<(L - 1)) + i * 2 + 1;
		int ok = 1;
		for(int j = 2; j <= 10; j++){
			out[j] = cal(now, j);
			if(out[j] == -1){
				ok = 0;
				break;
			}
		}
		if(ok){
			have++;
			printf("1");
			for(int j = L - 3; j >= 0; j--){
				if(i & (1 << j))printf("1");
				else printf("0");
			}
			printf("1");
			for(int j = 2; j <= 10; j++){
				printf(" %d", out[j]);
			}
			printf("\n");
		}
		if(have == N){
			break;
		}
	}
	return 0;
}

