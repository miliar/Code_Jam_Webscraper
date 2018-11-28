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

int re(int a, int b){
    if(a==-1 || b==-1 || a==b)
        return -1;
    if(a>b)swap(a,b);

    if(a=='R' && b=='S')return 'R';
    if(a=='P' && b=='S')return 'S';
    if(a=='P' && b=='R')return 'P';
    return -1;
}





int main(){
	ios::sync_with_stdio(false);
        cin.tie(0);

        int T;
        cin>>T;
        FOR(t,1,T){

            int n,r,p,s;
            cin>>n>>r>>p>>s;
            vll V;
            REP(i,r)
                V.PB('R');
            REP(i,p)
                V.PB('P');
            REP(i,s)
                V.PB('S');

            vll res;
            sort(V.begin(),V.end());
            do{
                vll X=V;
                while(X.size()>1){
                    vll XX;
                    //cout<<X.size()<<endl;
                    //cout<<X<<endl;
                    int size=X.size();
                    for(int i=0;i<size; i+=2){
                        XX.PB(re(X[i],X[i+1]));
                    }
                    X=XX;
                    if(X.size()>10)break;
                }
                if(X[0]!=-1){
                    res=V;
                    break;
                }
            }
            while(next_permutation(V.begin(),V.end()));
            

            cout<<"Case #"<<t<<": ";
            if(res.size()==0)cout<<"IMPOSSIBLE"<<endl;
            else{
                REP(i,res.size())
                    cout<<(char)res[i];
                cout<<endl;
            }
        }






}
