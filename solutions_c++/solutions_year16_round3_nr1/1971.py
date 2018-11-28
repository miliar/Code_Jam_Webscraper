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
    int T,N;
    cin>>T;
    rep(i,T){
        cin>>N;
        vector< pair<int,int> > arr(N);
        int k = 0;
        rep(j,N){
            cin>>arr[j].xx;
            arr[j].yy = j;
            k+=arr[j].xx;
        }
        sort(arr.begin(),arr.end());
        string ans = "";
        while(k){
            sort(arr.begin(),arr.end());
            ans += char(arr[N-1].yy+'A');
            arr[N-1].xx--;
            k--;
            sort(arr.begin(),arr.end());
            if(arr[N-1].xx/(k+0.0) > 0.5){
                ans += char(arr[N-1].yy+'A');
                arr[N-1].xx--;
                k--;
            }
            ans+=" ";
        }
        cout<<"Case #"<<i+1<<": ";
        cout<<ans<<"\n";
    }

    return 0;
}
