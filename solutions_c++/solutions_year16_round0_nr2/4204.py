#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int t, caseNum = 1, ans, i, j;
	char c[200], pre;
	scanf("%d", &t);
	while(t--){
		scanf("%s", c);
		ans = 0;
		pre = c[0];
		for(i = 1;i < strlen(c);i++){
			if(c[i] != pre){
				pre = c[i];
				ans++;
			}
		}
		if(c[strlen(c) - 1] == '-')
			ans++;
		printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}
