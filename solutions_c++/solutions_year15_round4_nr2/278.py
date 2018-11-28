#include "cstdio"
#include "iostream"
#include "algorithm"
#include "cmath"
#include "cstring"
#include "cstdlib"
#include "climits"
#include "cassert"
#include "bitset"
#include "complex"
#include "queue"
#include "vector"
#include "queue"
#include "set"
#include "map"
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MK make_pair
// #define X first
// #define Y second
// #define ll long long
// #define ull unsigned long long
// #define ITR iterator
// #define LB lower_bound
// #define UB upper_bound
// #define PII pair<int, int>
// #define CLR(a) memset(a, 0, sizeof(a))
int getint(){
    int s = 0, o = 1;
    char c;
    for(c = getchar(); c<'0'||c>'9';c = getchar()) if(c=='-') o = -1;
    for(;c>='0'&&c<='9'; c = getchar()) s *=10, s+=c-'0';
    return s*o;
}
  
const int maxn = 110;
double R[maxn], C[maxn];
double V,X;
long double VX;
int id[maxn];
int n;
bool check(long double T){
	long double W;
	long double l = 0, r = 0;
	W = V;
	rep(j,n) if(W > 0){
		int i = id[j];
		long double t = min(T, W / R[i]);
		l += t * R[i] * C[i];
		W -= t * R[i];
	}
	
	W = V;
	for(int j=n-1; j>=0; --j) if(W > 0){
		int i = id[j];
		long double t = min(T, W / R[i]);
		r += t * R[i] * C[i];
		W -= t * R[i];
	}
	// cerr << T << ' '<< l << ' ' << r << ' ' << VX << ' ' << (l<=VX && VX<=r) << endl;
	if(l<=VX+1e-14 && VX-1e-14<=r) return 1; else return 0;
}

bool cmp(int a,int b){
	return C[a] < C[b];
}

void run(int ca){
		printf("Case #%d: ", ca+1);
		// cerr << ca <<endl;
		n = getint();
		scanf("%lf%lf", &V, &X);
		VX = (long double)V*X;
		// cout << VX << endl;
		rep(i,n) scanf("%lf%lf", R+i, C+i);
		bool allda = 1, allxiao = 1;
		rep(i,n){
			allda &= (C[i] > X);
			allxiao &= (C[i] < X);
		}
		if(allda || allxiao){
			printf("IMPOSSIBLE\n");
			return;
		}

		rep(i,n) id[i] = i; sort(id, id+n, cmp);
		double minR = R[0], sumR = 0;
		rep(i,n) sumR += R[i], minR = min(minR, R[i]);
		long double l = (long double)V / sumR, r = (long double)V / minR;
		// cerr << l << ' ' << r << endl;
		rep(step,1000){
			long double m = (l+r) / 2;
			if(check(m)) r = m; else l = m;
		}
		long double right = 0;
		rep(i,n) if(C[i]==X) right += R[i];
		if(right > 0) r = min(r, (long double)V / right);
		printf("%.10lf\n", (double)r);
}

int main(int argc, char const *argv[])
{
	int cas = getint();
	rep(ca,cas){
		run(ca);
	}
	return 0;
}