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
#define runtime() ((long double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MK make_pair
#define X first
#define Y second
#define ll long long
#define ull unsigned long long
#define ITR iterator
#define LB lower_bound
#define UB upper_bound
#define PII pair<int, int>
#define CLR(a) memset(a, 0, sizeof(a))
int getint(){
    int s = 0, o = 1;
    char c;
    for(c = getchar(); c<'0'||c>'9';c = getchar()) if(c=='-') o = -1;
    for(;c>='0'&&c<='9'; c = getchar()) s *=10, s+=c-'0';
    return s*o;
}
  
const int maxn = 1000 + 10;
int n,k,ca;
int s[maxn], a[maxn], b[maxn];
pair<int,int> P[maxn];

bool check(int x, long long sum){
	long long r = 0;
	rep(i,k){
		if(b[i] > x) return 0;
		r += x - b[i];
	}
	return r >= sum;
}
void run(){
	long long sum = s[0];
	// rep(i,k) printf("%d %d\n", P[i].X, P[i].Y);
	rep(i,k) sum += P[i].X, b[i] = P[i].Y - P[i].X;
	sum = sum % k;
	if(sum < 0) sum += k;
	// printf("%d\n", sum);
	sort(b, b+k);
	int l = b[k-1] - 1, r = b[k-1] + k + k;
	// printf("~ %d %d\n", l, r);
	while(l+1<r){
		int m = (l+r)/2;
		if(check(m, sum)) r = m; else l = m;
	}
	printf("%d\n", r);
}

int main(int argc, char const *argv[])
{
	int cas = getint();
	for(ca=0; ca < cas; ca++){
		printf("Case #%d: ", ca+1);
		n = getint(), k = getint();
		rep(i,n - k + 1) s[i] = getint();
		rep(i,k) a[i] = 0;
		rep(i,n) if(i >= k) a[i] = a[i-k] + s[i-k+1] - s[i-k];
		// rep(i,n) printf("%d ", a[i] ); printf("\n");
		rep(i,k) P[i].X = P[i].Y = a[i];
		rep(i,n) P[i%k].X = min(P[i%k].X, a[i]), P[i%k].Y = max(P[i%k].Y, a[i]);
 		run();
	}	
	cerr << runtime();
	return 0;
}