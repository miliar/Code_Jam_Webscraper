#include<bits/stdc++.h>
using namespace std;

string s;
void solve(int x)
{
    printf("Case #%d: ",x);
    cin>>s;
    reverse(s.begin(),s.end());
    int add = 0;
    int ans = 0;
    for(int i=0;i<s.size();i++)
    {
        int now = (s[i]=='-');
        now+=add;
        if(now%2)
        {
            ans++;
            add++;
        }
    }
    printf("%d\n",ans);
}
int main()
{
    freopen("234.in","r",stdin);
    freopen("233.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
        solve(i);
    return 0;
}
