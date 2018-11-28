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

int a[100],b[100];
bool end=false;
bool av[100];
int dp[100];
int res[100];
int now[100];
int temp[100];
int n,t,cnt;
void bt(int p)
{
	if (end) return ;
	if  (p==n)
	{
		for (int i=n-1;i>=0;i--)
		{
			temp[i]=1;
			for (int j=i+1;j<n;j++) if (now[j]<now[i])
				smx(temp[i],temp[j]+1);
			if (temp[i]!=b[i]) return ;
		}
		end=true;
		for (int i=0;i<n;i++) res[i]=now[i];
		return ;
	}
	cnt++;
	for (int i=0;i<n && !end;i++) if (av[i])
	{
		now[p]=i;
		dp[p]=1;
		for (int j=0;j<p;j++) if (now[j]<now[p])
			smx(dp[p],dp[j]+1);
		if (dp[p]==a[p] && i+1>=b[p])
		{
			av[i]=false;
			bt(p+1);
			av[i]=true;
		}
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		show(tc);
		cin>>n;
		end=false;
		for (int i=0;i<n;i++) cin>>a[i];
		for (int i=0;i<n;i++) cin>>b[i];
		for (int i=0;i<n;i++) av[i]=1;
		cnt=0;
		bt(0);
		show(cnt);
		cout<<"Case #"<<tc<<": ";
		for (int i=0;i<n;i++) cout<<res[i]+1<<" ";
		cout<<endl;
	}
	return 0;
}
