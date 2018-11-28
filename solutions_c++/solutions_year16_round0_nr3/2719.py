/* sjsakib  */ 
#include <bits/stdc++.h>

#define stream istringstream
#define rep(i,n) for(int i=0; i<(int)n; i++)
#define repv(i,n) for(int i=n-1; i>=0; i--)
#define repl(i,n) for(int i=1; i<=(int)n; i++)
#define replv(i,n) for(int i=n; i>=1; i--)


#define INF (1<<28)
#define PI 3.141592653589793238462643383279502
#define pb(x) push_back(x)
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define mem(x,y) memset(x,y,sizeof(x))
#define eps 1e-9
#define pii pair<int,int>
#define vi vector<int>
#define pmp make_pair


#define sdi(x) scanf("%d",&x)
#define sdii(x,y) scanf("%d%d",&x,&y)
#define sdc(x) scanf("%c",&x)
#define SDs(x) scanf("%s",x)
#define uu first
#define vv second

using namespace std;

template<class T> inline T gcd(T a,T b) {if(a<0)return 
gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return 
lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T sqr(T x){return x*x;}
template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }

typedef long long i64  ;
typedef unsigned long long ui64  ;

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)


int fx[]={0,0,-1,+1,-1,-1,+1,+1};
int fy[]={-1,+1,0,0,-1,+1,-1,+1};


i64 toBase(string s,int b) {
    i64   n = 0;
    for(int i = s.size()-1,j = 0;i>=0;i--,j++) {
        n+=(s[i]-48)*pow(b,j);
    }
    return n;
}
i64 getDiv(i64   n) {
    i64   rt = sqrt(n);
    for(i64  i = 2;i<=rt;i++) {
        if(n%i==0) {
            return i;
        }
    }
    return -1;
}



int main() {
    READ("in");
    WRITE("out");
    int j = 0;
    string jc;
    vi divisors;
    cout<<"Case #1:\n";
    rep(i,3) {
        while(1) {
            jc = "1"+bitset<4>(j++).to_string()+"1";
            //cout<<jc<<' ';
            for(int k= 2;k<=10;k++) {
                i64  n = toBase(jc,k);
                i64  d = getDiv(n);
                cout<<n<<' '<<d<<endl;
                if(d == -1) {
                    break;
                } else {
                    divisors.push_back(d);
                }
            }
            if(divisors.size() == 9 ){
                break;
            } else {
                divisors.clear();
            }
        }
        cout<<jc;
        rep(k,divisors.size()) {
            cout<<" "<<divisors[k];
        }
        cout<<endl;
        divisors.clear();
    }
    return 0;
}