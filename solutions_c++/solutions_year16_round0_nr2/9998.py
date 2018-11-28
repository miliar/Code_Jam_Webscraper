#include<bits/stdc++.h>
using namespace std;

#define fre freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define ll long long
#define abs(x) ((x)>0?(x):-(x))
#define mod 1000000007
#define scand(x) scanf("%d",&x);
#define scanlld(x) scanf("%I64d",&x);
#define scans(x) scanf("%s",x);
#define printd(x) printf("%d",x);
#define printlld(x) printf("%I64d",x);
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define inf (1<<30)
#define forup(i,a,b) for(int i=a;i<b;i++)
#define pii pair<int,int>
#define boost ios_base::sync_with_stdio(0)
#define MAXN 100003
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define pb push_back
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%I64d",&x)
#define F first
#define S second
#define maxn 105
#define mod 1000000007

int vis[12];
int dp[2][maxn];

int main(){
	fre;
	    int t;
    cin>>t;
    rep(tc,t){
        memset(dp,0,sizeof dp);
        string s;
        cin>>s;
        if(s[0]=='+')dp[1][0]=1;
        else dp[0][0]=1;
        for(int i=1;i<s.size();i++){
            dp[0][i]=(s[i]=='+'?dp[0][i-1]:dp[1][i-1]+1);
            dp[1][i]=(s[i]=='-'?dp[1][i-1]:dp[0][i-1]+1);
        }
        cout<<"Case #"<<tc+1<<": "<<dp[0][s.size()-1]<<"\n";
    }

    return 0;
}