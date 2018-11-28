#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 0; test < T; test++){
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", test + 1);
		long long offset = pow(K, C - 1);
		for (int i = 0; i < S; i++)
			printf(" %llu", 1 + i * offset);
		printf("\n");
	}
}
