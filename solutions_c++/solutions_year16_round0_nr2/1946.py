#include <bits/stdc++.h>

using namespace std;

#define ld long double
#define pld pair<ld,ld>
#define ff first
#define ss second
#define vpld vector<pld>
#define pb push_back
#define LL long long
#define MOD 1000000007

LL dp[105][5];

int main()
{
    int t;
    cin >> t;
    for(int tt = 1; tt<=t;++tt){
    string s;
    cin >> s;
    for(int i = 0 ; i<=101 ; ++i)
    {
        for(int j = 0 ; j<=3; ++j)dp[i][j] = MOD;
    }

    vector<char> V;

    V.pb(s[0]);
    
    for(int i = 1;i<s.size();++i)
    {
        if(s[i]!=V[V.size()-1])
        {
            V.pb(s[i]);
        }
    }

    string tmp(V.begin() , V.end());

    s = tmp;

    dp[0][0] = 0;
    dp[0][1] = 0;

 //   cout<<s<<"\n";

    for(int i = 1 ; i<=s.size() ; ++i)
    {
        if(s[i-1]=='+')
        {
            dp[i][0] = min(dp[i-1][1]+1 , dp[i-1][0]);
            dp[i][1] = min(dp[i-1][1]+2,dp[i-1][0]+1);
        }

        else
        {
            dp[i][1] = min(dp[i-1][0]+1 , dp[i-1][1]);
            dp[i][0] = min(dp[i-1][0]+2 ,dp[i-1][1]+1);
        }
    }

    cout <<"Case #"<<tt<<": "<< dp[s.size()][0]<<"\n";
    }
    return 0;
}