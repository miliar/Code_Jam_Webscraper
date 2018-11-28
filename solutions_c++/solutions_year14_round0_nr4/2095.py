//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:16777216")

#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<ctime>
#include<cassert>
#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

#define maxim 100
#define LLD long long int
#define LLU long long unsigned
#define HD short int
#define HU short unsigned
#define ui unsigned
#define pi acos(-1.0)
#define inf (1<<29)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define sz(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define eps 1e-9
#define rep(i,init,n) for(i=init;i<n;i++)
#define rem(i,init,n) for(i=init;i>n;i--)
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define _abs(a) ((a)<0?(-(a)):(a))
#define area(x1,y1,x2,y2,x3,y3) ( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )
#define sqr(x) ((x)*(x))
#define distSqr(x1,y1,x2,y2) ( sqr(x1-x2) + sqr(y1-y2) )
#define spDist(lat1,long1,lat2,long2,r) ( r * acos( sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1-long2) ) )
#define isEq(a,b) (fabs(a-b)<eps)
#define STR string
#define LF double
#define IT iterator
#define VI vector<int>
#define VLLD vector<LLD>
#define VS vector<STR>
#define VLF vector<LF>
#define MII map<int,int>
#define MIB map<int,bool>
#define MSI map<STR,int>
#define MSB map<STR,bool>
#define MSS map<STR,STR>
#define M2dII map<int,map<int,int> >
#define QI queue<int>
#define SI stack<int>
#define PII pair< int, int >
#define PPI pair< PII, int >
#define ff first
#define ss second
#define VPII vector<PII>
#define MP make_pair

#define chk(a,k) ((bool)(a&(1<<(k))))
#define set0(a,k) (a&(~(1<<(k))))
#define set1(a,k) (a|(1<<(k)))

#define chkA(a,k) (bool)(a[(k)>>5] & (1<<((k)&31)))
#define setA0(a,k) (a[(k)>>5] &= ~(1<<((k)&31)))
#define setA1(a,k) (a[(k)>>5] |= (1<<((k)&31)))

#define SD(a) scanf("%d",&a)
#define SU(a) scanf("%u",&a)
#define SHD(a) scanf("%hd",&a)
#define SHU(a) scanf("%hu",&a)
#define SLLD(a) scanf("%lld",&a)
#define SLLU(a) scanf("%llu",&a)
#define SF(a) scanf("%f",&a)
#define SLF(a) scanf("%lf",&a)
#define SC(a) scanf("%c",&a)
#define SS(a) scanf("%s",a)

int diru[] = {-1,-1,-1,0,0,1,1,1};
int dirv[] = {-1,0,1,-1,1,-1,0,1};

using namespace std;

#define DEB(args...) (Debugger()) , args
class Debugger{ public: Debugger(const string& _separator = " "): first(true), separator(_separator){} template<typename ObjectType>Debugger& operator , (const ObjectType& v) { if(!first) cerr << separator; cerr << v; first = false; return *this; } ~Debugger() { cerr << endl; } private: bool first; string separator; }; template <typename T1, typename T2> inline ostream& operator << (ostream& os, const pair<T1, T2>& p) { return os << "(" << p.first << "," << p.second << ")"; } template<typename T> inline ostream &operator << (ostream & os,const vector<T>& v) { bool first = true; os << "{"; for(unsigned int i = 0;i < v.size();i++){ if(!first) os << ","; os << v[i]; first = false; } return os << "}"; } template<typename T> inline ostream &operator << (ostream & os,const set<T>& v) { bool first = true; os << "{"; for (typename set<T>::const_iterator ii = v.begin();ii != v.end();++ii) { if(!first) os << ","; os << *ii; first = false; } return os << "}"; } template<typename T1, typename T2> inline ostream &operator << (ostream & os,const map<T1, T2>& v) { bool first = true; os << "{"; for (typename map<T1, T2>::const_iterator ii = v.begin();ii != v.end();++ii) { if(!first) os << ","; os << *ii ; first = false; } return os << "}"; }

template< class T > T sq(T n) { return n*n; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template< class T > T power(T N,T P){  return (P==0)?  1: N*power(N,P-1); }

VLF A,B,a,b ;
int n ;

int war()
{
    A = a ;
    B = b ;

    int ret = 0,i,j ;

    rem(i,n-1,-1)
    {
        rep(j,0,n)
        {
            if(B[j]<0)      continue ;

            if(B[j]>A[i])
            {
                B[j] = -1 ;
                break ;
            }
        }

        if(j==n)
        {
            rep(j,0,n)
            {
                if(B[j]<0)      continue ;

                B[j] = -1 ;

                ret ++ ;

                break ;
            }
        }
    }

    return ret ;
}

int dct()
{
    A = a ;
    B = b ;

    int m = n, ret = 0,i,j ;

    while(m--)
    {
        rem(j,n-1,-1)
        {
            if(B[j]<0)      continue ;
            break ;
        }

        rep(i,0,n)
        {
            if(A[i]<0)      continue ;

            if(A[i] > B[j])
            {
                ret ++ ;

                A[i] = -1 ;
                B[j] = -1 ;

                break ;
            }
        }

        if(i==n)
        {
            rep(i,0,n)
            {
                if(A[i]<0)      continue ;

                A[i] = -1 ;
                B[j] = -1 ;

                break ;
            }
        }
    }

    return ret ;
}

int main()
{
	int T,t=1,m,i,j,k;
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	//while(scanf("%d",&n)==1)
	{
        SD(n) ;

        a.clear() ;
        b.clear() ;

        a.resize(n) ;
        b.resize(n) ;

		rep(i,0,n)      scanf("%lf",&a[i]) ;
		rep(i,0,n)      scanf("%lf",&b[i]) ;

		sort(all(a)) ;
		sort(all(b)) ;

		//DEB(a) ;
		//DEB(b) ;

		int ansW = 0 ;
		int ansD = 0 ;

        ansW  = war() ;
        ansD = dct() ;

		printf("Case #%d: %d %d\n",t,ansD,ansW) ;
	}
	return 0;
}
