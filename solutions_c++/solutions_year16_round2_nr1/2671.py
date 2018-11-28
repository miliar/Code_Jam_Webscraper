#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

const char *abc[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
char s[2010];
int len;
int cnt[256];
//0: Z E R O 4
//1: O N E 3 7
//2: T W O 3 10
//3: T H R E E 5 15
//4: F O U R 4 19
//5: F I V E 4 23
//6: S I X 3 26
//7: S E V E N 5 31
//8: E I G H T 5 36
//9: N I N E 4 40
//40
//
//Z: 0
//W: 2
//U: 4
//X: 6
//G: 8
//0 2 4 6 8
//O: 1
//T: 3
//F: 5
//S: 7
//9
const char e[10] = {'Z','O','W','T','U','F','X','S','G','E'};
int ans[10];

int main()
{
	int T;
	scanf("%d", &T);
	for (int Case = 1;Case <= T;++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%s", s);
		len = strlen(s);
		memset(cnt, 0, sizeof(cnt) );
		for (int i = 0;i < len;++ i)
			++ cnt[s[i]];
		for (int i = 0;i < 10;i += 2)
		{
			int t = cnt[e[i]];
			ans[i] = t;
			for (int j = 0;j < strlen(abc[i]);++ j)
				cnt[abc[i][j]] -= t;
		}
		for (int i = 1;i < 10;i += 2)
		{
			int t = cnt[e[i]];
			ans[i] = t;
			for (int j = 0;j < strlen(abc[i]);++ j)
				cnt[abc[i][j]] -= t;
		}
		for (int i = 0;i < 10;++ i)
			for (int j = 1;j <= ans[i];++ j)
				printf("%d",i);
		puts("");
	}
	return 0;
}
