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

const int INF = 1023456789 ;
const int size = 102 ;

void solve(){
    static int test_case = 1 ;
    int n ; scanf("%d",&n);
    char in[size] ; vector<pair<char ,int> > path[size] ;
    bool loss = false ;
    REP( i , n ){
        scanf("%s",in);
        int len = strlen( in ) ;
        for(int j=0;j<len&&!loss;){
            int d = 0 ;
            while( j+d < len && in[j] == in[j+d] ) d++ ;
            path[i].PB( MP( in[j] , j+d == len ? d :d+1) );
            if( i!= 0 && path[0][ S(path[i])-1 ].ST != path[i][ S(path[i])-1 ].ST )
                loss = true ;
            j+=d ;
        }
        if( S( path[0] ) != S( path[i] ) ) loss = true ;
        if( loss ) break ;
    }
    int ans = 0 ;
    if( !loss ){
        //REP( i , S(path[0]) )
          //  ans += abs( path[0][i].ND-path[1][i].ND ) ;
        REP( i , S(path[0]) ){
            int sol = INF ;
            FOR( j , 1 , 100 ){
                int kk = 0 ;
                REP( k , n )kk += abs( path[k][i].ND-j ) ;
                sol = min( sol , kk ) ;
            }
            ans += sol ;
        }
    }

    if( !loss ) printf("Case #%d: %d\n",test_case,ans);
    else printf("Case #%d: Fegla Won\n",test_case);
    test_case++ ;
}

int main(int argc, char const *argv[]){

	freopen( "A-small-attempt4.in", "r",  stdin);
	freopen("A-small-attempt4.out", "w", stdout);

	int l ; scanf("%d",&l);
	while( l-- > 0 ) solve() ;

	cerr << endl << "T : " << (double)clock()/(double)CLOCKS_PER_SEC ;
	return 0 ;

}
