#include<iostream>
#include<iomanip>
#include<algorithm>
#include<sstream>
#include<vector>
#include<queue>
#include<string>
#include<cctype>
#include<math.h>
#include<functional>
using namespace std;

#define FOR(i,a,b) for ( int i = (a) ; i <= (int)(b) ; i ++ )
#define FRD(i,a,b) for ( int i = (a) ; i >= (int)(b) ; i -- )
#define FR(i,a) FOR(i,0,a)
#define FZ(i,a) FRD(i,a,0)
#define sz size()
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define FRV(i,v) FR( i , v.sz - 1 )
#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vs vector<string>
#define vc vector<char>
#define vb vector<bool>

#define mp make_pair
#define ii <int,int>
#define id <int,double>
#define ss stringstream
#define MAX_INT ((1<<31)-1)

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

int ni() { int n; cin >> n ; return n; }
double nd() { double n; cin >> n ; return n; }
string ns() { string s; cin >> s ; return s; }
char nc() { char c; cin >> c ; return c; }
long int nli() { long int n; cin >> n; return n; }
long long nll() { long long n; cin >> n; return n; }
string nline() { string n; do { getline(cin,n); } while(n == ""); return n;}

int gcd ( int a, int b ) { return ( a%b == 0 ? b : gcd(b,a%b) ) ; }

void main(){
	int T;

	T = ni();

	FOR(tcn,1,T){
		ss res;
		int N = ni();
		vi A(N) , B(N);

		FR(i,N-1) A[i] = nd()*100000;
		FR(i,N-1) B[i] = nd()*100000;

		SORT(A); SORT(B);

		int w = 0, dw = 0;

		int i = 0 , j = 0;

		while ( j < N )
		{
			if( A[i] < B[j] ){
				i++;
				w++;
			}
			j++;
		}
		
		w = N - w;

		int i1 = N - 1; 
		int j1 = N - 1;

		while ( j1 >= 0 ){
			if( A[i1] > B[j1] ){
				dw ++;
				i1 --;
			}
			j1 --;
		}
		res << dw << " " << w;
		cout << "Case #" << tcn << ": "<<res.str()<<endl;
	}
}

