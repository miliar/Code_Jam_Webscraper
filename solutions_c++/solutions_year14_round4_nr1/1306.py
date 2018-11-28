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
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return ((x) * (x)); }
const double EPS = 1e-9;
const double BIG = 1e19;
const int INF = INT_MAX;
typedef long long ll;

/* Main Code starts here :) */
int s[10000+10];
int main(){
    R("large.in");
    W("large.out");
    int numcases;cin>>numcases;
    for(int case_id=1;case_id<=numcases;++case_id){
        int n,x;
        si(n);si(x);
        ipArray(s,n);
        sort(s,s+n);
        int i=0,j=n-1;
        int ans=0;
        while(j>=i){
            if(i==j){ans++;j--;}
            else if(s[j]+s[i]<=x){j--;i++;ans++;}
            else{
                j--;ans++;
            }
        }

        printf("Case #%d: %d\n",case_id,ans);
    }
}
