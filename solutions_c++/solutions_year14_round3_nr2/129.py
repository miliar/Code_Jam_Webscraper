#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <complex>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <unistd.h>
using namespace std;
typedef long long lng;
typedef unsigned long long ulng;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<short, short> PSS;
typedef pair<PII, int> PIII;
typedef pair<lng, lng> PLL;
typedef pair<ulng, ulng> PUU;
typedef pair<lng, int> PLI;
typedef pair<int, lng> PIL;
typedef pair<ld, ld> PDD;
template<class T> inline T sqr(T x) { return x * x; }
template<class T> inline string tostr(const T & x) { stringstream ss; ss << x; return ss.str(); }
inline lng parse(const string & s) { stringstream ss(s); lng x; ss >> x; return x; }
#define left asdleft
#define right asdright
#define link asdlink
//#define unlink asdunlink
#define next asdnext
#define prev asdprev
#define y0 asdy0
#define y1 asdy1
#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define X first
#define Y second
#define hash asdhash
#define move asdmove
const ld EPS = 1e-12;
const int INF = 1000*1000*1000;
const char CINF = 102;
const lng LINF = INF * 1ll * INF;
const ld DINF = 1e200;
const ld PI = 3.1415926535897932384626433832795l;
int gcd(int a,int b){return a?gcd(b%a,a):b;}
lng gcd(lng a,lng b){return a?gcd(b%a,a):b;}
lng powmod(lng a,lng p,lng m){lng r=1;while(p){if(p&1)r=r*a%m;p>>=1;a=a*a%m;}return r;}
#define TASKA "iota"

const lng mod=INF+7;
vector<string> A;
lng ans;

string norm(string s){
	string r;
	for(int i=0;i<sz(s);){
		r+=s[i];
		int ii=i+1;
		while(ii<sz(s) && s[ii]==s[i])
			++ii;
		i=ii;
	}
	return r;
}

vector<string> norm(vector<string> A){
	forv(i,A){
		A[i]=norm(A[i]);
	}
	map<char,int> cnt;
	forv(i,A){
		forv(j,A[i]){
			++cnt[A[i][j]];
		}
	}
	forv(i,A){
		if(sz(A[i])>2 && A[i][0]==A[i][sz(A[i])-1])
			return vector<string>();
		while(sz(A[i])>2){
			if(cnt[A[i][1]]>1)
				return vector<string>();
			A[i].erase(A[i].begin()+1);
		}
	}
	return A;
}

void solve(){
	A=norm(A);
	if(!sz(A)){
		ans=0;
		return;
	}
	ans=1;
	
	vector<vector<int> > gr(26);
	vector<vector<int> > igr(26);
	vector<int> loops(26);
	
	forv(i,A){
		int a=A[i][0]-'a';
		int b=A[i][sz(A[i])-1]-'a';
		if(a==b)
			(ans*=++loops[a])%=mod;
		else{
			gr[a].pb(b);
			igr[b].pb(a);
		}
	}
	
	vector<bool> was(26);
	int comps=0;
	forn(i,26){
		if(was[i])
			continue;
		if(sz(igr[i]))
			continue;
		if(!sz(gr[i]) && !loops[i]){
			was[i]=true;
			continue;
		}
		(ans*=++comps)%=mod;
		int v=i;
		while(true){
			if(was[v] || sz(gr[v])>1 || sz(igr[v])>1){
				ans=0;
				return;
			}
			was[v]=true;
			if(sz(gr[v]))
				v=gr[v][0];
			else
				break;
		}
	}
	
	forn(i,26){
		if(!was[i])
			ans=0;
	}
}

void brute(){
	ans=0;
	vector<string> A=norm(::A);
	if(!sz(A))
		return;
	
	vector<int> P(sz(A));
	forv(i,P){
		P[i]=i;
	}
	do{
		string s;
		forv(i,P){
			s+=A[P[i]];
		}
		bool was[26];
		clr(was,0);
		bool ok=true;
		for(int i=0;i<sz(s);){
			if(was[s[i]-'a']){
				ok=false;
				break;
			}
			was[s[i]-'a']=true;
			int ii=i;
			while(ii<sz(s) && s[ii]==s[i])
				++ii;
			i=ii;
		}
		if(ok)
			++ans;
	}while(next_permutation(all(P)));
	ans%=mod;
}

void input(){
	int n;
	cin>>n;
	A.resize(n);
	forn(i,n){
		cin>>A[i];
	}
}

void output(){
	cout<<ans<<endl;
}

int main(){
#ifdef __ASD__
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen(TASKA".in", "r", stdin); freopen(TASKA".out", "w", stdout);
#endif
	
	int tc;
	cin>>tc;
	forn(qqq,tc){
		cerr<<qqq<<"/"<<tc<<endl;
		input();
		/*
		brute();
		lng b=ans;
		solve();
		lng r=ans;
		if(r!=b){
			cerr<<"failed"<<endl;
			cout<<"failed "<<qqq<<": "<<b<<' '<<r<<endl;
			return 123;
		}//*/
		printf("Case #%d: ", qqq+1);solve();output();
	}
	//cerr<<"passed"<<endl;
	
	return 0;
}
