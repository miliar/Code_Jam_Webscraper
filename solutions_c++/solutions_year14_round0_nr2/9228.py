#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <climits>




using namespace std;
#define REP(i,n) for(int i = 0; i < int(n); ++i)
#define REPV(i, n) for (int i = (n) - 1; (int)i >= 0; --i)
#define FOR(i, a, b) for(int i = (int)(a); i < (int)(b); ++i)
#define FORV(i, a, b) for(int i = (int)(a)-1; i >= (int)(b); --i)
#define FORE(i, a) for(int i = 0; i < (int)a.size(); ++i)


#define two(x) (1LL << (x))
#define ALL(a) (a).begin(), (a).end()


#define sz(a) (int)a.size()
#define shows(a) if(a++)cout<<endl
#define pb push_back
#define st first
#define nd second
#define mp(x,y) make_pair(x, y)
#define println(a) cout<<a<<endl
#define print(a) cout<<a
#define clr(a,b) memset(a,b,sizeof(a))
#define OO 1e8
#define EPS 1e-8

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<ld> vd;
typedef vector<vd> vvd;
typedef vector<vector<int> > vvi;
typedef vector<pii> vpi;
typedef vector<string> vs;
typedef vector<ll> vl;
typedef vector<ull> vull;
typedef pair<int,pii> edge;


template<class T> void checkmin(T &a, T b){if (b<a)a=b;}
template<class T> void checkmax(T &a, T b){if (b>a)a=b;}
template<class T> void out(T t[], int n){REP(i, n)cout<<t[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> t, int n=-1){for (int i=0; i<(n==-1?t.size():n); ++i) cout<<t[i]<<" "; cout<<endl;}
inline int count_bit(int n){return (n==0)?0:1+count_bit(n&(n-1));}
inline int low_bit(int n){return (n^n-1)&n;}
inline int ctz(int n){return (n==0?0:ctz(n>>1)+1);}
int toInt(string s){int a; istringstream(s)>>a; return a;}
string toStr(int a){ostringstream os; os<<a; return os.str();}
string reverse(string& s){ int n=s.size();REP(i,n/2) s[i]=s[n-1-i];return s;}
inline int isvalid(int i,int j,int H,int L){ return (i>=H||i<0||j>=L||j<0)? 0:1;}
inline int doubleComare(double x,double y){if(fabs(x-y)<=EPS) return 0; if(x<y) return -1; return 1;}

/*
int main()
{
	int a,b,c;
	while(cin>>a>>b>>c){
		if(a!=b&&a!=c) cout<<"A"<<endl;
		else if(b!=a&&b!=c) println("B");
		else if(c!=a&&b!=c) println("C");
		else println("*");
	}
	return 0;
}*/
/*
int main()
{
	double l,w,d,p;
	int n,r=0;
	cin>>n;
	while(n--){
		cin>>l>>w>>d>>p;
		if(((l<=56.0&&w<=45.0&&d<=25.0)||(l+w+d<=125.0))&&p<=7.0) println(1),r++;
		else println(0);
	}
	println(r);
	return 0;
}*/
/*
int main()
{
	int T,r=0;
	cin>>T;
	while(T--){
		r++;
		int n;
		cin>>n;
		vi tab(n);
		REP(i,n) cin>>tab[i];
		cout<<"Case "<<r<<": "<<*max_element(ALL(tab))<<endl;
	}
	return 0;
}*/
/*
int main()
{
	int n,i,j;
	while(cin>>n>>i>>j){
		int r=1,p=2;
		i--,j--;
		while(i/p!=j/p) r++,p*=2;
		cout<<r<<endl;
	}
	return 0;
}*/
/*
int main()
{
	//ifstream cin("a.in");
	//ofstream cout("a.out");
	int win,r,t,tab[4][4]={0};
	cin>>t;
	while(t--){
		int c(0);
		int rows[4]={0};
		cin>>r;
		REP(i,16) cin>>tab[i/4][i%4],rows[i]=

	}
	
	return 0;
}*/

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int TT,k=0;
	cin>>TT;
	cout.precision(7);
	while(TT--){
		k++;
		double C,F,X,T=0,s=2.0;
		cin>>C>>F>>X;
		while(1){
			
				if(X/s<C/s+X/(s+F)) {
					T+=X/s;
					break;
				}
				T+=C/s;
				s+=F;
		}
		cout<<"Case #"<<k<<": "<<fixed<<T<<endl;
		
	}
	return 0;
}