/*
 * This is my code,
 * my code is amazing...
 */
//Template v3.0 alfa 1 
#include <bits/stdc++.h>
#define ll long long
#define lld long double
#define pll pair<ll,ll>
#define pld pair<lld,lld>
#define vll vector<ll>
#define vvll vector<vll>
#define vpll vector<pll>
#define vvpll vector<vpll>
#define INF 1000000000000000047
const char en='\n';
#define prime 47
#define lprime 1000000000000000009
#define lldmin LDBL_MIN
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define FOR(i,a,b) for(ll i=(ll)(a);i<=(ll)(b);i++)
#define FORD(i,a,b) for(ll i=(ll)(a);i>=(ll)(b);i--)
#define REP(i,b) for(ll i=0;i<(ll)(b);i++)
#define FORE(i,b) for(auto i=(b).begin(); i!=(b).end(); i++)
#define sqr(a) (a)*(a)
#define dst(a,b) sqr((a).ff-(b).ff)+sqr((a).ss-(b).ss)
#define mdst(a,b) abs((a).ff-(b).ff)+abs((a).ss-(b).ss)
//debug
#define debug 1
#define dbg(x) if(debug) cout<<#x<<"="<<(x)<<";"<<endl;
using namespace std;

template <class T, class U>
ostream& operator<<(ostream& out, const pair<T, U>&par) {
  out<<par.ff<<" "<<par.ss<<en;
  return out;
}
template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  REP(i, v.size()){if(i) out<<" ";cout<<v[i];}
  return out;
}







int main(){
	ios::sync_with_stdio(false);

        int T;
        cin>>T;
        FOR(t,1,T){

            ll b,m;
            cin>>b>>m;
            vvll V(b+10,vll(b+10,1));

            cout<<"Case #"<<t<<": ";
            ll p=1LL<<(b-2);
            if(m>p){
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            }
            cout<<"POSSIBLE"<<endl;
            if(m==p){
                REP(i,b){
                    REP(j,b)
                        cout<<1-(i==b-1 || i>=j);
                    cout<<endl;
                }
                continue;
            }
            V[2][b]=0;
            FOR(i,1,b-1){
                if(m%2==0){
                    //cout<<i<<" je 0"<<endl;
                    V[i+1-(i==1)][b]=0;
                }
                m/=2;
            }

            FOR(i,1,b){
                FOR(j,1,b)
                    cout<<(i==b || i>=j? 0 : V[i][j]);
                    cout<<endl;
            }




        }






}
