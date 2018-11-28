#include <cstdio>
#include <cstring>
#include <map>
#include <iostream>
#include <queue>
#include <utility>
#include <bits/stdc++.h>
using namespace std;

#define MAXN 1001001
#define MAXINT 2147483647
int solve[1001001];


int main(){
	int t, n, T;

	solve[0] = 0;
	bool digits[10];
	for(int i = 1; i < MAXN; i++){
		memset(digits, 0, sizeof digits);
		int count = 0;
		for(int tmp1 = 1; count < 10; tmp1++){
			for(int tmp2 = tmp1*i; tmp2; tmp2 /= 10){
				if(!digits[tmp2%10]){
					digits[tmp2%10] = 1;
					count++;
					if(count == 10){
						solve[i] = tmp1*i;
						break;
					}
				}
			}
		}
	}

	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		scanf("%d", &n);
		if(!n) printf("INSOMNIA\n");
		else printf("%d\n", solve[n]);
	}

	return 0;
}
