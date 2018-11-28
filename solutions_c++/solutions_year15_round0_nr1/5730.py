#include <cstdlib>
#include <cstdio>

int main()
{
	int T, n, i, j, k, digit, ans, now;
	char shy[1005];
	int p[1005];
	scanf("%d", &T);
	for(i = 0; i < T; i++){
		scanf("%d", &n);
		scanf("%s", shy);
		for(j = 0; j <= n; j++){
			p[j] = shy[j]-'0';
		}
		now = 0;
		now += p[0];
		ans = 0;
		for(j = 1; j <= n; j++){
			if(now > j)
				now += p[j];
			else{
				ans += (j - now);
				now += (j - now);
				now += p[j]; 
			}
		}
		printf("Case #%d: %d\n",i+1, ans);
	}
}

