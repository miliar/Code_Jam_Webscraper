#include <bits/stdc++.h>
using namespace std;
char s[300000];
int len;
int stk[300001] , top;
int main()
{
	int test;scanf("%d" , &test);
	for(int tt = 1 ; tt <= test ; tt++)
	{
		scanf("%s" , s + 1);
		len = strlen(s + 1);
		top = 0;
		int same = 0 , diff = 0;
		for(int i = 1 ; i <= len ; i++)
		{
			if(top && stk[top] == s[i])
			{
				top--;
				same++;
			}
			else
			{
				stk[++top] = s[i];
			}
		}
		diff = len / 2 - same;
		printf("Case #%d: %d\n" , tt , same * 10 + diff * 5);
	}
	return 0;
}