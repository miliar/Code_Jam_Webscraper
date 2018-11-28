#include<bits/stdc++.h>

#define gcd __gcd
#define bitcount __builtin_popcountll
#define getcx getchar
#define rep(i,j,n) for(i=j;i<n;i++)
#define tr(it,c) for(auto it=(c).begin();it!=(c).end();it++)
#define pb push_back
#define mp make_pair
#define hell 1000000007
#define uset unordered_set
#define umap unordered_map
#define ll long long

using namespace std;

const int MAXN = 1e3+10;

char S[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,N,i,ans;
    int noStanding;
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {
        cin>>N;
        cin>>S;
        noStanding = 0;
        ans=0;
        rep(i,0,N+1)
        {
            int p = S[i]-'0';
            if(i>noStanding&&p)
            {
                ans+=(i-noStanding);
                noStanding+=(i-noStanding);
            }
            noStanding+=p;
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
}
