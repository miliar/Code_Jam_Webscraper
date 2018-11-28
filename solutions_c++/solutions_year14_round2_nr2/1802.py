#include <cstdio>

int main()
{
	int t, caseNum = 1, ans, a, b, k;
	int i, j;
	scanf("%d", &t);
	while(t--){
		scanf("%d%d%d", &a, &b, &k);
		ans = 0;
		for(i = 0;i < a;i++)
			for(j = 0;j < b;j++){
				if(i == j)
					continue;
				//printf("%d %d %d\n", i, j, i&j);
				if((int)(i&j) < k){
					ans++;
				}
			}
		for(i = 0;i < a && i < b;i++)
			if(i < k)
				ans++;
		printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
