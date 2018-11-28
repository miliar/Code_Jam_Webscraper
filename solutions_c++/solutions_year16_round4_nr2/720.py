#include <bits/stdc++.h>
using namespace std;

const int maxn=17;

int n,k,z;
long double p[maxn];
long double a[maxn];
long double dp[maxn][maxn / 2 + 1][maxn /2 + 1];
int u[maxn][maxn/2+1][maxn/2+1];

long double f(int pos,int yes,int no)
{
    if(pos==k)
    {
        if(yes || no) return 0.0;
        else return 1.0;
    }
    if(u[pos][yes][no]) return dp[pos][yes][no];
    long double res=f(pos+1,yes,no);
    if(yes) res += a[pos]*f(pos+1,yes-1,no);
    if(no) res += (1.0 - a[pos])*f(pos+1,yes,no-1);
    u[pos][yes][no]=1;
    return dp[pos][yes][no] = res;
}

int main()
{
    ios::sync_with_stdio(0);
    //freopen("input.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    //scanf("%d",&T);
    cin >> T;
    for(int test=1;test<=T;++test)
    {
        //printf("Case #%d: ", test);
        cout << "Case #" << test << ": ";
        cin >> n >> k;
        for(int i=0;i<n;++i) cin >> p[i];
        /*memset(u,0,sizeof(u));
        cout << setprecision(10) << fixed << f(0,k/2,k/2) << "\n";*/

        long double ans=0.0;
        for(int i=0;i<(1<<n);++i)
        {
            int q=0;
            for(int j=0;j<n;++j) if(i&(1<<j)) a[q++]=p[j];
            if(q!=k) continue;
            memset(u,0,sizeof(u));
            ans=max(ans,f(0,k/2,k/2));
        }
        cout << setprecision(10) << fixed << ans << "\n";
    }

}
