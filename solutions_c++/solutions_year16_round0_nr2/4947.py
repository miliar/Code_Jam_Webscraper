// In the Name of Allah
// AD13

//check debug,   read 2 times at least!
//think --> idea? --> really works? (create test cases) --> code it! --> test again
#include <set>
#include <map>
#include <string>
#include <vector>
#include <iostream>
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
	freopen("bb.in", "r", stdin);
	freopen("bb.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		//cerr << "--> " << tc << " / " << T << endl;
		string str;
		cin >> str;
		int cnt = 0;
		int last = str.size() - 1;
		while (last >= 0) {
			if (str[last] == '+') {
				last--;
				continue;
			}
			cnt++;
			while (last >= 0 && str[last] == '-') last--;
			for (int i = 0; i <= last; i++) {
				if (str[i] == '-') str[i] = '+';
				else str[i] = '-';
			}
		}

			
		cout << "Case #" << tc << ": ";
		cout << cnt << endl;
	}
	
	return 0;
}
/*

*/