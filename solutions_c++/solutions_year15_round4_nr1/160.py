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

const double eps=1e-8;

const int MN=100+1000;

int t,tc;
int n,m;
char mp[MN][MN];
bool ng[MN][MN][4];
int xd[]={-1,0,1,0};
int yd[]={0,1,0,-1};
string dir="^>v<";
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	while (t-->0)
	{
		memset(ng,0,sizeof(ng));
		cin>>n>>m;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) cin>>mp[i][j];
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (mp[i][j]!='.') for (int d=0;d<4;d++)
		{
			int nx=i+xd[d],ny=j+yd[d];
			while (nx>=0 && nx<n && ny>=0 && ny<m && mp[nx][ny]=='.')
				nx+=xd[d],ny+=yd[d];
			ng[i][j][d]=!(nx>=0 && nx<n && ny>=0 && ny<m);
		}
		cout<<"Case #"<<++tc<<": ";
		int res=0;
		for (int i=0;i<n;i++) for (int j=0;j<m;j++) if (mp[i][j]!='.')
		{
			int cnt=0;
			for (int d=0;d<4;d++) cnt+=ng[i][j][d];
			if (cnt==4)
			{
				cout<<"IMPOSSIBLE"<<endl;
				goto nex;
			}
			int od=dir.find(mp[i][j]);
			res+=ng[i][j][od];
		}
		cout<<res<<endl;
nex:;
	}
	return 0;
}
