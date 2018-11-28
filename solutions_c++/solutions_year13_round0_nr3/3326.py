#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

// Input
#define s(n)					scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)

// Constants
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9

// Functions
#define maX(a,b)                ( (a) > (b) ? (a) : (b))
#define miN(a,b)                ( (a) < (b) ? (a) : (b))
#define abS(x)					( (x) < 0 ? -(x) : (x))
#define checkbit(n,b)           ( (n >> b) & 1)
#define DREP(a)                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)          (lower_bound(all(arr),ind)-arr.begin())

// Traversal
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define foreach(v,c)			for(typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)

// Container
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back

// Debugger
#define debug(args...)			{dbg,args; cerr<<endl;}
#define dline					cerr<<endl

struct debugger{
	template<typename T> debugger& operator , (const T& v){	
		cerr<<v<<" ";
		return *this;
	}
} dbg;

// Typedef
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;

LL limit = 1e15;
VL squares;

bool is_palindrome(LL n){
	int num = n, digit;
	LL rev = 0;

	while(num){
	    digit = num%10;
	    rev = (rev*10) + digit;
	    num /= 10;
    }

    if(rev == n){
    	return true;
    }
    return false;
}

void initiate_squares(){
	LL n = 1, square = 1, root;
	while(square <= limit){
		square = n * n;
		root = sqrt(square);
		if(is_palindrome(square) && is_palindrome(root)){
			squares.pb(square);
		}
		n++;
	}
}

int main(){
	// initiate_squares();
	// printf("LL s[%d] = {", SZ(squares));
	// REP(i,SZ(squares)-1){
	// 	printf("%lld, ", squares[i]);
	// }
	// printf("%lld};\n", squares[SZ(squares)-1]);

	int tc, start, end, i;
	LL s[21] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404};
	LL a, b;

	s(tc);

	REP(case_no,tc){
		sl(a); sl(b);

		i = 0;
		while(s[i] < a && i < 21) i++;
		start = i;

		while(i < 21){
			if(s[i] > b){
				break;
			}
			i++;
		}
		end = i;

		printf("Case #%d: %d\n", case_no+1, end-start);
	}
	return 0;
}
