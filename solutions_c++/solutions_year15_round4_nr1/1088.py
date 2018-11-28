#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<ctime>   // srand( time(NULL) )
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
#define CLR(x, a) memset(x, a, sizeof(x))
#define pb push_back
#define mp make_pair
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define LSOne(S) (S & (-S)) // bit menos significativo
#define first(x) x.first    // lidam com triplas
#define second(x) x.second.first
#define third(x) x.second.second
 
// Constantes
const double PI = 2*asin(1.0);
const int INF = 1000000000; // 9 zeros
const double EPS = 1e-10;
 
// Matematica basica
inline int cmp(double x, double y = 0, double tol = EPS) {
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }
inline ll gcd(ll n1, ll n2) {return n2==0? abs(n1) : gcd(n2,n1%n2);}    // MUDAR PARA O PKU!
inline ll lcm(ll n1, ll n2) {return n1==0||n2==0? 0 : abs(n1*(n2/gcd(n1,n2)));} // MUDAR PARA O PKU!

string mat[150];

int main() {
	int T;
	cin>>T;
	FORR (c, T) {
		int R, C;
		cin>>R>>C;
		FORR (i, R) cin>>mat[i];
		int res = 0;
		bool imp = false;
		FORR (i, R) {
			FORR (j, C) {
				if (mat[i][j]=='.') continue;
				bool ok = false;
				int aux = 0;
				FOR (k, i+1, R) {
					if (mat[k][j]!='.') {
						ok = true;
						aux |= 1;
						break;
						
					}
				}

				for (int k = i-1; k>=0; k--) {
					if (mat[k][j]!='.') {
						ok = true;
						aux |= 2;
						break;
					}
				}
	
				FOR (k, j+1, C) {
					if (mat[i][k]!='.') {
						ok = true;
						aux |= 4;
						break;
					}
				}

				for (int k = j-1; k>=0; k--) {
					if (mat[i][k]!='.') {
						ok = true;
						aux |= 8;
						break;
					}
				}
		

				if (ok) {
					if (mat[i][j]=='v') {
						if ((1 & aux) == 0) res++;
					} else if (mat[i][j]=='^') {
						if ((2 & aux) == 0) res++;
					} else if (mat[i][j]=='>') {
						if ((4 & aux) == 0) res++;
					} else {
						if ((8 & aux) == 0) res++;
					}
				} else {
					imp = true;
				}
	
				
			}
		}
		cout << "Case #" << c+1 << ": ";
		if (imp) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << res << endl;
		}
	}
    return 0;
}
