#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
char s[205], rem[205];
int len;
void work(int l, int r)
{
	for (int i = l; i <= r; i++)
		rem[i] = ((s[i] == '+') ? '-' : '+');
	for (int i = l, j = r; i <= r; i++, j--)
		s[i] = rem[j]; 	
} 
int main()
{
//	freopen("in2.in", "r", stdin);
//	freopen("in.out", "w", stdout); 
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%s", s + 1);
		len = strlen(s + 1);
		int ans = 0;
		while(s[len] == '+')len--; 
		while(len > 0) 
		{
			if(s[1] == '+')
			{
				int p = 1;
				while(s[p] == '+')s[p] = '-',p++;
				ans ++;
			}
			work(1, len); ans++;
			while(s[len] == '+')len--;
		}
		printf("Case #%d: %d\n", t, ans); 
	}
    return 0;
} 
