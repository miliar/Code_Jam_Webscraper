// LANG : C++

#include "cstdio"
#include "cstdlib"
#include "cstring"

#include "ctime"
#include "iostream"

#include "set"
#include "map"
#include "list"
#include "deque"
#include "queue"
#include "stack"
#include "string"
#include "vector"
#include "utility"
#include "algorithm"

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define S(x) (int)x.size()
#define Z(x) memset(x,0,sizeof(x))
#define D(a) cout << "[ " << #a << " : " << a << " ]"<< endl;
#define B(a) (a).begin()
#define E(a) (a).end()
#define A(a) B(a) , E(a)

#define FOR(i, a, b) for (int i(a);i<= b;++i)
#define REP(i, n) FOR(i,0,(n)-1)
#define FORD(i, a, b) for (int i(a);i>=b;--i)

//int dx[]={ 0, 1, 0,-1, 1, 1,-1,-1 };
//int dy[]={ 1, 0,-1, 0,-1, 1, 1,-1 };
//template<typename T> T test( T &a ){ }

using namespace std;

typedef long long llint;
typedef pair<int, int> PII;
typedef vector<int> VI;

//const int INF = 1023456789 ;
//const int size = 0 ;

void solve(){
	static int test_case = 1 ; 
	int a , b , k ; scanf("%d%d%d",&a,&b,&k);
	int sol = 0 ; 
	REP( i , a ) REP( j , b ) sol+=((i&j)<k);
	
	printf("Case #%d: %d\n",test_case,sol);
	test_case++;

}

int main(int argc, char const *argv[]){

	freopen( "1.in", "r",  stdin);
	freopen("1.out", "w", stdout);
	
	int q ; scanf("%d",&q);
	while( q-- > 0 ) solve();
	cerr << endl << "T : " << (double)clock()/(double)CLOCKS_PER_SEC ;
	return 0 ;

}

