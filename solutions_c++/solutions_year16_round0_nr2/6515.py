#include <cstdio>
#include <cstring>

#define MAX 200

int T;
char S[MAX];
char ch[] = { '-' , '+' };

void solve ()
{
	int cnt = 0;
	int idx = 0;

	for (int i=strlen(S)-1; i>=0; i--)
	{
		//printf("%c %c|", S[i], ch[idx]);
		if (S[i] == ch[idx]){
			cnt++;
			idx = ++idx & 1;
		}
	}

	printf("%d\n", cnt);
}

int main ()
{
	scanf("%d", &T);

	for (int t=1; t<=T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%s", S);
		solve();
	}

	return 0;
}