#include <cstdio>
#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cmath>
using namespace std;
#define LL long long
#define MAXN 1000000
int num[10], cnt;
void gao(int n){
	// printf("%d\n", n);
	while(n){
		if(!num[n%10]){
			num[n%10] = 1;
			cnt++;
		}
		n /= 10;
	}
}
int main()
{
	int T;
	scanf("%d", &T);
	int n, o = 0;
	while(T--){
		scanf("%d", &n);
		cnt = 0;
		int i = 1;
		memset(num, 0, sizeof(num));
		int t = 0;
		while(cnt < 10 && ++t < MAXN){
			gao(n*i++);
		}
		if(t >= MAXN) printf("Case #%d: INSOMNIA\n", ++o);
		else printf("Case #%d: %d\n", ++o, n*(i-1));
	}

	return 0;
}