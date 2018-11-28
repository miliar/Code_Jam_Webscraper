/* Code Jam Template */
#include <bits/stdc++.h>
using namespace std;
#define MOD 					1000000007
#define pb(x) 					push_back(x)
#define mp(x,y)                 make_pair(x,y)
#define FF 						first
#define SS 						second
#define s(n) 					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
//special macro for reading a character of input
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
/*
Use these macros when comparing variables of different data types.
For e.g. comparing int and long long will give error when used with std::max, use maX instead.
*/
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
typedef long long ll;
typedef unsigned long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<ll> vl;
typedef vector<PII> VII;
typedef vector<TRI> VT;

/*Main code begins now*/

void precompute() {
    /*
    Code that is common to all test cases and should be run before solving for any case, like Prime-NUmber Generation :)
    */


}
int n ;
string s;
void read() {
    /*
    Read Global variables here
    */

   cin>>n;

   cin>>s;
}



void solve() {

    /*
    Main logic goes here
    */
    int i ,ans=0,nos=0;
    for(i=0;i<=n;i++)
    {
        if(i<=nos) nos+=s[i]-'0';
        else {
            ans+=(i-nos);
            nos+=(i-nos);
            nos+=(s[i]-'0');
        }
       // cout<<nos<<endl;
    }
    cout<<ans<<endl;
}

int main(){
    freopen("A.in", "r", stdin);
	freopen("output.in", "w", stdout);
	precompute();
	//cout<<primecount[1];
	//cout<<cat[2];
	int t;
	s(t);
   // cout<<t;
	for(int T = 1; T <= t; T++) {
	    read();
	    printf("Case #%d: ",T);
        solve();
  	}
	return 0;
}
