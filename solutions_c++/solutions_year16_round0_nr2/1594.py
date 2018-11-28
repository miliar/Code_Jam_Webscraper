
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <ctime>
#include <iostream>

#include <set>
#include <map>
#include <list>
#include <deque> /* have op [] */
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

#define READ(f)  freopen(f, "r", stdin )
#define WRITE(f) freopen(f, "w", stdout)

#define D(a)      cout << "[ " << #a << " : " << a << " ]"
#define D2(a,b)   cout << "[ " << #a << " : " << a << " , " << #b << " : " << b << " ]" << endl  
#define D3(a,b,c) cout << "[ " << #a << " : " << a << " , " << #b << " : " << b << " , " << #c << " : " << c << " ]" << endl  
#define DL(a)  cout << #a << " : " << a << endl
#define TIME() cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s." << endl

#define FOR(i,a,b) for(int i(a);i<=b;++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i(a);i>=b;--i)

#define ALL(c)    (c).begin(), (c).end()
#define SORT(c)   sort(ALL(c))
#define ZERO(x)   memset(x,0,sizeof x);
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define MAX_I  2147483647
#define MAX_LL 9223372036854775807LL

#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >

template< typename T > bool inside(T a, T b, T c) { return ( a<=b and b<=c ) ; }

int dx[]={ 0, 1, 0,-1, 1, 1,-1,-1 };
int dy[]={ 1, 0,-1, 0,-1, 1, 1,-1 };
//[this,=,&,(&x,&y)](int a , int b )-> int { return } lamda

using namespace std;

typedef long long llint;
typedef pair<int ,int > PII ;
typedef pair<llint ,llint > PLL ;
typedef pair<int ,PII > PIPII ;

const int inf = -1u/2 ; // 1023456789 
const int MOD = 1 ;
const int N   = 0 ;

void rev( char sol[] , int s , int e ){
	//printf("bef : %s->",sol);
	int L = (e-s)+1 ; 
	for(int i=s;i<=e;i++) sol[i] = sol[i] == '+' ? '-' : '+' ;
		
	for(int i=0;i<L/2;i++) swap( sol[s+i] , sol[e-i] ) ; 
	
	return ;

}

int solve( char sol[] , int s , int e ){
	if( s > e ) return 0 ; 
	if( s == e ){
		if( sol[s] == '+' ) return 0 ; 
		return 1 ; 
	} 
	if( sol[e] == '+' ) return solve( sol , s , e-1 ) ; 
	if( sol[e] == '-' ){
		if( sol[s] == '-' ){
			rev( sol , s , e ) ; 
			return 1 + solve( sol , s , e ) ; 
		} else {
			for(int i=s;i<=e;i++){
				if( sol[i] == '-' ) break ;
				sol[i] = '-' ; 
			}
			rev(sol,s,e);
			//printf("ll%s\n",sol);
			return 2 + solve( sol , s , e ) ; 
		}
	}
}

int main(int argc, char const *argv[]){
	
	READ("/Users/JET/Downloads/B-large.in.txt");
	WRITE("/Users/JET/Downloads/B-large.out.txt");
	char in[10000] ; 
	int T ; scanf("%d",&T);
	FOR( i , 1 , T ){ 
		scanf("%s",in);
		//printf("%s\n",in);
		printf("Case #%d: %d\n",i , solve(in,0,strlen(in)-1) ) ;  
	}

	return 0 ;

}
