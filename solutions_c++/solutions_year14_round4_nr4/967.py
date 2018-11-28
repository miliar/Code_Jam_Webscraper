#include<bits/stdc++.h>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64
#define MOD 1000000007

int dp[1<<8][5],val[1<<9],dp2[1<<8][5],vis[1<<8][5];
string s[10];
int solve(int mask,int m){
    if(mask == 0){
        return -inf;
    }
    if(m == 1){
        dp2[mask][m] = 1;
        return val[mask]+1;
    }
    int &ret = dp[mask][m];
    int &ret2 = dp2[mask][m];
    if(vis[mask][m]) return ret;
    vis[mask][m] = 1;
    ret = -inf;
    ret2 = 0;
    int i;
    for(i = mask - 1, i&=mask;i;i--, i&=mask){
        int r = solve(mask ^ i, m - 1)+val[i]+1;
        if(r<0) continue;
        if(r>ret){
            ret = r;
            ret2 = dp2[mask^i][m-1];
        }
        else if(r == ret){
            ret2+=dp2[mask^i][m-1];
            ret2%=MOD;
        }
    }
    return ret;
}
int main(){
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    int t,cs=1,i,j,k,m,n,cnt;

    cin>>t;
    while(t--){
        cin>>n>>m;
        for(i = 0;i<n;i++) cin>>s[i];
        val[0] = 0;
        for(i = 1;i<(1<<n);i++){
            vector<string> v;
            for(j = 0;j<n;j++){
                if(!(i & (1<<j))) continue;
                v.pb(s[j]);
            }
            sort(all(v),greater<string>());
            cnt = v[0].length();
            for(j = 1;j<v.size();j++){
                for(k = 0;k<v[j].size();k++){
                    if(v[j][k]!=v[j-1][k]) break;
                }
                cnt+=v[j].size() - k;
            }
            val[i] = cnt ;
        }
        CLR(vis);
        solve((1<<n)-1,m);
        printf("Case #%d: %d %d\n",cs++,solve((1<<n)-1,m),dp2[(1<<n)-1][m]);
    }
	return 0;
}
