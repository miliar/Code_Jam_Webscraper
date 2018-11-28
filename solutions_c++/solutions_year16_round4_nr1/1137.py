#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstring>
#include <ctime>
#include <deque>
#include <forward_list>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream> // istringstream buffer(myString);
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;
typedef unsigned long long int ull;
typedef long long int ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pi> vpi;
struct dbg_ {template<typename T> dbg_ & operator ,(const T & x) { cerr << x << ' '; return *this;}} dbg_t;
struct cin_ {template<typename T> cin_ & operator ,(T & x) { cin >> x; return *this;}} cin_;
template <typename T1, typename T2>
static inline ostream & operator<<(ostream & os, std::pair<T1, T2> const& p) {
    os << "{" << p.first << ", " << p.second  << "}";return os;
}
#define sync ios_base::sync_with_stdio(0) //to synchronize the input of cin and scanf

#define inf 2000000007
#define eps 1e-9
#define popcnt __builtin_popcount
#define gcd __gcd

#define rep(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define dwn(i,n) for(int i=(n); --i>=0; )
#define repr(i,l,r) for(int i=(l), _##i=(r); i<_##i; ++i)
#define dwnr(i,l,r) for(int i=(r), _##i=(l); --i>=_##i; )
#define repa(i,a) for(auto i : a)
#define rd(args...) { cin_,args; }

#define mp make_pair
#define pb push_back
#define x first
#define y second
#define qtop(q) ((tmp=q.front()),q.pop(),tmp)
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define has(a,b) ((a).find(b) != (a).end())
#define index(a,x) (lower_bound(all(a),x)-arr.begin())
#define fill(a,v) memset(a, v, sizeof(a))
#define nfill(a,n,v) rep(i,n)a[i]=v;
#define clr(a) memset(a, 0, sizeof(a))
#define rda(a,n) rep(i,n){cin>>a[i];}
#define sz(a) ((int)(a.size()))
#define e(a) ((int)1e##a+7)
#define _ << " " <<

#define in(i,l,r) (l<=i&&i<r)
#define remax(a,b) (a)=max((a),(b))
#define remin(a,b) (a)=min((a),(b))
#define remax2(a,b,ai,bi) do{if((a)>(b)){a=b;ai=bi;}}while(0)
#define remin2(a,b,ai,bi) do{if((a)<(b)){a=b;ai=bi;}}while(0)
#define ifmax(a,b) if((a)>(b)&&(1||a=b))
#define ifmin(a,b) if((a)<(b)&&(1||a=b))
#define checkbit(n,b) ((n >> b) & 1)

#ifdef SLONICHOBOT
	#define tu cerr << "#line: " << __LINE__ << endl
	#define dbg(args ...) { cerr << "|" << __LINE__ << "| "; dbg_t,args;cerr << endl; }
	#define dbgg(X) cerr << #X ": " << X << endl
	#define debug(args...) do {cerr << #args << ": "; dbg_t,args; cerr << endl;} while(0)
	#define dbga(a,n) rep(i,n)cerr<<a[i]<<" ";cerr<<endl
	#define dbgc(a) repa(i,a)cerr<<a[i]<<',';cerr<<endl
#else
	#define tu
	#define dbg
	#define dbgg
	#define debug
	#define dbga
	#define dbgc
#endif
int tmp,act;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

int N,P,R,S;
int arr[4];

string str;
string gmr(int w,int d) {
	int l =(w+1)%3;
	if (d==1){
		arr[w]--;arr[l]--;
		// dbg(d,':',arr[0],arr[1],arr[2]);
		rep(i,3)if(arr[i]<0) return "";
		string tmp="";tmp+=(w==0 ? 'P' : w==1 ?'R' : 'S'); tmp+=(l==0 ? 'P' : l==1 ?'R' : 'S');
		sort(all(tmp));
		return tmp;
	}
	string ret = "";
	string a = gmr(w,d-1);
	string b = gmr(l,d-1);
	if (a=="" || b=="") return "";
	return min(a,b)+max(a,b);
}
string gm(int w,int d) {
	str="";
	arr[0]=P; arr[1]=R; arr[2]=S;
	return gmr(w,d);
}

void solve() {
	rd(N,R,P,S);
	vector<string> rt;
	string ret = gm(0,N); if (ret!="") rt.pb(ret);
	ret=gm(1,N); if (ret!="") rt.pb(ret);
	ret=gm(2,N); if (ret!="") rt.pb(ret);
	sort(all(rt));
	if (sz(rt)==0) str="IMPOSSIBLE";
	else str=rt[0];
	cout << str << endl;
}

int main()
{
	int T; cin >> T;
	rep(i,T) {
		cout << "Case #" << (i+1) << ": ";
		solve();
	}
	return 0;
}
