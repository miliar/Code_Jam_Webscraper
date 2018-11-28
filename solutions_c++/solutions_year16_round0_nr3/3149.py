//#define _CRT_SECURE_NO_WARNINGS

//#pragma comment(linker, "/STACK:640000000")

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <bitset>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define forn1(i, n) for(int i = 1; i <= (int)(n); i++)
#define forr(i, l, r) for(int i = int(l); i <= int(r); i++)
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define y1 __y1
#define sqr(x) ((x) * (x))

typedef long long li;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long uli;
typedef pair<int, int> pt;

inline void read(int&);
inline void read(li&);
inline void read(ld&);
inline void read(char&);
inline void read(string&);
template <typename T1, typename T2> inline void read(T1&, T2&);
template <typename T1, typename T2, typename T3> inline void read(T1&, T2&, T3&);
template <typename T1, typename T2, typename T3, typename T4> inline void read(T1&, T2&, T3&, T4&);

inline void read(string &s) {
	static char buf[int(1e6) + 10];
	assert(scanf("%s", buf) == 1);
	s = string(buf);
	return;
}

const int INF = (int)(1e9);
const li INF64 = (li)(INF) * (li)(INF);
const ld eps = 1e-8;
const ld pi = ld(3.1415926535897932384626433832795);

inline bool in(int i, int j, int n, int m) {
    return i >= 1 && i <= n && j >= 1 && j <= m;
}

inline int myrand() {
    return (rand() ^ (rand() << 15));
}

inline li randL() {
    return myrand() * 1LL * myrand() + myrand();
}



//#define _DEBUG ;

int n,k;

inline bool read() {

	if(!(cin >> n)) return false;
	
	if(!(cin >> k)) return false;

    return true;
}

const long long  int MAXSIZE = (1<<26);
long long int p[MAXSIZE];
long long int powers[11][33];
 
//p[i] == 0 if 2*i + 1 is prime
 
void getTheNumber(long long int n) {
  long long int i, j;//, nr = 1;
   for (i = 2; i < n; ++i) {
    if (p[i] == 0) {
     // nr++;
      for (j = i + i; j <= n; j += i) {
        p[j] = i;
      }
    }
  }

//for (i=1; 2 * i + 1 <= 100; ++i) 
 //  if (p[i] == 0) cerr<<i<<" ";cerr<<"\n";
 // return nr;
  for(int i=2;i<=10;++i){
  	powers[i][0]=1;
  	for(int j=1;j<32;++j){
  		powers[i][j] = powers[i][j-1]*i*1LL; 
  	   // cerr<<powers[i][j]<<" ";
  	}
  	//cerr<<"\n";
  }
}




long long int toBase(int base,  long long nr){
	if(base == 2 )return nr;
	 long long  n = 0;
	for(long long int i=0;(1<<i) <= nr && i<32;++i){
		n += powers[base][i]*((nr & (1<<i))?1:0);
		//cerr<<n<<"\n";
	}

	return n;
}

long long int findDiv(long long int nr){
	//if(nr>MAXSIZE) return 1;
	if(nr <= 0) return -1;
	if(nr < MAXSIZE && p[nr]==0) return -1;
	if(nr < MAXSIZE) return p[nr];
	//cerr<<"-";
	int long long to = sqrt(nr);
	//cerr<<to<<"\n";
	for (int long long i=2; i <= to; ++i) 
      if ((nr%i) == 0) return i;
  return -1;
}

bool ok;
long long int theNR[11];
void write(long long int nr);

void df(long long int n, int base){
	long long int numar = toBase(base, n);
	long long int divizor = findDiv(numar);
	//write(n);
	//cerr<<" "<<n<<" "<<numar<<" "<<divizor<<"\n" ;
	if(divizor == -1)return;
	theNR[base] = divizor;
	if(base == 10){
		ok=true;	
		
		return;
	}
	//if(base == 3)cerr<<"-\n";
	df(n,base+1);
}

void write(long long int nr){
	for(int i=0;(1<<i) <= nr;++i)
		cout<<((nr & (1<<i))?1:0);
	cout<<" ";
}

inline void solve() {
	long long int begin = (1<<(n-1)) + 1;
	long long int end  = (1<<(n)) - 1;
   // cerr<<begin<<" "<<end<<"\n";
	//write(begin); cout<<"\n";
   // df(32773,2);
   // cerr<<findDiv(toBase(5,32773))<<"\n";
  ///  cerr<<MAXSIZE<<"\n";
   // cerr<<p[9]<<"\n";
//return;
  //  k=14;
		for(long long int i=begin;i<end;i+=2){
			//if(p[i]==0)cerr<<i<<" ";
			ok = false;
			df(i,2);
			if(ok){
				//write(i);
				cout<<toBase(10,i)<<" ";
				for(int j=2;j<=10;++j)
					cout<<theNR[j]<<" ";
				cout<<"\n";
				--k;
			}
			if(k==0)return;
		}
	
}

int main() {
#ifdef _DEBUG
    assert(freopen("t.in", "rt", stdin));
    assert(freopen("t.out", "wt", stdout));
#else
#endif

    cout << setprecision(10) << fixed;
    cerr << setprecision(10) << fixed;

    srand(int(time(NULL)));
    

    int T = 1;
    cin>>T;
    //assert(scanf("%d", &T) == 1);

    getTheNumber( MAXSIZE - 1 );

    forn(i, T) {
		//cerr << "TEST == " << i + 1 << endl;
        assert(read());
        cout<<"Case #"<<(i+1)<<":\n";
        solve();
    }

#ifdef _DEBUG
    cerr << "TIME == " << clock() << " ms" << endl;
#endif
    return 0;
}