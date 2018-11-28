#include<bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define res resize
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
void solve(string &s){
    vector<int>dp[2];
    dp[0].res(s.size()); dp[1].res(s.size());
    if(s[0]=='+')dp[0][0]=1;
    else dp[1][0]=1;

    for(int i=1;i<s.size();i++)
        if(s[i]=='-'){
            dp[0][i]=dp[0][i-1];
            dp[1][i]=1+dp[0][i-1];
        }
        else{
            dp[1][i]=dp[1][i-1];
            dp[0][i]=1+dp[1][i-1];
        }
    cout<<dp[1][s.size()-1]<<"\n";
}
int main(){
    cout.sync_with_stdio(0);
    int t; cin>>t;
    for(int i=1;i<=t;i++){
        string s; cin>>s;
        cout<<"Case #"<<i<<": "; solve(s);
    }
	return 0;
}
