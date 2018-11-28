#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))

using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

const int INF=0x3f3f3f3f;

const int N=5;
int m2[N][N], m[N][N], n;
vi v;

int dp[N][1<<N];

bool fu(int j, int mask) {
    if(j==n) 
        return 1;
    if(dp[j][mask]!=-1)return dp[j][mask];
    int u=v[j];
    bool ok=1, ss=0;
    for(int i=0;i<n;i++)if(m2[u][i] && !(mask & (1<<i))) {
        ss=1;
        ok &= fu(j+1, mask | (1<<i));
    }
    //cout<<ss<<endl;
    if(!ss)return dp[j][mask]=false;
    return dp[j][mask]=ok;
}

int f() {
    v.clear();
    For(i,0,n) v.pb(i);
    bool ok=1;
    do { 
        memset(dp, -1, sizeof dp);
        ok &= fu(0,0);
        if(!ok)break;
    }while(next_permutation(v.begin(), v.end()));

    return ok;
}

int fx(int i, int sp) {
    if(i==n) {
        if(f())
            return sp;
        return INF;
    }
    int ret=INF;
    for(int us=0;us<(1<<n);us++) {
        int spx=0;
        for(int k=0;k<n;k++)
            m2[i][k]=m[i][k];
        for(int k=0;k<n;k++) if(us & (1<<k)) {
            if(!m[i][k]) {
                //cout<<"##\n";
                m2[i][k]=1;
                spx++;
            }
        }
        ret =min(ret, fx(i+1, sp+spx));
    }
    return ret;
}

int main(void) {
    int T;cin>>T;
    For(tt, 0, T) {
        cin>>n;
        cout<<"Case #"<<tt+1<<": ";
        For(i,0,n)
            For(j,0,n)scanf("%1d", &m[i][j]);

        cout<<fx(0,0)<<endl;
    }

	
	return 0;
}
