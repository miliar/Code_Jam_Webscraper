#include <stdio.h>
#include <algorithm>

using namespace std;
const int MAXN = 1009;

char s[MAXN];
int t, n, st, ans;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d" ,&t);
	
	for (int T=1; T<=t; T++)
	{
		scanf("%d" ,&n);
		scanf("%s" ,s);
		
		ans = st = 0;
		
		for (int i=0; i<=n; i++)
		{
			if (st >= i)
				st += (s[i]-'0');
			else
				ans++, st++, st += (s[i]-'0');
		}
		
		printf("Case #%d: %d\n" ,T ,ans);
	}
}
