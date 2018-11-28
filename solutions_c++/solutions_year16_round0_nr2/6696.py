#include <cstdio>
#include <cstring>
#include <algorithm>
#define convert(c) (c=='+'?'-':'+')
char str[105];
int T;

void trim()
{
	int i = 0;
	while (true)
	{
		if (str[i] != '+' && str[i] != '-')
		{
			str[i] = '\0';
			break;
		}
		i++;
	}
}
void reverse(int n)
{
	for (int i = 0; i <= n / 2; i++)
	{
		char tmp = convert(str[i]);
		str[i] = convert(str[n - i]);
		str[n - i] = tmp;
	}
}
int main(void)
{
	scanf("%d", &T);
	gets(str);
	for (int t = 1; t <= T; t++)
	{
		gets(str);
		trim();
		int len = strlen(str);
		int cnt = 0;
		for (int i = 1; i < len; i++)
		{
			if (str[i] != str[i - 1]){
				reverse(i - 1);
				cnt++;
			}
		}
		if (str[0] == '-')
			cnt++;
		printf("Case #%d: %d", t, cnt);
		if (t != T)
			putchar('\n');
	}
}