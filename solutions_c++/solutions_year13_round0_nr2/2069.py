//#pragma warning(disable:4786)
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include<deque>
#include<numeric>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>

#include<assert.h>
#include<math.h> 
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

/*
#define lli __int64
#define llu unsigned __int64
*/

#define lli  long long
#define llu  unsigned long long
#define uint unsigned int

typedef pair<int,int> pi;
typedef pair<double,double> pd ;
typedef set<int>       si;
typedef vector<bool>   vb;
typedef vector<int>    vi;
typedef vector<lli>    vli;
typedef vector<llu>    vlu;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<pi>    vpi;
typedef vector<pd>    vpd;
typedef map<int,int>    mii ;
typedef map<string,int> msi ;
typedef map<int,string> mis ;

//#define iter(tp,it) tp::iterator it
#define iter ::iterator
#define stend string::npos
#define powr(a,b) pow((double)(a), (double)(b))
#define inf (1<<30)
#define eps 1e-9
#define py (2.0*acos(0.0))
#define torad (py/180.0)
#define mpa make_pair
#define istr istringstream
#define ostr ostringstream
#define S(x) ((x)*(x))

#define zero(x) (fabs(x)<eps)
#define eq(a,b) (fabs(a-b)<eps)
#define bet(x,a,b) ((x>=a)&&(x<=b))


// for long 1LL<<45 ... 
#define lsh(i) (1<<i)
#define chkb(mask,i)  ((mask)&(1<<i))

#define setb(mask,i)  ((mask)|=(1<<i))
#define clrb(mask,i)  ((mask)&=~(1<<i))
#define setbr(mask,i) ((mask)|(1<<i))
#define clrbr(mask,i) ((mask)&=~(1<<i))


#define has(a,b)    ((a).find(b)!=(a).end())
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))

#define all(x) (x).begin(),(x).end()
#define fr(i,a,b)   for (i = (a); i <= (b); i++)
#define frr(i,a,b)  for (i = (a); i >= (b); i--)
#define rep(i,a,b)  for (i = (a); i <  (b); i++)
#define repr(i,a,b) for (i = (a); i >  (b); i--)

#define fi(i,b) rep(i,0,b)

const int month[] = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

#define in(a)  freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)

/* desnot work in visual c++ 
#define cnttz(mask) __builtin_ctz(mask)
#define cntlz(mask) __builtin_clz(mask)
#define cntb(mask)  __builtin_popcount(mask)
*/
template<class T> int cntb( T i){ int ret=0 ; while(i)i=(i-1)&i ,      ret++;return ret;}
template<class T> int cntlz(T i){ int ret=0 ; while(!chkb(i,0)&&i)i/=2,ret++;return ret;}

template<class T> T gcd(T a, T b){ return (b==0)? a: gcd(b,a%b);}
template<class T> void frstring(string s , T &r){ r = 0 ; istr ci(s); ci>>r ; }
template<class T> string tostring(T n){ ostr co; co<<n ; co.flush(); return co.str();}

template<class T> T bigmod( T x, T n ,T m) { 
   T ret=1; 
   while(n>0){ 
	   if(n%2==1) ret = (ret*x)%m ;
	   x=(x*x)%m;  n/=2; }
   return ret ;
}


struct gb{
   
	int  x , i , j ;

	bool operator< ( gb nn ){
	    return (x<nn.x) ;

	}

} ;



int ar[105][105] ;
int t , cs ;
int N , M ;

vector<gb> st ;

bool upd( int x , int y ){
 
	if(ar[x][y]== -1) return true ;
    bool flag = 0 ;
	
	int i , j , k ;

	bool fl = 1 ;
    rep(i , 0 , M ){
	    if(ar[x][i]!=ar[x][y] && ar[x][i]!=-1)
			fl = 0;
	}

	if(fl){
	   
		flag = 1 ;
		rep(i , 0 , M ){
		   ar[x][i]=-1;
		}
	
	}


	fl = 1 ;

	rep(i , 0 , N ){
	    if(ar[i][y]!=ar[x][y] && ar[i][y]!=-1)
			fl = 0;
	}

	if(fl){
	   
		flag = 1 ;
		rep(i , 0 , N ){
		   ar[i][y]=-1;
		}
	
	}



  return flag ;

}

int main(){
#ifndef ONLINE_JUDGE
  in("1.txt");
  out("3.txt");
#endif


   
 int i,j,k ;
 int a,b,c ;

 cin>>t ;

 while(t--){
	 
	 st.clear() ;
     scanf("%d %d", &N , &M );

	 rep(i , 0 , N ){
	    
		 rep(j , 0 , M ){

			 scanf("%d",&ar[i][j]);
	         gb f ;
			 f.x = ar[i][j] ;
			 f.i = i ; f.j = j ;
			 st.push_back(f) ;
		 }
	 }

     sort(all(st));


	 bool flag = true ;

	 rep( i , 0 , st.size() ){
	    
		 int x , y ;

		 x = st[i].i ;
		 y = st[i].j ;

		 flag = upd(x , y) ;

		 if(flag==0) break ;
	 
	 
	 }

 
	 printf("Case #%d: ", ++cs );

	 if(flag)
		 printf("YES\n");
	 else
		 printf("NO\n");
 }


return 0 ;
}
