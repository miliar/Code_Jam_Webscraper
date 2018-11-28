#include <cstdio>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <iterator>
#include <cstring>
#include <string>
#include <cmath>
#include <numeric>
#include <ctype.h>
#include <cctype>
#include <complex>
#include <cassert>
#include <cstdlib>
#include <functional>
#include <utility>
#include <ctime>
//#include <ext/hash_set>
//#include <ext/hash_map>
//struct hasher{ size_t operator()(const string& s) const{ 
//		return hash<const char*>()(s.c_str());} };
using namespace std;
using namespace __gnu_cxx;
#define PB push_back
#define PF push_front
#define MP make_pair
#define X first
#define Y second
#define ST first
#define ND second
#define MT(x,y,z) MP(MP(x,y),z)
#define XT X.X
#define YT X.Y
#define ZT Y
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(VAR(i,(x).begin());i!=(x).end();++i)
#define FORDE(i,x) for(VAR(i,(x).rbegin());i!=(x).rend();++i)
#define FOREACH(i,x) FORE(i,x)
#define VAR(v,n) __typeof(n) v = (n)
#define IT(x) __typeof((x).begin())
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(ALL(c),x) != (c).end())
#define SIZE(x) (int)((x).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define CPY(to,from) memcpy(to,from,sizeof (from))
#define IND(t,n,v) lower_bound(t,t+n,v) - t
#define sqr(a) ((a)*(a))
#define db(x) { if (DEBU) cerr << "line " << __LINE__ << " " << #x \
					 << " = " << x << "\n"; }
#define dbn(x) { if (DEBU) cerr << "\n"; }
#define dba(x) { if (DEBU) { cerr << "line " << __LINE__ << " " << #x \
					<< " = {"; FORE(qwe,x) {if(qwe!=(x).begin()) cerr << ","; \
					 cerr << *qwe; } cerr << "}\n"; } }
#define dbt(t,x) { if (DEBU) { REP(qwe,x) cerr << #t << "[" << qwe << "]=" \
					 << t[qwe] << " "; cerr << "\n"; }}
#define dbtt(t,x,y) { if (DEBU) { REP(qwe,x) { REP(rty,y) cerr << #t \
					 << "[" << qwe << "][" << rty << "]=" << t[qwe][rty] \
					 << " "; cerr << "\n"; }}}
#define dbb(x,r) { if (DEBU) { bitset<r> qwe(x.to_ulong()); \
				 cerr << "line " << __LINE__ << " " << #x \
				 << " = " << qwe << "\n"; } }
#define dbbt(t,x,r) { if (DEBU) REP(rty,x) dbb(t[rty],r); }

typedef long double ld;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long long int lli, LL;
typedef pair<int, int> pii, PII;
typedef pair<pii, int> piii;
typedef pair<lli, lli> pll;
typedef pair<pll, lli> plll;
typedef vector<int> vi, VI;
typedef vector<pii> vii;
typedef vector<piii> viii;
typedef vector<lli> vl;
typedef vector<pll> vll;
typedef vector<plll> vlll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T,class U>ostream & operator<<(ostream&os,const pair<T,U>&qwe){
	    return os << "(" << qwe.X << "," << qwe.Y << ")";
}
template<class T> ostream& operator << (ostream &os, const vector<T>& qwe){
        REP(rty,(int)qwe.size()) os << "vec[" << rty << "]=" << qwe[rty] << " "; 
		return os << "\n";
}
template<class T> ostream& operator << (ostream &os, const set<T>& qwe){
        os << "set:{"; FORE(rty,qwe) {if(rty!=qwe.begin()) os<<","; os << *rty;} 
		return os << "}\n";
}
template<class T> ostream& operator << (ostream &os, const list<T>& qwe){
        os << "list:{"; FORE(rty,qwe) {if(rty!=qwe.begin()) os<<","; os << *rty;}
		return os << "}\n";
}

const double E = 2.718281828459045235360287471351;
const double PI = 3.1415926535897932384626433832795;

#define IsZero(x) (x>=-EPS && x<=EPS)
#define sgn(x) (IsZero(x)?0:((x<0)?-1:1))

lli los(lli l, lli r) { 
	return l + (lli) ((double)(r-l+1) * (rand() / (RAND_MAX + 1.0))); }
string cts(char c) { string s = ""; s+=c; return s; }

template<class T> void minX(T &x, T y){ if(x>y)x=y; }
template<class T> void maxX(T &x, T y){ if(x<y)x=y; }
template<class T> void min(T x, T y, T z){ return min(min(x,y),z); }
template<class T> void max(T x, T y, T z){ return max(max(x,y),z); }

template <class Ty, class Tx>
Ty cast(const Tx &x) {
	    Ty y; stringstream ss(""); ss<<x; ss.seekg(0); ss>>y; return y;
}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}

// #pragma comment (linker, "/STACK:256000000")
// #x zwraca nazwe zmiennej    a ## b laczy napisy i daje zmienna ab

