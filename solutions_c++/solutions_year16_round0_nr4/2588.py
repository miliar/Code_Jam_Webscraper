#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long
ll t, c, k, s;
int power(int a, int b){
	if (b == 0) return 1;
	if (b == 1) return a;
	int half;
	if (b % 2 == 0){
		half = power(a, b/2);
		half *= half;
	} else {
		half = power(a, (b - 1)/2);
		half *= half;
		half *= a;
	}
	return half;
}
int main(){
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-out.txt", "w", stdout);
	scanf("%lld", &t);
	for (ll i = 0; i < t; i++){
		scanf("%lld%lld%lld", &k, &c, &s);
		printf("Case #%lld:", i + 1);
		for (int j = 0; j < s; j++){
			printf(" %lld", j + 1);
		}
		printf("\n");
	}
}
