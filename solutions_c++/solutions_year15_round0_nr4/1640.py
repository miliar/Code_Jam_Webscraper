// In the Name of Allah
// AD13
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long long ll;		//	typedef unsigned long long  ull;
typedef pair <int, int> pii;//	typedef pair <double, double> pdd;
typedef vector <int> VI;
#define MP make_pair
const int INF = 2147483647, MOD = 1000*1000*1000 + 7;
const double eps = 1e-8; // (eps < 1e-15) is the fact (1e-14)
#define For(i, n) for (int i = 0; i < (n); i++)
#define For1(i, n) for (int i = 1; i <= (n); i++)
//#define debug(x) { cerr << #x << " = _" << (x) << "_" << endl; }
void Error(string err) { cout << err; cerr << "_" << err << "_"; exit(0); }
int gcd(int a, int b) { return (b==0)? a: gcd(b, a%b); }
/*-------------------------------------------------------------------------------------*/

const int sz = 100 * 1000;

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		//cerr << "--> " << tc << " / " << T << endl;
		int x, r, c;
		cin >> x >> r >> c;
		int winner = 0;
		if (r > c) swap (r, c);

		if (r * c % x == 0) {
			if (x <= 2) winner = 1;
			else {
				if (x == 3) {
					if ( (r == 2 && c == 3)
						|| (r == 3 && c >= 3))
						winner = 1;
				}
				else {
					if (r + c >= 7) winner = 1;
				}
			}
		}

		cout << "Case #" << tc << ": ";
		if (winner == 0) cout << "RICHARD";
		else cout << "GABRIEL";
		cout << endl;
	}
	
	return 0;
}
/*

*/