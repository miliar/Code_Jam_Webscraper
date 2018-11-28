
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
int cc = 0 , CC = 0 ;
int in[10000] ; 
vector<int> prime ; 
int pMod(int a, int n, int m){

    int res = 1;
    a = a % m;  
    while (n > 0){
        if (n & 1) res = (res*a) % m;
        n /= 2 ;
        a = (a*a) % m;  
    }
    return res;
}

int isP( int sol[] , int base , int l ){
	// for(int i=l-1;i>=0;i--) printf("%d",sol[i]);
	for(int i=0;i<prime.size();i++){
		
		int R = 1 ; 
		for(int j=1;j<l;j++){
			if( sol[j] == 1 ){
				R += pMod( base , j , prime[i] ) ;
				R %= prime[i] ; 
			}
			// if( base == 2 ) printf("[%d]",R);
		}

		if( R == 0 ) return prime[i] ; 
	}
	return -1 ; 
}

void recur( int sol[] , int level , int l ){
	if( cc == CC ) return ;
	if( level == 0 ){
		sol[level] = 1 ; 
		recur( sol , level+1 , l ) ; 
	} 
	if( level == l-1 ){
		sol[level] = 1 ;
		int ans[12] ; 
		bool isC = true ; 
		for(int i=2;i<=10;i++){
			ans[i] = isP( sol , i , l );
			if( ans[i] == -1 ){
				isC = false ; 
				break ; 
			}
		}
		if( isC ){ 
			cc++ ; 
			for(int i=l-1;i>=0;i--) printf("%d",sol[i]);
			printf(" ");
			for(int i=2;i<=10;i++){
				int kk = 0 ; 
				for(int j=l-1;j>=0;j--){
					kk *=i ;
					if( sol[j] == 1 ) kk += 1 ;
				} 
				 // printf("%d:",kk);
				printf("%d ",ans[i]);
			}
			printf("\n");
		}

		return ;
	
	}
	sol[level] = 0 ; 
	recur( sol , level+1 , l ) ; 
	sol[level] = 1 ; 
	recur( sol , level+1 , l ) ; 

}

void genP(){
	const int NP = 1<<20 ; 
	int a[NP] ;
	memset( a , 0 , sizeof(a) ) ;
	for(int i=2;i*i<NP;i++){
		if( a[i] == 0 ){
			for(int j=i*i;j<NP;j+=i){
				a[j] = 1 ; 
			}
		}
	}
	for(int i=2;i*i<NP;i++) 
		if( a[i] == 0 )
			prime.push_back( i ) ;
	return ;
}

int main(int argc, char const *argv[]){
	READ("/Users/JET/Downloads/C-large.in.txt");
	WRITE("/Users/JET/Downloads/C-large.out.txt");
	genP();
	// cerr << "complete genP " ; 
	int t , n , j ; 
	scanf("%d%d%d",&t,&n,&j);
	CC = j ; 
	printf("Case #1:\n");
	recur( in , 0 , n );
	// cerr << cc ;
	return 0 ;

}
