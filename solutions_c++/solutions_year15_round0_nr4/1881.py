
#include <bits/stdc++.h>
#include <sys/time.h>
//#include <emmintrin.h>


using namespace std;


#define INLINE   inline __attribute__ ((always_inline))
#define NOINLINE __attribute__ ((noinline))

#define ALIGNED __attribute__ ((aligned(16)))

#define likely(x)   __builtin_expect(!!(x),1)
#define unlikely(x) __builtin_expect(!!(x),0)

#define SSELOAD(a)     _mm_load_si128((__m128i*)&a)
#define SSESTORE(a, b) _mm_store_si128((__m128i*)&a, b)

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define ULL         unsigned long long
#define LD          long double
#define MP          make_pair
#define X           first
#define Y           second
#define VC          vector
#define PII         pair <int, int>
#define PDD         pair <double, double>
#define VI          VC < int >
#define VVI         VC < VI >
#define VVVI        VC < VVI >
#define VPII        VC < PII >
#define VD          VC < double >
#define VVD         VC < VD >
#define VVVD        VC < VVD >
#define VS          VC < string >
#define VVS         VC < VS >
#define DB(a)       cerr << #a << ": " << (a) << endl;
#define ASSERT      assert

template<class T> void print(VC < T > v) {cerr << "[";if (v.S) cerr << v[0];FOR(i, 1, v.S) cerr << ", " << v[i];cerr << "]" << endl;}
template<class T> string i2s(T x) {ostringstream o; o << x; return o.str();}
VS splt(string s, char c = ' ') {VS all; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) all.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) all.PB(s.substr(p)); return all;}

double getTime() {
	timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec * 1e-6;

}




int main(){

	long T;

	cin >> T;

	REP(t,T){
		int X,R,C;
		cin >> X >> R >> C;
		/*if( X >= 7 ){
			cout << "Case #" << t+1 << ": RICHARD" << endl;
						
		}*/
		if((R * C) % X) {
			cout << "Case #" << t+1 << ": RICHARD" << endl;
	
		}
		else if(X == 1){
			cout << "Case #" << t+1 << ": GABRIEL" << endl;
	
		}
		else if(X == 2 &&  ( (R * C) % X == 0) ){
				cout << "Case #" << t+1 << ": GABRIEL" << endl;

			
		} else if(X == 3){
			
			
			if((R == 3) && ((C == 2) || (C == 3) || (C == 4))){
				cout << "Case #" << t+1 << ": GABRIEL" << endl;

			} else if((C == 3) && ((R == 2) || (R == 3) || (R == 4))){
				cout << "Case #" << t+1 << ": GABRIEL" << endl;

			}else {
				cout << "Case #" << t+1 << ": RICHARD" << endl;
			}
		}
		else if(X == 4 ){
			if( ( (R == 4 ) && (C >= 3 )) || ( (R >= 3) && (C ==4 )) ){
				cout << "Case #" << t+1 << ": GABRIEL" << endl;

			}
			else {
			cout << "Case #" << t+1 << ": RICHARD" << endl;
			}
		}
		
		
		else {
			cout << "Case #" << t+1 << ": RICHARD" << endl;
		}
	}
	return 0;
} 