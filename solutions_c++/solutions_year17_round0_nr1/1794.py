#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

int solve()
{
    string s;
    int k,ans,n;
    cin>>s>>k;
    n = s.length();
    ans = 0;
    for (int i=0;i<=n-k;i++)
    {
        if (s[i]=='+') continue;
        for (int j=i;j<i+k;j++)
        {
            if (s[j]=='+') s[j] = '-'; else s[j] = '+';
        }
        ++ans;
    }

    for (int i=0;i<n;i++)
    {
        if (s[i]=='+') continue;
        return -1;
    }

    return ans;
}
int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T,res;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        res = solve();
        cout<<"Case #"<<test<<": ";
        if (res==-1) cout<<"IMPOSSIBLE"<<endl; else cout<<res<<endl;
    }
    return 0;
}
