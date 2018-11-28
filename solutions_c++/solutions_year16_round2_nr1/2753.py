#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;
int cnt[1000], ans[11];
void remove(const char s[], char c, int x)
{
	ans[x] = cnt[c];
	for(int i = 0; i < strlen(s); i++)
		cnt[s[i]] -= cnt[c];
	cnt[c] = 0;
	return;
}
void print()
{
	for(char c = 'A'; c <='Z' ; c++)
		printf("%c %d\t", c, cnt[c]);
	printf("\n");
}
int main()
{
	int T,n;
	scanf("%d", &T);
	char s[2001];
	for(int kase = 1; kase <= T; kase ++)
	{
		printf("Case #%d: ", kase);
		memset(cnt, 0, sizeof(cnt));
		memset(ans, 0, sizeof(ans));
		do{
			scanf("%s", s);
		}while(!strlen(s));
		for(int j = 0; j < strlen(s); j++)
			cnt[s[j]]++;

		remove("ERO", 'Z', 0);
		remove("FOR", 'U', 4);
		remove("EIHT", 'G', 8);
		remove("SI", 'X', 6);
		remove("TO", 'W', 2);
		remove("IVE", 'F', 5);
		remove("SEEN", 'V', 7);
		if(cnt['S'] != 0)
			fprintf(stderr, "ERROR!\n");
		remove("HREE", 'T', 3);
		remove("NE", 'O', 1);
		remove("NNE", 'I', 9);
		for(int i = 0; i < 10; i++)
			for(int j = 0; j < ans[i]; j++)
				printf("%c", '0' + i);
		printf("\n");
	}
	return 0;
}