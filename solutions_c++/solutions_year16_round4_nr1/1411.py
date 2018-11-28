#include <iostream>
#include <string.h>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int a[3],n;
string s[3][20];


void dfs(int dep,char c,int id)
{
    if(dep > 12) return ;
    s[id][dep].push_back(c);
    if(c == 'P')
    {
        dfs(dep + 1,'P',id);
        dfs(dep + 1,'R',id);
    }
    else if(c == 'R')
    {
        dfs(dep + 1,'R',id);
        dfs(dep + 1,'S',id);
    }
    else
    {
        dfs(dep + 1,'P',id);
        dfs(dep + 1,'S',id);
    }
}

bool check(string s)
{
    for(int i = 0; i < s.length(); ++i)
    {
        if(s[i] == 'R') a[0]--;
        else if(s[i] == 'P') a[1]--;
        else a[2]--;
    }
    if(a[0] == 0 && a[1] == 0 && a[2] == 0) return true;
    for(int i = 0; i < s.length(); ++i)
    {
        if(s[i] == 'R') a[0]++;
        else if(s[i] == 'P') a[1]++;
        else a[2]++;
    }
    return false;
}

string change(string s)
{
    int len = s.length();
    string res;
    for(int i = 4; i <= len; i <<= 1)
    {
        res = "";
        for(int j = 0; j < len; j += i)
        {
            string x = s.substr(j,i / 2);
            string y = s.substr(j + i / 2,i / 2);
            if(x < y) res += x + y;
            else res += y + x;
        }
        s = res;
    }
    return s;
}

void solve()
{
    int T,cnt = 0;
    dfs(0,'P',0);
    dfs(0,'R',1);
    dfs(0,'S',2);
    for(int i = 0; i < 3; ++i)
    {
        for(int j = 1; j <= 12; ++j)
        {
            s[i][j] = change(s[i][j]);
        }
    }
    cin >> T;
    while(T--)
    {
        scanf("%d",&n);
        scanf("%d %d %d",&a[0],&a[1],&a[2]);
        printf("Case #%d: ",++cnt);
        string ans;
        bool flag = false;
        for(int i = 0; i < 3; ++i)
        {
            ans = s[i][n];
            if(check(ans))
            {
                flag = true;
                break;
            }
        }
        if(flag) cout << ans << endl;
        else puts("IMPOSSIBLE");
    }
}

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    solve();
    return 0;
}
