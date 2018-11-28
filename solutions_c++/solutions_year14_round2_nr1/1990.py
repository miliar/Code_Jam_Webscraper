#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define ll long long
using namespace std;

const int N=101;

string t, s[N], of[N];
int dp[N][N], res, l[N], id, ans, num, T, p, n, m, i, j;

int f(string s, string t)
{
    int i, j, n, m, l=0, res=0;
    n=s.length();
    m=t.length();
    for(i=0; i<=n; i++)
        dp[i][0]=i;
    for(j=0; j<=m; j++)
        dp[0][j]=j;
    for(i=1; i<=n; i++)
        for(j=1; j<=m; j++)
            if(s[i-1]==t[j-1])dp[i][j]=dp[i-1][j-1]; else
                              dp[i][j]=min(dp[i-1][j], dp[i][j-1])+1;
    return dp[n][m];
}

int main()
{
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    while(T--)
    {
        num++;
        ans=0;
        p=1;
        cin>>n;
        for(i=0; i<n; i++)
        {
            cin>>t;
            s[i]="";
            of[i]=t;
            m=t.length();
            l[i]=t.length();
            for(j=0; j<m; j++)
                if(j==0||t[j]!=t[j-1])s[i]+=t[j];
            ans+=m-s[i].length();
        }
        id=s[0].length();
        for(i=1; i<n; i++)
        {
            m=s[i].length();
            if(s[i]!=s[0])
            {
                p=0;
                break;
            }
        }
        if(p)
        {
            for(i=0; i<n; i++)
            {
                res=0;
                for(j=0; j<n; j++)
                    if(i!=j)res+=f(of[i], of[j]);
                ans=min(ans, res);
            }
        }
        cout<<"Case #"<<num<<": ";
        if(p)cout<<ans<<endl; else cout<<"Fegla Won"<<endl;
    }
}
