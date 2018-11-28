//In the name of Allah
//
//
//////////////////////
// Program: 
// Written By Alireza Farhadi (LGM)
//////////////////////
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <map>
//#include <climits>
//#include <list>

using namespace std;

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define sz(x) ((int((x).size())))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define fl endl<<flush

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T _rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pie;
typedef pie pii;
typedef complex<double> point;

const double eps=1e-8;
const ld leps=1e-14;
const int MN=100+10;
int t,tc,n,m;
int mp[MN][MN];
int mr[MN],mc[MN];
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	while (++tc<=t)
	{
		cout<<"Case #"<<tc<<": ";
		cin>>n>>m;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) cin>>mp[i][j];
		for (int i=0;i<n;i++) mr[i]=0;
		for (int i=0;i<m;i++) mc[i]=0;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) smx(mr[i],mp[i][j]),smx(mc[j],mp[i][j]);
		bool av=true;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (min(mr[i],mc[j])>mp[i][j])
			av=false;
		cout<<(av?"YES":"NO")<<endl;
	}
	return 0;
}

