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

int mat[100][100];
int N, M;

// <-, /\, ->, \/
int p1[100][100], p2[100][100], p3[100][100], p4[100][100];

bool vet1[100], vet2[100];

bool check (){
	FORR (i, N){
		FORR (j, M){
			if ((j==0 || p1[i][j-1]<=mat[i][j]) && (j==M-1 || p3[i][j+1]<=mat[i][j])) continue;
			if ((i==0 || p2[i-1][j]<=mat[i][j]) && (i==N-1 || p4[i+1][j]<=mat[i][j])) continue;
			return false;
		}
	}
	
	return true;
}

int main() {
	int T;
	cin>>T;
	FORR (k, T){
		cin >> N >> M;
		FORR (i, N) FORR (j, M) cin >> mat[i][j];
		FORR (i, N) vet1[i] = true;
		FORR (i, M) vet2[i] = true;
		FORR (i, N) {
			p1[i][0] = mat[i][0];
			p3[i][M-1] = mat[i][M-1];
		}
		FORR (i, M){
			p2[0][i] = mat[0][i];
			p4[N-1][i] = mat[N-1][i];
		}

		
		FORR (i, N){
			FOR (j, 1, M){
				p1[i][j] = max (p1[i][j-1], mat[i][j]);
			}
		}
		
		FOR (i, 1, N){
			FORR (j, M){
				p2[i][j] = max (p2[i-1][j], mat[i][j]);
			}
		}
		
		FORR (i, N){
			for (int j = M-2; j>=0; j--){
				p3[i][j] = max (p3[i][j+1], mat[i][j]);
			}
		}
		
		for (int i = N-2; i>=0; i--){
			FORR (j, M){
				p4[i][j] = max (p4[i+1][j], mat[i][j]);
			}
		}
		
		
		cout << "Case #" << (k+1) << ": ";
		if (check())
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
