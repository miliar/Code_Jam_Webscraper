/*
  Aditya Gourav
  @adi.pearl
*/
#include<bits/stdc++.h>
using namespace std;

//scanning
#define si(x) scanf("%d",&x)
#define ss(x) scanf("%s",x)
#define ssWSP(x) scanf(" %[^\r\n]",x)
#define sill(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)

//debugging
#define dbm1(msg,x) cerr<<(msg)<<" "<<(x)<<endl;
#define dbm2(msg,x,y) cerr<<(msg)<<" "<<(x)<<" "<<(y)<<endl;
#define dbm3(msg,x,y,z) cerr<<(msg)<<" "<<(x)<<" "<<(y)<<" "<<(z)<<endl;
#define dbm(msg) cerr<<(msg)<<endl;
#define db1(x) cerr<<(x)<<endl;
#define db2(x,y) cerr<<(x)<<" "<<(y)<<endl;
#define db3(x,y,z) cerr<<(x)<<" "<<(y)<<" "<<(z)<<endl;
//others
#define F(i,n) for(int i=0;i <= n-1;++i)
#define F1(i,n) for(int i=1;i <= n;++i)
#define ipArray(arr,size) F(i,size) si(arr[i]);
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T sqr(T x) { return ((x) * (x)); }
const double EPS = 1e-9;
const double BIG = 1e19;
const int INF = INT_MAX;
typedef long long ll;

/* Main Code starts here :) */
int m,n;
string s[100];
vector<int> st[100];
const int mod=1000000007;
int arrng,ans;
inline void solve(int i){
    if(i==m){
        bool f=1;F(j,n)if(st[j].size()==0){f=0;break;}
        if(!f)return;
        int nodes=0;
        F(j,n){
            set<string> se;
            nodes++;
            for(int x: st[j]){
                string str="";
                for(int k=0;k<s[x].size();++k){
                    str+=s[x][k];
                    if(se.find(str)==se.end()){
                        se.insert(str);
                        nodes++;
                    }
                }
            }
        }
        if(nodes>ans){
            ans=nodes;arrng=1;
        }
        else if(nodes==ans)arrng=(arrng+1)%mod;
        return;
    }
    F(j,n){
        st[j].pb(i);
        solve(i+1);
        st[j].pop_back();
    }
}
int main(){
    R("small.in");
    W("small.out");
    int numcases;cin>>numcases;
    for(int case_id=1;case_id<=numcases;++case_id){
        si(m);si(n);
        F(i,m)cin>>s[i];
        arrng=0;ans=INT_MIN;
        solve(0);
        printf("Case #%d: %d %d\n",case_id,ans,arrng);
    }
}
