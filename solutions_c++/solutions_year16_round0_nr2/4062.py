#include <bits/stdc++.h>
using namespace std;
char s[200];
int main()
{
	int T;scanf("%d" , &T);
	for(int tt = 1 ; tt <= T ; tt++)
	{
		printf("Case #%d: " , tt);
		scanf("%s" , s + 1);
		
		int res = 0;
		for(int i = 2 ; i <= strlen(s + 1) ; i++)
			if(s[i] != s[i - 1])++res;
		if(s[strlen(s + 1)] == '-')++res;
		printf("%d\n" , res);
	}
	return 0;
}