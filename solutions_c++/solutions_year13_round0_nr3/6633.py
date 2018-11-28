/**********************************************
			Author : smiley007	
***********************************************/

//Data Structure Includes
#include <vector>
#include <queue>
#include <bitset>
#include <stack>
#include <list>
#include <set>			
#include <map>

//Other Includes
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>

using namespace std;

//Defines
#define FOR(i,a,b)         	for(int i = (a); i <  (b) ; i++)
#define FOE(i,a,b)         	for(int i = (a); i <= (b) ; i++)
#define FOED(i,a,b)			for(int i = (a); i >= (b) ; i--)
#define ITR(v,it) 			for( typeof(v.begin()) it=v.begin();it!=v.end();it++)
#define REP(i,n)			FOR(i,0,n)
#define ALL(a) 				a.begin(),a.end()
#define SORT(a) 			sort(ALL(a))
#define SZ(a)				((int)a.size())
#define SQR(x)				((x)*(x))
#define BS(i) 				__builtin_popcount(i)
#define LZ(i)				__clz
#define RE 					return
#define FI 					first
#define SD 					second
#define P 					printf
#define S 					scanf
#define PB					push_back
#define MP(x,y)				make_pair(x,y)
//#define SET(a,v)			memset(&a[0],v, sizeof(a[0])*SZ(a) )
#define POW2(i)				( 1LL << (i) )
#define SET(a,i)			a |= POW2(i)
#define CLR(a,i)			a &= ~ POW2(i)
#define TOGGLE(a,i)			a ^= POW2(i)
#define TEST(a,i)			((a) & POW2(i))
#define EPS					1e-9
#define INF					1e9
#define PI 					3.141592653589793
#define MOD 				1000000007

//Typedefs
typedef char C ;
typedef int I ;
typedef double D ;
typedef long long LL ;
typedef pair<I,I> PII ;
typedef pair<LL,LL> PLL ;
typedef pair<string,string> PSS ;
typedef vector<I> VI ;
typedef vector<LL> VL ;
typedef vector<VI> VVI ;
typedef vector<VL> VVL ;
typedef vector<string> VS ;
typedef vector<PII> VPII ;
typedef vector<PLL> VPLL ;

//Templates 
//<< ----- Number Theory --- >>
template<class T> bool isPrime(T x){if(x<=1)RE false;T i;for(i=2;i*i<=x;i++)if(x%i==0)RE false;RE true;} //isPrime
template<class T> class Prime{public:vector<T> z ;Prime(){z.resize(1e5+7);REP(i,SZ(z)) z[i]=1;
z[0]=0;z[1]=0;T j;FOR(i,2,SZ(z)){if(z[i]){j=i+i;while(j<SZ(z)){ z[j]=0;j += i ;} } }} }; //Prime

//<< ----- Geometry -------- >>
template<class T> D dist(T x1,T y1,T x2,T y2){RE sqrt( 1.*(x2-x1)*(x2-x1) + 1.*(y2-y1)*(y2-y1) ) ;} //dist
template<class T> class Point{
    public :
    T x, y;
    Point(){}
    Point(T a,T b):x(a),y(b){}
    bool operator ==(const Point& tmp)const{ RE(x==tmp.x && y==tmp.y);}
    Point operator-(const Point& tmp) const{ RE Point<T> (x-tmp.x,y-tmp.y);} 
};

//<<---- Conversions ------- >>
C toLowerCase(C x){RE(x+32);}
C toUpperCase(C x){RE(x-32);}
bool isUpperCase(C x){RE (65<=x && x<=90)? 1 : 0 ;}
bool isLowerCase(C x){RE (97<=x && x<=122)? 1 : 0 ;}
bool isAlpha(C x){RE (isUpperCase(x) || isLowerCase(x))? 1 : 0 ;}
bool isDigit(C x){RE('0'<=x && x<='9')? 1 : 0 ;}
template<class T> T toDec(string s){stringstream is(s);T res;is>>res;RE res;} //toDec
template<class T> string toStr(T n){string s;stringstream is;is<<n;is>>s;RE s;} //toStr


template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}

//Code Begins Here ------ >>>
bool isPalin(I x){
	string s = toStr<I>(x) ;
	I l,r;
	l = 0 ;
	r = SZ(s) - 1 ;
	while(l<r){
		if(s[l]!=s[r]) RE false ;
		l++;r--;
	}
	RE true ;
}

I main(){
	#ifdef LocalHost
		freopen("C-small-attempt0.in","r",stdin);
		freopen("output.txt","w",stdout);
	#endif

	I t,k,a,b,l,r,tot ;
	cin >> t ;
	k = 1 ;
	while(k <= t){
		cin >> a >> b ;
		l = sqrt(a) ;
		if(SQR(l) != a) l++ ;
		r = sqrt(b) ;
		tot = 0 ;
		FOE(j,l,r){
			if( isPalin(j) && isPalin(SQR(j)) ) tot++ ;
		}
		cout << "Case #" << k << ": " << tot << "\n" ;
		k++ ;
	}

	RE 0;
}