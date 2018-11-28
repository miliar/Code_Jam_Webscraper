//writed by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
using namespace std;
typedef long long LL;
const int NUM = 100010;
int n, R, P, S;
char ans[NUM], *p;
void to(int R, int P, int S, int &x, int &y, int &z)
{
    x = (P + R - S) / 2;
    y = (S + P - R) / 2;
    z = (S + R - P) / 2;
}
bool solve()
{
    for(int i = 0; i < n; ++i)
    {
        to(R, P, S, P, S, R);
        if(P < 0 || S < 0 || R < 0) return false;
    }
    return true;
}
string dfs(int i, int who)
{
    if(i == n)
    {
        if(who == 1) return "P";
        else if(who == 2) return "R";
        else return "S";
    }
    else
    {
        ++i;
        string a, b;
        if(who == 1)
        {
            a = dfs(i, 1);//P
            b = dfs(i, 2);//R
            if(a < b)
				return a + b;
			else
				return b + a;
        }
        else if(who == 2)
        {
            a = dfs(i, 2);//R
            b = dfs(i, 3);//S
            if(a < b)
				return a + b;
			else
				return b + a;
        }
        else
        {
            a = dfs(i, 1);//P
            b = dfs(i, 3);//S
            if(a < b)
				return a + b;
			else
				return b + a;
        }
    }
}
int main()
{
#ifdef ACM_TEST2
    freopen("in.txt", "r", stdin);
//  freopen("in.txt", "w", stdout);
#else
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int T; scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
    	printf("Case #%d: ", cas);
        scanf("%d%d%d%d", &n, &R, &P, &S);
        if(!solve())
        {
            puts("IMPOSSIBLE");
        }
        else
        {
            string ans;
            if(P == 1) ans = dfs(0, 1);
            else if(R == 1) ans = dfs(0, 2);
            else if(S == 1) ans = dfs(0, 3);
            printf("%s\n", ans.data());
        }
    }
    return 0;
}
