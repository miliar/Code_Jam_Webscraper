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
    cout<<"Case #"<<num+1<<":"<<endl;

    int N,J;
    cin>>N>>J;
    int n=N/2;
    for(int i=0;i<(1<<n)&&J;i++){
        if((i&1)==0)continue;
        if((i>>(n-1)&1)==0)continue;
        rep(j,n-1)if((i>>j&1)&&(i>>(j+1)&1))continue;
        rep(j,n)cout<<((i>>j&1)?"11":"00");
        reps(j,2,10+1)cout<<" "<<j+1;
        cout<<endl;
        J--;
    }    
}

signed main(){
    int T;
    cin>>T;
    rep(i,T)solve(i);
    return 0;
}
