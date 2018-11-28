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
#include<climits>

using namespace std;

// Typedefs
typedef long long ll;
typedef long double ld;
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
#define all(v) v.begin(), v.end()
#define sz(A) int((A).size())
#define pb push_back
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define LSOne(S) (S & (-S)) // bit menos significativo
#define first(x) x.first	// lidam com triplas
#define second(x) x.second.first
#define third(x) x.second.second
#define CLR(x, a) memset(x, a, sizeof(x))

// Constantes
const double PI = 2*asin(1.0);
const int INF = 1000000000;	// 9 zeros
const double EPS = 1e-10;

// Matematica basica
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
inline ll gcd(ll n1, ll n2) {return n2==0? abs(n1) : gcd(n2,n1%n2);}	// MUDAR PARA O PKU!
inline ll lcm(ll n1, ll n2) {return n1==0||n2==0? 0 : abs(n1*(n2/gcd(n1,n2)));}	// MUDAR PARA O PKU!

int vet[150];

bool pali (ll X){
	int pos = 0;
	while (X){
		vet[pos++] = X%10;
		X/=10;
	}
	FORR (i, pos/2)	if (vet[i]!=vet[pos-i-1]) return false;
	return true;
}

vector<ll> pre;

int bsearch1 (ll X){
	int inf = 0, sup = sz(pre)-1;
	while (inf<sup){
		int med = (inf+sup+1)/2;
		if (X>=pre[med])
			inf = med;
		else
			sup = med-1;
	}
	return inf;
}

int bsearch2 (ll X){
	int inf = 0, sup = sz(pre)-1;
	while (inf<sup){
		int med = (inf+sup+1)/2;
		if (X>pre[med])
			inf = med;
		else
			sup = med-1;
	}
	return inf;
}

int main() {
	int T;
	pre.pb(0);
	for (ll i = 1; i <= 10000000; i++) {
		if (pali(i)&&pali(i*i)) pre.pb(i*i);
	}
	//for (int i = 0; i < sz(pre); i++) cout << pre[i] << " ";
	//cout << endl;
	//cout << bsearch1 (4) << endl;
	cin>>T;
	FORR (k, T){
		ll A, B;
		cin >> A >> B;
		cout << "Case #" << (k+1) << ": ";
		cout << (bsearch1(B)-bsearch2(A)) << endl;
	}
}
