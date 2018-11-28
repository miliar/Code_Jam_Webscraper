#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<vector>
using namespace std;

int n, m;
char s[110][110];
int a[110], b[110], T;

int main()
{
  freopen("text.in","r",stdin);
  freopen("text.out","w",stdout);
  cin >> T;
  for (int test=1; test<=T; test++)
  {
  	int ans = 0, bo = 0;
		cin >> n >> m;
		memset (a, 0, sizeof(a));
		memset (b, 0, sizeof(b));
		for (int i=0; i<n; i++)
		{
			scanf ("%s", s[i]);
			for (int j=0; j<m; j++)
				if (s[i][j] != '.') a[i]++, b[j]++;
		}
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (s[i][j] != '.')
				{
					if (a[i] == 1 && b[j] == 1)
						bo = 1;
					if (s[i][j] == '>')
					{
						int t = 0;
						for (int k=j+1; k<m; k++)
							if (s[i][k] != '.') { t = 1; break; } 
						if (t == 0) ans ++;
					}
					if (s[i][j] == '<')
					{
						int t = 0;
						for (int k=0; k<j; k++)
							if (s[i][k] != '.') { t = 1; break; } 
						if (t == 0) ans ++;
					}
					if (s[i][j] == '^')
					{
						int t = 0;
						for (int k=0; k<i; k++)
							if (s[k][j] != '.') { t = 1; break; } 
						if (t == 0) ans ++;
					}
					if (s[i][j] == 'v')
					{
						int t = 0;
						for (int k=i+1; k<n; k++)
							if (s[k][j] != '.') { t = 1; break; } 
						if (t == 0) ans ++;
					}
				}
			if (bo == 1) printf ("Case #%d: IMPOSSIBLE\n", test);
			else printf ("Case #%d: %d\n", test, ans);
	}
  return 0;
}

