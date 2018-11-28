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
const int MN=10000;
const ll MOD=1000002013;
int dsu[MN];
void merge(int a,int b)
{
	if (a!=b) dsu[a]=b;
}
int par(int a)
{
	if (dsu[a]==a) return a;
	return dsu[a]=par(dsu[a]);
}
pie s[MN],e[MN];
int t,n,m;
ll sc,fc;
ll go(vector <pie> s,vector <pie> e)
{
	sort(s.begin(),s.end());
	ll res=0;
	for (int i=s.size()-1;i>=0;i--)
	{
		int mn=(1<<30),p=-1;
		for (int j=0;j<e.size();j++) if (e[j].second && e[j].first>=s[i].first && e[j].first<mn)
			mn=e[j].first,p=j;
		int t=min(e[p].second,s[i].second);
		ll temp=ll(e[p].first-s[i].first)*ll(e[p].first-s[i].first-1)/2;
		temp%=MOD;
		temp*=t;
		temp%=MOD;
		res+=temp;
		res%=MOD;
		e[p].second-=t;
		s[i].second-=t;
		if (s[i].second!=0)
			i++;
	}
	return res;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin>>t;
	for (int tc=1;tc<=t;tc++)
	{
		cin>>n>>m;
		sc=fc=0;
		for (int i=0;i<m;i++) 
		{
			int p;
			cin>>s[i].first>>e[i].first>>p;
			s[i].second=e[i].second=p;
			ll temp=ll(e[i].first-s[i].first)*ll(e[i].first-s[i].first-1)/2;
			temp%=MOD;
			temp*=p;
			temp%=MOD;
			sc=(sc+temp)%MOD;
		}
		for (int i=0;i<m;i++) dsu[i]=i;
		for (int i=0;i<m;i++) for (int j=0;j<m;j++) if (e[i].first<s[j].first || e[j].first<s[i].first)
			;
		else
			merge(par(i),par(j));
		for (int i=0;i<m;i++) if (par(i)==i)
		{
			vector <pie> st,et;
			for (int j=0;j<m;j++) if (par(j)==i)
			{
				st.push_back(s[j]);
				et.push_back(e[j]);
			}
			fc+=go(st,et);
			fc%=MOD;
		}
		ll temp=fc-sc;
		temp%=MOD;
		if (temp<0) temp+=MOD;
		cout<<"Case #"<<tc<<": "<<temp<<endl;
	}
	return 0;
}
