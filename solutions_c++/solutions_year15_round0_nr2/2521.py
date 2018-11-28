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

int Ans;

void f (VI v, int cnt = 0) {
	sort (v.begin(), v.end());
	int n = v.size();

	int x = v[n-1];
	int ret = cnt + x;
	if (Ans <= cnt) return;
	if (Ans > ret) Ans = ret;
	if (x <= 3) return;
	
	v.push_back (0);
	for (int i = 2; i < x - 1; i++) {
		v[n-1] = i;
		v[n] = x - i;
		f (v, cnt+ 1);
	}
}

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		cerr << "--> " << tc << " / " << T << endl;
		int n;
		cin >> n;
		VI v(n);
		For (i, n) {
			cin >> v[i];
		}

		Ans = 100100;
		f (v);
		cout << "Case #" << tc << ": " << Ans << endl;
	}
	
	return 0;
}
/*
4
3 5 5 5
4 4 4 4 8
3 5 5 9
2 9 6

5
5
6
6
*/