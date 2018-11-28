#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t, n, cnt, ls;
char s[1005];
bool ch;

int main()
{
	// freopen("A-large.in", "r", stdin);
	// freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
    {
    	cnt = 0;
    	ch = true;
    	scanf("%s %d", s, &n);
    	ls = strlen(s);
    	for(int i = 0; i < ls - n + 1; ++i)
    	{
    		if(s[i] == '-')
    		{
    			for(int j = 0; j < n; ++j)
    				s[i + j] = s[i + j] == '-'? '+': '-';
    			++cnt;
    		}
    	}
    	// printf("%s %d %d\n", s, ls, n);
    	for(int i = ls - n + 1; i < ls; ++i)
    		if(s[i] == '-')
    		{
    			ch = false;
    			printf("Case #%d: IMPOSSIBLE\n", z);
    			break;
    		}
    	if(ch)
    		printf("Case #%d: %d\n", z, cnt);
    }
    return 0;
}