// iostream:cin,getline(cin,string) 
// stdio:scanf,gets(char*),fgets(char*),getchar()
// fgets nie wczytuje bialych znakow z nastepnej linii, dla stringa iostream
// iostream: cout;   stdio: putchar(char) printf
// ios_base::sync_with_stdio(0); przyspiesza iostreama, nie mieszac z stdio 
// freopen ("in.txt","r",stdin); freopen ("out.txt","w",stdout); ... 
// fclose (stdin); fclose (stdout);
// while(scanf("%d",&n)!=EOF)  '\n' == 10
// %c %s %d %u %hd short int %lld %f float %lf double %Lf long double 
// %x unsigned hex small %X unsigned hex big %o octal %llu unsigned lli
// (%5d, 2)    2  (%05d,2)00002  (%x,100) 64  (%#x,100) 0x64  (%#o,100) 0144 
// (%6.2lf, 2)   2.00  (%+d,5) +5   (%*d,5,10)   10 (%.*f,3,2) 2.000 (0*d,3,1) 003
//
// int -> char* : int a; char b[N]; sprintf(b, "%d", a);
// char* -> int : int a; char b[N]; sscanf(b, "%d", &a);
// int -> char* podstawa base : char a[N]; itoa(int, a, base)
// char* -> int podstawa base : char a[N]; strtol(a, NULL, base)
// atoi(char*) to int, atof(char*) to double
// string s; stringstream ss(s); while(ss >> buf) res.PB(buf)
// 
// string -> char* : string a; a.c_str();
// char* -> string : char a[N]; string(a);
// porowananie char* : strcmp(char*,char*) np return strcmp(&c[a],&c[b])<0;
// strlen strcpy strncpy strdup strcat strcmp strncmp 
// strchr strcspn strpbrk strstr strrev
// isupper(int) islower(int) toupper(int) tolower(int) 
// isspace isalpha isalnum isdigit isxdigit ispunct
//
// sort(ALL(v),less<int>()) rosnaca, sort((v),greater<int>()) malejaca
// bool func(pii a,pii b){return a.X*a.X+a.Y*a.Y < b.X*b.X+b.Y*b.Y;}
// struct T {string name; lli X,Y;};
// bool operator<(T a,T b){return a.X*a.X+b.Y*b.Y < a.X*a.X+b.Y*b.Y;}
//
// bitset<N> bs(lli); 
// set() filp() reset() size() count() any() none() [] to_ulong() to_string() 
// __builtin_popcount(int) lli nie dziala,  __ gcd(int,int),  x<<32 does nothing
// __builtin_clz(int) __builtin_ctz(int) for 0 undefined
// REP(s,(1<<N)) - wszystkie podzbiory  for(s=X;s!=0;s=(s-1)&X) - podzbiory X
// !x&(x-1) pow 2, x&(-x)  x&~(x-1) najmniej znaczac bit, ffs(int) jego indeks
// memset(t,0/1/-1,sizeof(t))  1l 1ll 1u 1f
//
// set.size() liniowo, set.end() O(1), set.erase(it++), multiset.erase(x) wszystkie x 
// priority_queue: push,top,pop     queue:push,pop,front,back  
// set/map:insert,erase,find,set.lower_bound 	list:insert,erase,reverse
// deque(jak vector) / list:back,front,push_back,push_front,pop_back,pop_front
// hash_set<string,hasher> hs; hash_map<string,int,hasher> hm; hm.bucket_count()
//
// exit(0) M_PI fabsl abs labs llabs sqrtl llround round(0.5)=1 
// lower_bound - pierwszy nie mniejszy  upper_bound - pierwszy wiekszy
// min_element(All(x)) max_element(ALL(x)) 
// sort(ALL(v)); v.erase(v.unique(),v.end())
// set_union, set_intersection, set_differenece, set_symmetric_difference
// random_shuffle RAND_MAX int rand()=random() srand(int seed) 
// complex<double> x; real,imag,abs,arg,norm,conj,polar,cos,exp,sin,sqrt
// LR :: ++ -- () [] . -> RL ++ -- (unary)+- ! ~ (type) * (address)& 
// LR .* ->* * / % + - << >> < <= > >= == != & ^ | && || ?: = += -= itd
const double EPS = 1e-9;
#define INF 1000000005
#define MAXN 100005
#define MAXM 100005 
#define DEBU 1
#define MOD 1000000009
#define N 105
#define M 105

int t, n, m, a[N][M], maxC[M], maxR[N];
int main(){
	scanf("%d",&t);
	REP(i,t){
		scanf("%d%d",&n,&m);
		REP(j,n) REP(k,m) scanf("%d",&a[j][k]);
		REP(j,n) REP(k,m) maxX(maxR[j], a[j][k]);
		REP(j,m) REP(k,n) maxX(maxC[j], a[k][j]);
		bool yes = 1;
		REP(j,n) REP(k,m) if(min(maxR[j],maxC[k]) != a[j][k]) yes=0;
		if(yes) printf("Case #%d: YES\n",i+1);
		else printf("Case #%d: NO\n",i+1);
		REP(j,n) maxR[j] = 0;
		REP(j,m) maxC[j] = 0;
	}
	return 0;
}
