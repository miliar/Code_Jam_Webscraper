#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;
FILE *fi = freopen("A-large.in", "r", stdin);
FILE *fo = freopen("ALout.txt", "w", stdout);
#define ll long long
ll tmp, k;
int n, test, bit;
int main(){
	scanf("%d", &test);
	int lev = 0;
	while (test--){
		++lev;
		bit = 0;
		scanf("%d", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA\n", lev); continue;
		}
		for (int i = 1;; i++){
			tmp = 1LL * n*i;
			 k = tmp;
			while (tmp){
				bit |= 1 << (tmp % 10); tmp /= 10;
			}
			if (bit == (1 << 10) - 1){
				 break;
			}
		}
		printf("Case #%d: %lld\n",lev,  k);
	}
}