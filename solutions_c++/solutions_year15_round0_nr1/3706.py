#include <bits/stdc++.h>
#define FOR(i,a,b) for(int i = (a) ; i<b ; i++)
#define Set(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back
#define all(v) (v.begin(), v.end())
typedef long long LL;
using namespace std;
LL MOD = 1e9+7;

string s;
int dp[1009][10009];
int solve(int idx , int stand)
{
    if(stand<idx)return 1e9;
    if(idx==s.size())return 0;
    if(dp[idx][stand]!=-1) return dp[idx][stand];
    int mini=1e9;
    for(int i=0;i<=9;i++)
        mini=min(mini,solve(idx+1,stand+s[idx]-'0'+i)+i);
    return dp[idx][stand] = mini;
}


int main()
{
    ios_base::sync_with_stdio(0);
    //freopen("input.in", "r", stdin);
    //freopen("output.txt", "w", stdout);

     int t;cin>>t;
    int kase=0;
    while(t--)
    {
        int dum;cin>>dum;
        cin>>s;
        Set(dp,-1);
        int res = solve(0,0);
        cout << "Case #" << ++kase << ": " << res <<endl;
    }


    return 0;
}
