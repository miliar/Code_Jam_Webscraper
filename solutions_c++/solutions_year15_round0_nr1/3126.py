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
#define linf 123456789999999990
#define iinf 1234567890
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
#define tr(c,i) for(typeof( (c).begin() ) i = (c).begin();i != (c).end();i++)
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
    return (a % b == 0) ? b : gcd( b, a%b );
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

string s;
int ara[1010];

int main()
{
    Read(".in");
    Write("ans.out");
	
	int t,sm;

	cin >> t;

	Rep(cases,1,t+1){
		
		cin >> sm;
		
		cin.ignore();
		
		cin >> s;
		
		rep(i,s.sz)ara[i] = s[i] - '0';

		int ans = 0,st = 0;

		Rep(i,1,s.sz){
			
			if(st + ara[i-1] >= i){
				
				st+= ara[i-1];
			}
			else {
				
				ans += (i - (st + ara[i-1]));
				st += (i - st);
			}
		}
		printf("Case #%d: %d\n",cases,ans);
	}

    return 0;
}

