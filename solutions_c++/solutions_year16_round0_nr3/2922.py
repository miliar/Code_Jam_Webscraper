#include <bits/stdc++.h>
using namespace std;

int T, N, J, hitung = 0;
bool cek(long long x){
	for(int i = 2; i <= 10; i++){
		long long tmp = 1, sum = 0;
		for(int j = 0; j < 16; j++){
			if(x & (1 << j)) sum += tmp;
			tmp *= (long long)i;
		}
		bool isPrime = 1;
		for(int j = 2; j <= (int)sqrt(sum); j++)
			if(sum%j == 0) isPrime = 0;
		if(isPrime) return 0;
	}
	return 1;
}
void cetakBukti(long long x){
	for(int i = 2; i <= 10; i++){
		long long tmp = 1, sum = 0;
		for(int j = 0; j < 16; j++){
			if(x & (1 << j)) sum += tmp;
			tmp *= (long long)i;
		}
		for(int j = 2; j <= (int)sqrt(sum); j++)
			if(sum%j == 0){
				printf(" %d", j);
				break;
			}
	}
}
void solveSmall(long long x, long long y){
	if(hitung == J) return;
	if(y == N-1){
		if(cek(x | (1 << N-1))){
			printf("1");
			for(int i = N-2; i >= 0; i--)
				if(x & (1 << i)) printf("1");
				else printf("0");
			cetakBukti(x | (1 << N-1));
			puts("");
			hitung++;
		}
		return;
	}
	solveSmall(x, y+1);
	solveSmall(x | (1 << y), y+1);
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	scanf("%d %d", &N, &J);
	puts("Case #1:");
	solveSmall(1, 1);
	return 0;
}
