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

string inc(string str) {
	int ind = str.length() - 1;
	while (str[ind] == '1')  {
		str[ind--] = '0';
		if (ind < 0) {
			cout << "The END!";
			exit(0);
		}
	}
	str[ind] = '1';
	return str;
}

ll str2num(string str, int b) {
	ll ret = 0;
	for (int i = 0; i < str.length(); i++) {
		ret *= b;
		ret += str[i] - '0';
	}
	return ret;
}

bool cal (string str) {
	ll nums[9];
	str = "1" + str + "1";
	for (int base = 2; base <= 10; base++) {
		const ll val = str2num(str, base);
		bool found = false;
		for (ll i = 2; i * i <= val; i++) {
			if (val % i == 0) {
				found = true;
				nums[base - 2] = i;
				break;
			}
		}
		if (!found) return false;;
	}

	cout << str << " ";
	for (int i = 0; i < 9; i++) cout << nums[i] << ' ';
	cout << endl;
	
	return true;
}

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		//cerr << "--> " << tc << " / " << T << endl;
		int n, len;
		cin >> len >> n;
		cout << "Case #" << tc << ":" << endl;
		string str = "";
		for (int i = 0; i < len - 2; i++) str += "0";

		while(n) {
			// cerr << str << endl;
			if (cal(str)) {
				cerr << n << str << endl;
				n--;
			}
			str = inc(str);
		}
	}
	
	return 0;
}
/*

*/