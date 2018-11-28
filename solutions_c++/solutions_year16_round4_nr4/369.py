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

int N;
int G[4][4];

bool f(){

    rep(i,N){
        vint p;
        rep(j,N)if(i!=j)p.pb(j);
        bool ex=false;
        vint q;
        rep(j,N)q.pb(j);
        do{
            do{
                bool ok=true;
                rep(j,N-1){
                    if(G[p[j]][q[j]]==0){
                        ok=false;
                        break;
                    }
                }
                if(!ok)continue;
                ex=true;
                if(G[i][q[N-1]]==0)return false;
            }while(next_permutation(all(q)));
        }while(next_permutation(all(p)));
        if(!ex)return false;
    }
    return true;
}

void solve(int Case){
    cout<<"Case #"<<Case+1<<": ";

    int GG[4][4];
    cin>>N;
    rep(i,N)rep(j,N){
        char c;cin>>c;
        GG[i][j]=c-'0';
    }

    int ans=1001001001;
    rep(b,1<<(N*N)){
        bool ok=true;
        rep(i,N){
            rep(j,N){
                if(GG[i][j]&&(b>>(i*N+j)&1)){
                    ok=false;
                }
                G[i][j]=GG[i][j]|(b>>(i*N+j)&1);
            }
        }
        if(!ok)continue;
        int cnt=0;
        rep(i,N*N)if(b>>i&1)cnt++;
        if(f())chmin(ans,cnt);
    }
    cout<<ans<<endl;
}

signed main(){
    int T;
    cin>>T;
    rep(i,T)solve(i);
    return 0;
}

