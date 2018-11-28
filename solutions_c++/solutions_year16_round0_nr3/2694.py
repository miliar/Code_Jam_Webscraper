#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#define maxn 40
using namespace std;
int T, n, m, t;
int main()
{
	scanf("%d", &T);
	scanf("%d%d", &n, &m);
	t = n / 2 - 2;
	puts("Case #1:");
	for (int i = 0; i < m; ++ i){
		printf("11");
		for (int j = 0; j < t; ++ j)
			if (i & (1 << j)) printf("11"); else printf("00");
		printf("11 ");
		for (int j = 2; j <= 10; ++ j) printf("%d ", j + 1);
		puts("");
	}

}
