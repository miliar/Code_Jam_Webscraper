# include<bits/stdc++.h>
using namespace std;

# define FOR(i,a,b) for(int i=int(a);i<=int(b);i++)
# define FORn(i,a,b) for(int i=int(a);i>=(b);i--)
# define rep(i,a)   FOR(i,0,a-1)
# define repn(i,a)  FORn(i,a-1,0)
# define ALL(x) x.begin(),x.end()
# define MAX(a,b) (a)>(b)?(a):(b)
# define MIN(a,b) (a)<(b)?(a):(b)
# define xx first
# define yy second
# define S(x) scanf("%d",&x)
# define SL(x) scanf("%I64d",&x);
# define S2(x,y) scanf("%d%d",&x,&y)
# define P(x)	printf("%d\n",x)
# define PL(x) printf("%I64d\n",x);
# define pb	push_back
# define _ ios_base::sync_with_stdio(0);cin.tie(0);
# define sz(x) int((x).size())
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=c.end();i++)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef map<int,int> mii;
typedef multimap<int,int> mmii;


const double pi=acos(-1);
const int md=1e9+7;

inline ll power(ll a, ll n) {ll p = 1;while (n > 0) {if(n%2) {p = p * a;} n >>= 1; a *= a;} return p;}
ll gcd (ll a, ll b) {return ( a ? gcd(b%a, a) : b );}


int main(){
    freopen("AL.in","r",stdin);
    freopen("AL.out","w",stdout);
    int N,T;
    scanf("%d",&T);
    rep(tc,T){
        scanf("%d",&N);
        printf("Case #%d: ",tc+1);
        int tmp = 0 , i=0,X;
        if(!N){
            printf("INSOMNIA\n");
            continue;
        }
        while(tmp != (1<<10)-1){
            i++;
            X = N * i;
            while(X){
                tmp |= 1<<(X%10);
                X /= 10;
            }
        }
        if(tmp==(1<<10)-1)
            printf("%d\n",N * i);

    }

    return 0;
}
