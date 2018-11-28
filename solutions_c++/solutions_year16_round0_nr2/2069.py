#include<bits/stdc++.h>
using namespace std;
void solve()
{
    string s;
    int ans=0;
    cin>>s;
    for(int i=1;i<s.size();i++) if(s[i]!=s[i-1]) ans++;
    if(s[s.size()-1]=='-') ans++;
    printf("%d\n",ans);
}
int main()
{
    int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        solve();
    }
}
