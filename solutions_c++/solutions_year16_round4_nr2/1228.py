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
  out<<"("<<par.ff<<","<<par.ss<<")";
  return out;
}
template <class T>
ostream& operator<<(ostream& out, const vector<T>& v) {
  REP(i, v.size()){if(i) out<<" ";cout<<v[i];}
  return out;
}







int main(){
	ios::sync_with_stdio(false);
        cin.tie(0);

        int T;
        cin>>T;
        FOR(t,1,T){

            int n,k;
            cin>>n>>k;
            vector<lld> V;
            REP(i,n){
                lld x;
                cin>>x;
                V.PB(x);
            }
            lld naj=0;
            REP(j,(1<<n)){
                int p=j;
                int pocet=0;
                while(p){
                    pocet+=p%2;
                    p/=2;
                }
                if(pocet!=k)continue;
                p=j;
                vector<lld> R;
                REP(i,n){
                    if(p%2==1)
                        R.PB(V[i]);
                    p/=2;
                }
                //cout<<R<<endl;
                vector<vector<lld>> X(k+1,vector<lld>(k+1,0));
                X[0][0]=1;
                FOR(i,1,k){
                    X[i][0]=X[i-1][0]*(1-R[i-1]);
                    FOR(ii,1,k){
                        //X[i][ii] - i ludi, ii hlasov ma danu pst 
                        X[i][ii]=X[i-1][ii]*(1-R[i-1])+X[i-1][ii-1]*R[i-1];
                    }
                }
                naj=max(naj,X[k][k/2]);
            }


            cout<<"Case #"<<t<<": "<<setprecision(10)<<fixed<<naj<<endl;
        }






}
