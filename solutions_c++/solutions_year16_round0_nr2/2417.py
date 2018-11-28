#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
LL dp[1002][4] = {};
int i;

int main()
{
    freopen("input1.in","r+",stdin);
    freopen("output1.txt","w+",stdout);
    int T;
    cin>>T;

    for(int e = 0 ; e<T;++e)
    {
        string S;
        cin>>S;
        dp[1][0] = S[0]!='-';
        dp[1][1] = S[0]!='+';
        for(i=2;i<=S.length();++i)
        {
            dp[i][0] = S[i-1]==S[i-2] || (S[i-1]=='-') ?dp[i-1][0] : dp[i-1][0]+2 ;
            dp[i][1] = S[i-1]==S[i-2] || (S[i-1]=='+') ?dp[i-1][1] : dp[i-1][1]+2 ;
        }
        cout<<"Case #"<<e+1<<": ";
        cout<<dp[S.length()][1]<<'\n';
    }
    cout<<endl;
    return 0;
}
