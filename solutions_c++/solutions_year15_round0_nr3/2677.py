// LANG : C++

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <ctime>
#include <iostream>

#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

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

const int INF = -1u/2 ; // 1023456789 
const int SIZE = 0 ;
const int MOD = 1 ;
// i = 2 
// j = 3 
// k = 4 

int sol[5][5];

int cal( int a , int b ){

	int t = 1 ;
	if( a < 0 )t*=-1;
	if( b < 0 )t*=-1;
	sol[1][1] = 1 ; sol[1][2] =  2 ; sol[1][3] =  3 ; sol[1][4] =  4 ;
	sol[2][1] = 2 ; sol[2][2] = -1 ; sol[2][3] =  4 ; sol[2][4] = -3 ;
	sol[3][1] = 3 ; sol[3][2] = -4 ; sol[3][3] = -1 ; sol[3][4] =  2 ;
	sol[4][1] = 4 ; sol[4][2] =  3 ; sol[4][3] = -2 ; sol[4][4] = -1 ;
	return sol[ abs(a) ][ abs(b) ]*t ;
}

char in[100004];

void solve(){

	static int a = 1 ;
	printf("Case #%d: ",a++);

	int l , x ; scanf("%d%d",&l,&x);
	int ff = 99999999, ee = -9999999 ;
	// vector< int > f ;
	// vector< int > e ; 
	scanf("%s",in);
	if( l*x < 3 ) {
		printf("NO\n"); 
		return ;
	}
	int t = 1 ; int h = 1 ; 
	for(int i=0;i<l*x;i++){
		int has = in[i%l] == 'i' ? 2 : in[i%l] == 'j' ? 3 : 4 ;
		h = cal( h , has ) ;
	}

	for(int i=0;i<l*x;i++){
		int has = in[i%l] == 'i' ? 2 : in[i%l] == 'j' ? 3 : 4 ;
		t = cal( t , has ) ;
		if( t == 2 ){ ff = i ; break ; } //f.push_back( i ) ;  
	} 
	t = 1 ; 
	for(int i=(l*x)-1;i>=0;i--){
		int has = in[i%l] == 'i' ? 2 : in[i%l] == 'j' ? 3 : 4 ;

		t = cal( has , t ) ; 
		if( t == 4 ){ ee = i ; break ; } //e.push_back( i ) ;  
	} 
	if( h == -1 && ff < ee ){
		printf("YES\n");
	} else {
		printf("NO\n"); 
		return ;
	}

}

int main(int argc, char const *argv[]){

	 freopen("C-small-attempt2.in", "r",  stdin);
	 freopen("outC-small-attempt2.txt", "w", stdout);
	int T ; scanf("%d",&T);

	while( T-- ) solve() ; 	

	return 0 ;

}
