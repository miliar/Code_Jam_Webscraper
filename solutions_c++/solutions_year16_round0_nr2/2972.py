#include <bits/stdc++.h>
#define ll long long int
#define ull unsigned long long int
#define s(a) scanf("%lld",&a)
#define pb push_back
#define mp make_pair
#define f first
#define sc second
#define inf 10e16

using namespace std;

int main()
{
    freopen("inp1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    ll t,tt,n,i,j,k,l,w,ww,x,y,z;
    string s;
    s(t);
    for(tt=1;tt<=t;tt++) {
        s.clear();
        ll dp[111]={0};
        cin>>s;
        l = s.length();
        if(s[l-1]=='+') dp[l-1]=0;
        else dp[l-1]=1;
        for(i=l-2;i>=0;i--) {
            if(s[i]==s[i+1]) dp[i]=dp[i+1];
            else dp[i]=dp[i+1]+1;
        }
        cout<<"Case #"<<tt<<": "<<dp[0]<<endl;
    }
    return 0;
}
