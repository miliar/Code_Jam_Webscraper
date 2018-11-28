#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int N = 1010;

int n, a[N];

int main(){

	int tcase; scanf("%d", &tcase);
	for (int i = 1; i <= tcase; ++ i){
		scanf("%d", &n);
		char c = getchar();
		for (; c < '0' || c > '9'; c = getchar());
		for (int j = 0; j <= n; ++ j, c = getchar()) a[j] = c - '0';

		int ans = 0;
		for (int j = 0, clap = 0; j <= n; ++ j){
			if (clap < j) ans += j - clap, clap += j - clap;
			clap += a[j];
		}
		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}
