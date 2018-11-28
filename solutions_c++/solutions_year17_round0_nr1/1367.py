#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define CL(A,I) (memset(A,I,sizeof(A)))

#define FOR(i, m, n) for (int i=m; i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)

#define D(X) cout<<"  "<<#X": "<<X<<endl;

using ll=long long;
using ii=pair<ll,ll>;
using vi=vector<ll>;
using vii=vector<ii>;

#define aa first
#define bb second

#define EPS (1e-9)
#define EQ(A,B) (A+EPS>B&&A-EPS<B)

string s;
int k;

int solve(){
    cin>>s>>k;
    int ans=0;
    F(s.size()){
        if(s[i]^'+'){
            if(i+k>s.size())return -1;
            FF(k)if(s[i+j]^'+')s[i+j]='+';else s[i+j]='-';
            ans++;
        }
    }
    return ans;
}

int main() {
    int t;cin>>t;
    F(t){
        int x=solve();
        cout<<"Case #"<<i+1<<": ";
        if(~x)cout<<x<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}