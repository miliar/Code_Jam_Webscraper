#include<stdio.h>

int maneuver(char* s)
{
	int cnt = 1;

	char sign = s[0];
	for(int i = 0; s[i] != '\0'; i++) {
		if(sign != s[i]) { cnt++; sign = s[i]; }
	}

	if(s[0] == '-' && cnt%2 == 0) cnt--;
	if(s[0] == '+' && cnt%2 == 1) cnt--;

	return cnt;
}

int main()
{
	int T, cnt = 0;
	char s[110];
	scanf("%d", &T);
	while(T--) {
		scanf("%s", s);
		int ans = maneuver(s);
		printf("Case #%d: %d\n", ++cnt, ans);
	}
}
