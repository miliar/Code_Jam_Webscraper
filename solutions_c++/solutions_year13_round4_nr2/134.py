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


/*
ifstream fin(".in");
ofstream fout(".out");
#define cin fin
#define cout fout
*/

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pie;
typedef pie pii;
typedef complex<double> point;

const double eps=1e-8;
const ld leps=1e-14;

int t;
ll n,p;
bool can1(ll n,ll p,ll m)
{
	if (m==0) return true;
	if (m!=0 && p<=(1LL<<(n-1)))
		return false;
	p-=(1LL<<(n-1));
	return can1(n-1,p,(m+1)/2-1);
}
bool can2(ll n,ll p,ll m)
{
	if (p<=0) return false;
	if (m==0) return true;
	if (p>=(1LL<<n)) return true;
	if (m==(1LL<<n)-1 && p<=(1LL<<(n-1))) return false;
	if (m==(1LL<<n)-1)
		return can2(n-1,p-(1LL<<(n-1)),(1LL<<(n-1))-1);
	return can2(n-1,p,(m+1)/2);
}
ll bs1()
{
	ll s=0,e=(1LL<<n)-1;
	ll res=0;
	while (s<=e)
	{
		ll m=(s+e)/2;
		if (can1(n,p,m))
			res=m,s=m+1;
		else
			e=m-1;
	}
	return res;
}
ll bs2()
{
	ll s=0,e=(1LL<<n)-1;
	ll res=0;
	while (s<=e)
	{
		ll m=(s+e)/2;
		if (can2(n,p,m))
			res=m,s=m+1;
		else
			e=m-1;
	}
	return res;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		cin>>n>>p;
		cout<<"Case #"<<tc<<": "<<bs1()<<" "<<bs2()<<endl;
	}
	return 0;
}
