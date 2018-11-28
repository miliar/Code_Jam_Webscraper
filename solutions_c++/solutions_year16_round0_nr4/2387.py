#include<bits/stdc++.h>
using namespace std;

#define int long long
typedef pair<int,int>pint;
typedef vector<int>vint;
typedef vector<pint>vpint;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) (v).begin(),(v).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
template<class T,class U>inline void chmin(T &t,U f){if(t>f)t=f;}
template<class T,class U>inline void chmax(T &t,U f){if(t<f)t=f;}

void solve(int num){
    cout<<"Case #"<<num+1<<":";
    int K,C,S;
    cin>>K>>C>>S;
    if((K+C-1)/C>S){
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }

    rep(i,(K+C-1)/C){
        int p=1;
        rep(j,C){
            int k=i*C+j+1;
            if(k>K)k=1;
            p=(p-1)*K+k;
        }
        cout<<" "<<p;
    }
    cout<<endl;
}

signed main(){
    int T;
    cin>>T;
    rep(i,T)solve(i);
    return 0;
}
