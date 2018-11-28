/**********************************************
			Author : smiley007	
***********************************************/

//Data Structure Includes
#include <vector>
#include <queue>
#include <deque>
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
#include <cassert>
#include <numeric>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>

using namespace std ;

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
#define PB					push_back
#define MP(x,y)				make_pair(x,y)
#define SET(a,v)			memset(&a[0],v, sizeof(a[0])*SZ(a) )
#define POW2(i)				( 1LL << (i) )
//#define SET(a,i)			a |= POW2(i)
#define CLR(a,i)			a &= ~ POW2(i)
#define TOGGLE(a,i)			a ^= POW2(i)
#define TEST(a,i)			((a) & POW2(i))
#define EPS					1e-9
#define INF					1e9
#define PI 					3.141592653589793
#define MOD 				1000000007

//Typedefs
typedef long long ll ;
typedef pair<int,int> pii ;
typedef pair<string,string> pss ;
typedef vector<int> vi ;
typedef vector<ll> vl ;
typedef vector<vi> vvi ;
typedef vector<vl> vvl ;
typedef vector<bool> vb ;
typedef vector<vb> vvb ;
typedef vector<string> vs ;
typedef vector<pii> vpii ;

//Templates 
//<< ----- Number Theory --- >>
template<class T> bool isPrime(T x){if(x<=1)RE false;T i;for(i=2;i*i<=x;i++)if(x%i==0)RE false;RE true;} //isPrime
template<class T> class Prime{public:vector<T> z ;Prime(){z.resize(1e5+7);REP(i,SZ(z)) z[i]=1;
z[0]=0;z[1]=0;T j;FOR(i,2,SZ(z)){if(z[i]){j=i+i;while(j<SZ(z)){ z[j]=0;j += i ;} } }} }; //Prime

//<< ----- Geometry -------- >>
template<class T> double dist(T x1,T y1,T x2,T y2){RE sqrt( 1.*(x2-x1)*(x2-x1) + 1.*(y2-y1)*(y2-y1) ) ;} //dist
template<class T> class Point{
    public :
    T x, y;
    Point(){}
    Point(T a,T b):x(a),y(b){}
    bool operator ==(const Point& tmp)const{ RE(x==tmp.x && y==tmp.y);}
    Point operator-(const Point& tmp) const{ RE Point<T> (x-tmp.x,y-tmp.y);} 
};

//<<---- Conversions ------- >>
char toLowerCase(char x){RE(x+32);}
char toUpperCase(char x){RE(x-32);}
bool isUpperCase(char x){RE (65<=x && x<=90)? 1 : 0 ;}
bool isLowerCase(char x){RE (97<=x && x<=122)? 1 : 0 ;}
bool isAlpha(char x){RE (isUpperCase(x) || isLowerCase(x))? 1 : 0 ;}
bool isDigit(char x){RE('0'<=x && x<='9')? 1 : 0 ;}
template<class T> T toDec(string s){stringstream is(s);T res;is>>res;RE res;} //toDec
template<class T> string toStr(T n){string s;stringstream is;is<<n;is>>s;RE s;} //toStr


template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}

//Code Begins Here ------ >>>

// Grab your asses fella's , because this code is gonna go deep into you :)


int main(){
	#ifdef LocalHost
		freopen("A-small-attempt2.in","r",stdin);
		freopen("output.txt","w",stdout);
	#endif

	int t,row,i,j,match,test = 1,card;
	cin >> t ;
	vi a(10),b(10);
	vvi mat(10,vi(10));
	while(t--) {
		match = 0;
		cin >> row ;
		for (i = 1; i <= 4; i++)
			for(j = 1; j <= 4; j++)
				cin >> mat[i][j];
		for (j = 1;j <= 4; j++) a[j] = mat[row][j];

		cin >> row ;
		for (i = 1; i <= 4; i++)
			for(j = 1; j <= 4; j++)
				cin >> mat[i][j];
		for (j = 1;j <= 4; j++) b[j] = mat[row][j];

		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++)
				if (a[i] == b[j]) match++,card = a[i];
		cout << "Case #" << test << ":";
		switch(match) {	
			case 0: {
				cout << (" Volunteer cheated!\n");
				break;
			}
			case 1:{
				cout << " " << card << "\n";
				break;
			}
			default: {
				cout << (" Bad magician!\n");
				break;
			}
		}
		test++;
	}
	
	




	


	#ifdef LocalHost
    //cout<<endl<<"Execution time = "<<(float)clock()/CLOCKS_PER_SEC <<" s"<<endl;
	#endif

	RE 0;
}