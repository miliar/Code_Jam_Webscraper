#include<stdio.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		int S, ans=0, cur=0;
		char aud[1100] = {0,};
		scanf("%d%s", &S, aud);
		for(int i = 0; i <= S; i++){
			if((aud[i]-'0') == 0)continue; 
			if(cur < i) {
				ans += (i-cur);
				cur += (i-cur);
			}
			cur += (aud[i]-'0');
		}
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}