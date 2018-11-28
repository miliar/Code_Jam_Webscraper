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

int main()
{
    Read("D-small-attempt1.in");
    Write("D-small-attempt0.out");

    ios_base::sync_with_stdio(0); cin.tie(0);

	int t,c,k,s;

	cin >> t;

	for(int cases = 1;cases <= t;cases++){

		cin >> k >> c >> s;

		cout << "Case #" << cases << ": ";

		if(c == 1 && s >= k){

			for(int i = 1;i < k;i++)cout << i << ' ';
			cout << k << endl;
		}
		else if(c > 1 && s >= k-1){

            for(int i = 2;i < k;i++)cout << i << ' ';
            cout << k << endl;
		}
		else cout << "IMPOSSIBLE" << endl;
	}

    return 0;
}

