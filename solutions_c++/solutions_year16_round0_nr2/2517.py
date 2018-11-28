#include<bits/stdc++.h>
using namespace std;
char s[1005];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,test = 0;
	scanf("%d\n",&T);
	while (T>0)
	{
		T--;
		scanf("%s\n",s);
		printf("Case #%d: ",++test);
		int tot = 1;
		int n = strlen(s);
		for (int i=1;i<n;i++)
			if (s[i]!=s[i-1]) tot++;
		if (s[0]=='+')
		{
			printf("%d\n",2 * (tot / 2));
		} 
		else
		{
			printf("%d\n",2 * ((tot-1) / 2) + 1);
		}
	}
}
