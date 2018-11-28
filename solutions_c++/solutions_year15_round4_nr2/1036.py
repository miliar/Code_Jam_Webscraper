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
typedef double ld;
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

double R[150], C[150];

int main() {
	int T;
	cin>>T;
	FORR (c, T) {
		int N;
		cin>>N;
		double V, X;
		cin>>V>>X;
		FORR (i, N) cin>>R[i]>>C[i];
		cout << "Case #" << c+1 << ": ";
		if (N==1) {
			if (C[0]==X) {
				double cost = V/R[0];
				cout << fixed << setprecision(15) << cost << endl;
			} else {
				cout << "IMPOSSIBLE" << endl;
			}
		} else {
			
			if (C[0]>C[1]) swap (C[0], C[1]), swap (R[0], R[1]);
		
			bool imp = false;
			double cost = 0.;
			if (C[0]==X) {
				if (C[1]>X) {
					cost = V/R[0];
				} else if (C[1]==X) {
					cost = V/(R[1]+R[0]);
				} else {
					imp = true;
				}
			} else if (C[0]<X) {
				if (C[1]==X){
					cost = V/R[1];
				} else if (C[1]> X) {
					double V0 = (X * V - C[1] * V) / (C[0] - C[1]);
					double V1 = V - V0;
					cost = max (V0/R[0], V1/R[1]);
				} else {
					imp = true;
				}
			} else {
				imp = true;
			}

			/*double cost = 0;
			if (C[0]==C[1]) {
				if (X==C[0]) {
					cost = V/(R[1]+R[0]);
				} else {
					imp = true;
				}
			} else if (C[0]<=X && C[1]>=X) {
				double V0 = (X * V - C[1] * V) / (C[0] - C[1]);
				double V1 = V - V0;
				cost = max (V0/R[0], V1/R[1]);
				if (V0<0||V1<0) imp = true;
			} else {
				imp = true;
			}*/
			if (imp) {	
				cout << "IMPOSSIBLE" << endl;
			} else {
				cout << fixed << setprecision(15) << cost << endl;
			}
		}
	}
    return 0;
}
