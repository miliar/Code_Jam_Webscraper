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

char sol[1005] ; 

void solve(){

	static int t = 1 ; 
	int n ; scanf("%d %s",&n,sol);

	int sum = 0 ; int adj = 0 ;
	FOR( i , 0 , n ){ 
		if( sum+adj < i ){
			adj += (i-(sum+adj));
		}
		sum += sol[i]-'0' ;
	}

	printf("Case #%d: %d\n",t++,adj);
	return ; 
}

int main(int argc, char const *argv[]){

	freopen("A-large.in", "r",  stdin);
	freopen("outA-large.txt", "w", stdout);
	
	int T ; scanf("%d",&T);

	while( T-- ) solve() ; 	
	

	//cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s." << endl;
	return 0 ;

}
