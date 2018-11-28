#include<bits/stdc++.h>
using namespace std;

#define sin(x) scanf("%d",&x)
#define sin2(x,y) scanf("%d%d",&x,&y)
#define sin3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define pb push_back
#define mp make_pair
#define y1 asdnqw
#define next mdamdamda
#define right praviy
#define x first
#define y second
const int N=2e5+5;
const double eps=0.1;
#define double long double
double a[45],dp[45][45];
int n,k,m,test;
double ans;
main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int test;
    int kl=0;
    cin>>test;
    for(;test;--test){
    ++kl; cout<<"Case #"<<kl<<": ";

    ans=0;
        cin>>n>>k;
        for(int i=1;i<=n;++i)
            cin>>a[i];
        for(int mask=0;mask<(1<<n);++mask)
        if(__builtin_popcount(mask)==k){
            for(int i=0;i<=k;++i)
                for(int j=0;j<=k/2;++j)
                    dp[i][j]=0;
            dp[0][0]=1;
            for(int i=1;i<=n;++i)
                if((1<<(i-1)&mask))
                for(int j=k;j>=0;--j)
            for(int z=0;z<=k/2;++z){
                dp[j+1][z+1]+=dp[j][z]*a[i];
                dp[j+1][z]+=dp[j][z]*(1-a[i]);
            }
            ans=max(ans,dp[k][k/2]);
        }
        cout.precision(7);
        cout<<fixed<<ans<<'\n';

  }
}
