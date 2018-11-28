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
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		cerr << "--> " << tc << " / " << T << endl;
		int n; cin >> n;
		int arr[1010];
		For (i, n) cin >> arr[i];
		int ans1 = 0, ans2 = 0, rate = 0;
		for (int i = 1; i < n; i++) {
			if (arr[i] < arr[i-1]) {
				int k = arr[i-1] - arr[i];
				ans1 += k;
				rate = max (rate, k);
			}
		}
		For (i, n-1) {
			if (rate >= arr[i])
				ans2 += arr[i];
			else 
				ans2 += rate;
		}

		cout << "Case #" << tc << ": ";
		cout << ans1 << ' ' << ans2 << endl;
	}
	
	return 0;
}
/*

*/