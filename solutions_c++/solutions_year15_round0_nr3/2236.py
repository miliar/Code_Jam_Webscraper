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

string cal(const string aStr, const char b) {
	char ret = '1', a = aStr[0];
	bool neg = false;

	if (a == '-') {
		neg = true;
		a = aStr[1];
	}

	if (a == '1') ret = b;
	else if (a == 'i') {
		if (b == 'i') { neg = !neg; ret = '1'; }
		else if (b == 'j') ret = 'k';
		else if (b == 'k') { neg = !neg; ret = 'j'; }
	}
	else if (a == 'j') {
		if (b == 'i') { neg = !neg; ret = 'k'; }
		else if (b == 'j') { neg = !neg; ret = '1'; }
		else if (b == 'k') { ret = 'i'; }
	}
	else if (a == 'k') {
		if (b == 'i') { ret = 'j'; }
		else if (b == 'j') { neg = !neg; ret = 'i'; }
		else if (b == 'k') { neg = !neg; ret = '1'; }
	}

	string retStr = "1";
	retStr[0] = ret;
	if (neg) return "-" + retStr;
	else return retStr;
}

string pre[30300];

/*_____________________________________________________________________________________*/
int main() {
	//*
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	//*/
	int T;
	cin >> T;
	For1 (tc, T) {
		cerr << "--> " << tc << " / " << T << endl;
		int l, x;
		cin >> l >> x;
		string s;
		string str = "";
		cin >> s;
		bool yes = false;
		
		For (i, x) str += s;

		if (str.length() > 2) {
			pre[str.length()] = "-1";
			for (int i = str.length()-1; i >= 0; i--) {
				pre[i] = cal (pre[i+1], str[i]);
				if (pre[i][0] == '-') pre[i] = pre[i].substr(1);
				else pre[i] = "-" + pre[i];
			}

			string ret1 = "1";
			for (int i = 1; !yes && i < str.length() - 1; i++) {
				ret1 = cal(ret1, str[i-1]);
				if (ret1 == "i") {
					string ret2 = "1";
					for (int j = i + 1; !yes && j < str.length(); j++) {
						ret2 = cal (ret2, str[j-1]);
						if (ret2 == "j" && pre[j] == "k")
							yes = true;
					}
				}
			}
		}

		cout << "Case #" << tc << ": ";
		if (yes) cout << "YES";
		else cout << "NO";
		cout << endl;
	}
	
	return 0;
}
/*
2
6 1
jkkiij
2 3000
ij
*/