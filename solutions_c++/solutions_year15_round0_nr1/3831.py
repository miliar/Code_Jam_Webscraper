#define _CRT_SECURE_NO_DEPRECATE
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
using namespace std;

const int MaxN = 1000 + 10;
int N, L, total, Ans;
char A[MaxN];

int main(){
	freopen("1.txt", "r", stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d", &N);
	for (int i = 1; i <= N; i++){
		scanf("%d%s", &L, A);
		total = A[0] - '0';
		Ans = 0;
		for (int i = 1; i <= L; i++){
			if (i > total){
				Ans += i - total;
				total += i - total;
			}
			total += A[i] - '0';
		}
		printf("Case #%d: %d\n",i, Ans);
	}
	return 0;
}