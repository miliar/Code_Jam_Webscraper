/*
ID: Asif Jawad
LANG: C++
TASK:
*/

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <iterator>
#include <utility>
#include <sstream>

using namespace std;

#define Read(f) freopen(f,"r",stdin)
#define Write(f) freopen(f,"w",stdout)

#define geti(n) scanf("%d",&n)
#define getll(n) scanf("%lld",&n)
#define getf(n) scanf("%lf",&n);

#define pi acos(-1)
#define eps 1e-9
#define mem(a,n) memset(a,n,sizeof a)
#define countbit(x) __builtin_popcountll(x)

#define rep(i,n) for(int i = 0;i < n;i++)
#define Rep(i,a,n) for(int i = (a) ;i < n;i++)
#define REP(i,a,n) for(int i = (a); i >= n;i--)

#define pb push_back
#define sz size()
#define mp make_pair
#define all(c) (c).begin(),(c).end()
//#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ( (c).find(x) != (c).end() )
#define cpresent(c,x) ( find(all(c),x) != (c).end() )
#define ff first
#define ss second

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector< vi >vvi;

inline int Set(int N,int pos)
{
    return N = N | (1 << pos);
}
inline int Reset(int N,int pos)
{
    return N = N & ~ (1 <<pos);
}
inline bool check(int N,int pos)
{
    return (bool) (N & (1 << pos) );
}

template<class T>
T gcd(T a,T b)
{
    return (!b) ? a : gcd( b, a%b );
}

template <class T>
T lcm(T a,T b)
{
    return (a / gcd(a,b)) * b;
}

template<class T>
bool is_prime(T n)
{
    if( (n % 2 == 0 && n > 2) || n < 2 )return 0;

    for( T i = 3; i * i <= n ; i = i + 2 )
    {

        if( n % i == 0 )return 0;
    }
    return 1;
}

//template ends here

vector<string> v;

void call(int i,string w)
{
	if(i == 15){

		v.pb("1"+w+"1");
		return;
	}
	call(i+1,w + "0");
	call(i+1,w + "1");
}

string s[] = {"0","1","2","3","4","5","6","7","8","9"};

ll conv(string t,ll b)
{
	//cout << t << endl;

	ll nn=0,g=1;

	rep(i,t.sz-1)g*=(ll)b;

	for(int i = 0;i < t.sz;i++){

		nn += (g*(ll)(t[i]-'0'));
		g /= b;
	}
	//cout<< nn << endl;
	return nn;
}

int main()
{
    Read("C-small-attempt0.in");
    Write("C-small-attempt0.out");

    ios_base::sync_with_stdio(0); cin.tie(0);
	

	//conv("1001",6);

	int c=0,t,p,q;

	cin >> t;

	cin >> p >> q;

	call(1,"");

	cout << "Case #1:" << endl;

	rep(i,v.sz){

		vector<ll> t;

		for(ll b = 2;b <= 10;b++){

			ll n = conv(v[i],b);

			if(n%2LL == 0){
				
				t.pb(2);
				continue;
			}

			for(ll p = 3;p * p <= 100;p+= 2){

				if(n%p == 0){

					t.pb(p);
					break;
				}
			}
		}
		if(t.sz == 9){

			cout << v[i];

			rep(i,t.sz)cout << ' ' << t[i];

			cout << endl;

			c++;
		}
		if(c==q)break;
	}
    return 0;
}

