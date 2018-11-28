// /\||/\||
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
#include <cassert>
#include <csignal>
#include <cmath>
#include <array>
#include <queue>
#include <stack>
#include <string>
#include <regex>
#include <set>
#include <map>
#include <tuple>
#include <list>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <unordered_set>
#include <unordered_map>

using namespace std;
#ifdef _TEST
#define testdo(x) x
#else
#define testdo(x)
#endif
#define show(x) testdo(cerr<<((#x))<<" = "<<((x))<<" "<<endl)
#define bit(a,b) (((a)>>(b))&1)
#define gt(x,i) (get<((i))>(((x))))
#define ALL(x) ((x)).begin(),((x)).end()
#define Mt make_tuple
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define bcntll(x) ((__builtin_popcountll(x)))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define list _list

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T gcd(T x,T y) { return y?gcd(y,x%y):x;}
namespace std{ template<class T,class U> struct hash<pair<T,U>> {
	inline size_t operator() (const pair<T,U> & p) const { return hash<T>()(p.first)*701+hash<U>()(p.second);}
};}

typedef long long ll;
typedef pair<int,int> pie;
typedef tuple<int,int,int> trip;
typedef complex<double> point;

const double eps=1e-11l;

const int MN=1000;

int t,n;
long double v,x;
long double r[MN],c[MN];
long double cs[MN];
void update(long double & tot,long double & tt)
{
	tot=tt=0;
	for (int i=0;i<n;i++) 
		tot+=cs[i]*r[i],tt+=cs[i]*r[i]*c[i];
}
bool check(long double m)
{
	long double tot=0,tt=0;
	for (int i=0;i<n;i++)
		cs[i]=m,tot+=r[i]*m,tt+=r[i]*m*c[i];
	if (tot+eps<v) return 0;
	if (abs(tt/tot-x)<=eps) return 1;
	while (tot>v+eps)
	{
		long double temp=tt/tot;
		if (abs(temp-x)<=eps) return 1;
		int inx=-1;
		bool sgn=temp>x;
		if (temp>x)
		{
			for (int i=0;i<n;i++) if (cs[i]>eps && (inx==-1 || c[i]>c[inx]))
				inx=i;
		}
		else
		{
			for (int i=0;i<n;i++) if (cs[i]>eps && (inx==-1 || c[i]<c[inx]))
				inx=i;
		}
		long double m=min(cs[inx],(tot-v)/r[inx]);
		cs[inx]-=m;
		update(tot,tt);
		temp=tt/tot;
		if (abs(temp-x)<=eps) return 1;
		if (sgn==1 && temp<x) return 1;
		if (sgn==0 && temp>x) return 1;
	
	}
	return 0;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		cin>>n>>v>>x;
		cerr<<tc<<" : "<<v<<" "<<x<<endl;
		for (int i=0;i<n;i++) cin>>r[i]>>c[i];
		long double s=0,e=1e10;
		bool fnd=false;
		for (int i=0;i<1000;i++)
		{
			long double m=(s+e)/2;
			if (check(m))
				fnd=true,e=m;
			else
				s=m;
		}
		cout<<"Case #"<<tc<<": ";
		if (!fnd)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<fx(10)<<(s+e)/2<<endl;
	}
	return 0;
}
