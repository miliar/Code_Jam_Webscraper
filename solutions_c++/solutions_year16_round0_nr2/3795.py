#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int T;
string s;
int f[200];
int g[200];

string flip(int x)
{
    string ans = s;
    for (int i = 0; i <= x; i++)
        ans[i] = s[x - i - 1];
    return ans;
}

int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    freopen("B-large.in","r",stdin);
    freopen("a.txt","w",stdout);
	scanf("%d", &T);
	for (int cse = 1; cse <= T; cse++)
	{
		cin>>s;
		//for (int i = s.size() - 1; i >= 0; i--)
		f[0] = 0;
		g[0] = 0;
		for (int i = 1; i <= s.size(); i++)
        {
            if (s[i - 1] == '+')
            {
                f[i] = f[i - 1];
                g[i] = f[i - 1] + 1;
            }
            else
            {
                f[i] = g[i - 1] + 1;
                g[i] = g[i - 1];
            }
        }
        printf("Case #%d: %d\n", cse, f[s.size()]);
	}
	return 0;
}

