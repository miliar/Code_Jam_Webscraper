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

double v[210];
vector<double> vx;
int n, k;

double dp[201][201];
bool seen[201][201];

double ff(int a, int b) {
    if(a==k/2 && b==k/2) 
        return 1;
    if(seen[a][b])return dp[a][b];
    double ret=0;
    int j=a + b;
    if(a<k/2)
        ret += vx[j] * ff(a+1, b);
    if(b<k/2)
        ret+= (1.0-vx[j]) * ff(a, b+1);
    seen[a][b]=1;
    return dp[a][b]=ret;
}

double f(int mask) {
    vx.clear();
    for(int i=0;i<n;i++)if(mask & (1<<i)) {
        vx.pb(v[i]);
    }
    memset(seen, 0, sizeof seen);
    return ff(0, 0);
}

int main(void) {
    int T;cin>>T;
    for(int tt=0;tt<T;tt++) {
        cin>>n>>k;
        for(int i=0;i<n;i++)
            cin>>v[i];
        double ans=0;
        for(int us=0;us<1<<n;us++)if(__builtin_popcount(us)==k) {
            ans=max(f(us), ans);
        }
        printf("Case #%d: %.9lf\n", tt+1, ans);
    }
	
	return 0;
}
