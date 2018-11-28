#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int n, m, x, y, z, k, w, ans;
int tc, tt;
char s[1005];

void flip(int x)
{
	FOR(i, x, x + k) if (s[i] == '-') s[i] = '+'; else s[i] = '-';
	ans++;
}

int main ()
{
	scanf("%d", &tc);
	while(tc--)
	{
		scanf("%s", s);
		scanf("%d", &k);
		n = strlen(s);
	
		ans = 0;
		FOR(i, 0, n - k + 1) if (s[i] == '-') flip(i);
		FOR(i, 0, n) if (s[i] == '-') ans = -1;
		
		if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", ++tt);
		else printf("Case #%d: %d\n", ++tt, ans);
	}
	
	return 0;
}
