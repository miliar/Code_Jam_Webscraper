// /\||/\||
//
//
//////////////////////
// Program: 
// Written By Alireza Farhadi (LGM)
//////////////////////
#include <bits/stdc++.h>

using namespace std;

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define FE(i, c) for(auto i = ((c)).begin(); i != ((c)).end(); i++)
#define get(x,i) (get<((i))>(((x))))
#define ALL(x) ((x)).begin(),((x)).end()
#define Mt make_tuple
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define sz(x) ((int((x).size())))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)
#define fl endl<<flush
#define list _list

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T _rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}


/*
ifstream fin(".in");
ofstream fout(".out");
#define cin fin
#define cout fout
*/

int Main();
int main()
{
	ios_base::sync_with_stdio(false);
	cout<<fixed<<setprecision(10);
	return Main();
}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pie;
typedef pie pii;
typedef tuple<int,int,int> trip;
typedef complex<double> point;

const double eps=1e-8;
const ld leps=1e-14;

int t,tc;
int r1,r2;
int mp1[4][4],mp2[4][4];
int Main()
{
	cin>>t;
	while (t-->0)
	{
		cin>>r1,r1--;
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) cin>>mp1[i][j];
		cin>>r2,r2--;
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) cin>>mp2[i][j];
		vector <int> all;
		for (int i=0;i<4;i++) for (int j=0;j<4;j++) if (mp1[r1][i]==mp2[r2][j])
			all.push_back(mp1[r1][i]);
		cout<<"Case #"<<++tc<<": ";
		if (all.size()>1)
			cout<<"Bad magician!"<<endl;
		else if (all.size()==1)
			cout<<all[0]<<endl;
		else
			cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
