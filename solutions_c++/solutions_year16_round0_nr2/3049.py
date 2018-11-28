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
    string s;cin>>s;

    int ans=0;
    if(s[0]=='-')ans--;
    rep(i,s.size()){
        if(s[i]=='+')continue;
        ans+=2;
        int cur=i;
        while(cur<s.size()&&s[cur]=='-'){
            s[cur]='+';
            cur++;
        }
    }
    cout<<"Case #"<<num+1<<": "<<ans<<endl;
}

signed main(){
    int T;
    cin>>T;
    rep(i,T)solve(i);
    return 0;
}
