
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


int mat[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}}; 

int main(){

	long T,L,X;
	string str;

	cin >> T;
	//cout << T << endl;

	REP(t,T){
 		cin >> L >> X >> str;

 		if(L * X < 3){
 			cout << "Case #" << t+1 <<": NO" << endl;
 			continue;	
 		}
 		int n = 1;
 		int a[3];
 		a[0] = a[1] = a[2] = 0;
 		int f = 0;
 		for(long j = 0; j < X; ++j)
		for(long i = 0; i < L; ++i){
			char c = str[i];
			//cout << c << endl;
			if(c == 'i'){
				a[0] = 1;
				n = mat[abs(n)-1][1]*(n > 0 ? 1:-1);
			} else if(c == 'j'){
				a[1] = 1;
				n = mat[abs(n)-1][2] * (n > 0 ? 1:-1);

			} else if(c == 'k'){
				a[2] = 1;
				n = mat[abs(n)-1][3] * (n > 0 ? 1:-1);

			}if(f ==0)
			if(n == 2){
				f = 1;
			}
			if(f == 1){
				if(n == 4){
					f = 2;
				}
			}
			//cout << n << endl;
		}
		if(n != -1){

			cout << "Case #" << t+1 <<": NO" << endl;
		} else {
			int s = 0;
			REP(i,3){
				s += a[i];
			}
			if(s > 1 && f == 2) cout << "Case #" << t+1 <<": YES" << endl;
			else cout << "Case #" << t+1 <<": NO" << endl;
		} 
		/*
		if(n == 1){
			cout << "Case #" << t <<": NO" << endl;
		} else if(n == -1){
			if(X % 2 == 0) cout << "Case #" << t <<": YES" << endl;
				else cout << "Case #" << t <<": NO" << endl;
		} else {
			if(X % 4 == 0){
				cout << "Case #" << t <<": YES" << endl;
			} else {
				cout << "Case #" << t <<": NO" << endl;
			}
		}
		*/
	}
	


	return 0;
} 