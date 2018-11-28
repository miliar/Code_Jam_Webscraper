#include <bits/stdc++.h>

using namespace std;

string s;
int n;

int main()
{
    freopen("B_large.in","r",stdin);
    freopen("B_large.out","w",stdout);
    int t;
    cin >> t;
    int tc;
    int i;
    for(tc=1;tc<=t;tc++)
    {
        cin >> s;
        n=s.size();
        for(i=s.size()-1;i>=0;i--)
        {
            if(s[i]=='-') break;
        }
        if(i==-1){ printf("Case #%d: 0\n",tc); continue; }
        int ans=1;
        i--;
        for(;i>=0;i--)
        {
            if(s[i]!=s[i+1]) ans++;
        }
        printf("Case #%d: %d\n",tc,ans);
    }
}
