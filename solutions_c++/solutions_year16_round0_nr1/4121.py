#include <cstdio>
#include <cstdlib>
#include <cstring>

int check(char c[], char rec[])
{
	int i;
	for(i = 0;i < strlen(c);i++){
		rec[c[i] - '0'] = 1;
	}
	for(i = 0;i < 10;i++){
		if(rec[i] == 0)
			return 1;
	}
	return 0;
}

int main()
{
	int t, caseNum = 1, i;
	long long n, ans;
	char c[1000], rec[10];
	scanf("%d", &t);
	while(t--){
		scanf("%lld", &n);
		if(n == 0)
			printf("Case #%d: INSOMNIA\n", caseNum++);
		else{
			for(i = 0;i < 10;i++)
				rec[i] = 0;
			ans = n;
			sprintf(c, "%lld", ans);
			while(check(c, rec)){
				ans += n;
				sprintf(c, "%lld", ans);
			}
			printf("Case #%d: %lld\n", caseNum++, ans);
		}
	}
	return 0;
}
