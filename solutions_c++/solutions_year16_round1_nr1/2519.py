// In the Name of Allah
// AD13

//think --> idea? --> really works? (create test cases) --> code it! --> test again
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

string f (string str) {
	if (str.length() < 2) return str;
	int best = 0;
	for (int i = 1; i < str.length(); i++) {
		if (str[i] >= str[best]) best = i;
	}
	string ret = "";
	ret += str[best];
	ret += f(str.substr(0, best));
	ret += str.substr(best + 1);
	
	return ret;
}

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		//cerr << "--> " << tc << " / " << T << endl;
		string str;
		cin >> str;

		cout << "Case #" << tc << ": " << f(str);
		cout << endl;
	}
	
	return 0;
}
/*

*/