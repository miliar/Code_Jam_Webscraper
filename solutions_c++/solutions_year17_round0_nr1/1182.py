#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

bool ok(string s)
{
    for(int i=0;i<s.length();i++)
        if(s[i]=='-')
            return false;
    return true;
}
string s;
int m;
int solve()
{
    int ans=0;
    for(int i=0;i<=s.length()-m;i++)
    {
        if(s[i]=='-')
        {
            for(int j=0;j<m;j++)
                s[i+j]=(s[i+j]=='-'?'+':'-');
            ans++;
        }
        if(ok(s))
            return ans;
    }
    return -1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        cin>>s>>m;
        int ans=solve();
        if(ans==-1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}
