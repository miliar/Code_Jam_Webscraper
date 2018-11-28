#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<ctime>	// srand( time(NULL) )
#include<iostream>
#include<iomanip>
#include<sstream>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<utility>
#include<algorithm>
#include<map>
#include<set>
#include<bitset>
#include <fstream>

using namespace std;

// Typedefs
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair< int, pair<int, int> > iii;
typedef vector<iii> viii;
typedef vector< vector<int> > vvi;
typedef vector< vector<ii> > vvii;
typedef vector< vector<iii> > vviii;

// Macros
#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, a) for(int i = 0; i < a; ++i)
#define FORE(i, a, b) for(int i = a; i >= b; --i)
#define all(v) (v).begin(), (v).end()
#define sz(A) int((A).size())
#define pb push_back
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define LSOne(S) (S & (-S)) // bit menos significativo
#define first(x) x.first	// lidam com triplas
#define second(x) x.second.first
#define third(x) x.second.second

// Constantes
const double PI = 2*asin(1.0);
const int INF = 1000000000;	// 9 zeros
const double EPS = 1e-10;

// Matematica basica
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
inline ll gcd(ll n1, ll n2) {return n2==0? abs(n1) : gcd(n2,n1%n2);}
inline ll lcm(ll n1, ll n2) {return n1==0||n2==0? 0 : abs(n1*(n2/gcd(n1,n2)));}

int energia, r, vetor[10];

int backtracking(int pos, int atual, const int n, int ganho) {
	if(pos == n) return ganho;
	int res = ganho;
	FORR(i, atual+1) {
		res = max(res, backtracking(pos+1, min(energia, atual-i+r), n, ganho+vetor[pos]*i));
	}
	return res;
}

int main() {
	int t, n, v;
	scanf("%d", &t);
	FORR(l, t) {
		scanf("%d %d %d", &energia, &r, &n);
		FORR(i, n) scanf("%d", &vetor[i]);
		printf("Case #%d: %d\n", l+1, backtracking(0, energia, n, 0));
	}
}
