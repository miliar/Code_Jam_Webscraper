#include <bits/stdc++.h>
#define gcd         __gcd
#define bitcount    __builtin_popcountll
#define rep(i,j,n)  for(i=j;i<n;i++)
#define tr(it,c)    for(auto it=(c).begin();it!=(c).end();it++)
#define pb          push_back
#define mp          make_pair
#define hell        1000000007
#define uset        unordered_set
#define umap        unordered_map
using namespace std;
typedef pair<int,int> pi;
typedef long long ll;

template <class T> T& get(T &n) {
    cin>>n;
    return n;
}

int main() {
    static char ans_string[100];
    static int T,N,i,j,k;
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    get(T);
    rep(k,1,T+1){
        get(N);
        int m=0,ans;
        vector<int> v(N);
        rep(i,0,N){
            get(v[i]);
            m=max(m,v[i]);
        }
        ans=m;
        rep(i,1,m+1){
            int tans=i;
            rep(j,0,N){
                tans+=v[j]/i;
                if(v[j]%i==0)
                    tans--;
            }
            ans=min(ans,tans);
        }
        sprintf(ans_string, "Case #%d: %d", k, ans);
        cout<<ans_string<<'\n';
    }
    return 0;
}

