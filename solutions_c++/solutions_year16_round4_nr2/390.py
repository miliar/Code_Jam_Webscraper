#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef pair<int,int>pint;
typedef vector<int>vint;
typedef vector<pint>vpint;
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
template<class T,class U>inline void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>inline void chmax(T &t,U f){if(t<f)t=f;}

int N,K;
double P[200];
double dp[210][110];

double calc(vector<double>p){

    rep(i,210)rep(j,110)dp[i][j]=0;
    dp[0][0]=1;

    rep(i,K){
        for(int j=0;j<=K/2;j++){
            dp[i+1][j]+=dp[i][j]*(1-p[i]);
            dp[i+1][j+1]+=dp[i][j]*p[i];
        }
    }
    return dp[K][K/2];
}

void solve(int Case){
    cout<<"Case #"<<Case+1<<": ";

    cin>>N>>K;
    rep(i,N)cin>>P[i];
    sort(P,P+N);

    double ma=0;
    for(int i=0;i<=K;i++){
        vector<double>p;
        for(int j=0;j<i;j++)p.pb(P[j]);
        for(int j=0;j<K-i;j++)p.pb(P[N-1-j]);
        sort(all(p));
        chmax(ma,calc(p));
    }
    printf("%.20f\n",ma);
}

signed main(){
    int T;
    cin>>T;
    rep(i,T)solve(i);
    return 0;
}

