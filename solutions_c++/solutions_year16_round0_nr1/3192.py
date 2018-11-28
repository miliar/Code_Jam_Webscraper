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

typedef long long i64;
typedef unsigned long long ui64;

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)


int fx[]={0,0,-1,+1,-1,-1,+1,+1};
int fy[]={-1,+1,0,0,-1,+1,-1,+1};



int main()
{
    READ("in");
    WRITE("out");
    int t,n;
    bool foundDig[10];
    sdi(t);
    rep(i,t) {
        mem(foundDig,false);
        sdi(n);
        if(n==0) {
            printf("Case #%d: INSOMNIA\n",i+1);
            continue;
        }
        int j =1;
        int x;
        string num;
        while(1) {
            x = n*j;
            num = to_string(x);
            rep(k,num.size()) {
                foundDig[num[k]-48] = true;
            }
            if(all_of(begin(foundDig),end(foundDig),[](bool i){return i;})) {
                printf("Case #%d: %d\n",i+1,x);
                break;
            }
            j++;
        }
    }
    return 0;
}