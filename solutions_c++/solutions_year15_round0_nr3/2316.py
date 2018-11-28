#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi > vvi; 
typedef pair<int,int> ii; 
typedef vector<ii > vii;
typedef vector<vii > vvii;
typedef set<ii > sii;

#define pb(x) push_back(x)
#define all(c) (c).begin(),(c).end()
#define ins(c) inserter((c),(c).begin())
#define mp(x,y) make_pair((x),(y))
#define mt(x,y,z) make_tuple((x),(y),(z))
#define INF (1e9)

ostream& operator<<(ostream& out, vi v)
{
    for (auto a: v)
        out << a << " ";
    return out;
}

ostream& operator<<(ostream& out, ii d)
{
    out << d.first << ", " << d.second << " ";

    return out;
}

string neg(string str)
{
	if (str[0] == '-')
		return str.substr(1);
	
	return "-" + str;
}

string mult(string a, string b)
{
	bool is_neg = false;

	if (a[0] == '-') {
		a = neg(a);
		is_neg = !is_neg;
	}

	if (b[0] == '-') {
		b = neg(b);
		is_neg = !is_neg;
	}

	if (is_neg) {
		return neg(mult(a, b));
	}

	if (a == "1")
		return b;
	
	if (b == "1")
		return a;
	
	if (a == b)
		return "-1";
	
	if (a == "i" && b == "j")
		return "k";
	
	if (a == "j" && b == "k")
		return "i";
	
	if (a == "k" && b == "i")
		return "j";
	
	if (a == "k" && b == "j")
		return "-i";
	
	if (a == "j" && b == "i")
		return "-k";
	
	if (a == "i" && b == "k")
		return "-j";
		
	return "ERR: " + a + " " + b;
}

string val_exp(string val, int x)
{
	if (x < 1) {
		cout << "fail" << endl;
		return "1";
	}

	if (x == 1)
		return val;
	
	int a = (x + 1) / 2;
	int b = x / 2;

	return mult(val_exp(val, a), val_exp(val, b));
}

string str_to_val(string str)
{
	string val = "1";

	for (auto a: str) {
		stringstream ss;
		ss << a;
		val = mult(val, ss.str());
	}
	
	return val;
}

int prefix_i(string str)
{
	string val = "1";

	for (int i = 0; i < str.size(); i++) {
		val = mult(val, str.substr(i, 1));

		if (val == "i")
			return i;
	}

	return -1;
}

int suffix_k(string str)
{
	string val = "1";

	for (int i = str.size() - 1; i >= 0; i--) {
		val = mult(str.substr(i, 1), val);

		if (val == "k")
			return i;
	}

	return -1;
}

string solve(string pat, int x)
{
	string base_val = str_to_val(pat);
	string val = val_exp(base_val, x);

	if (val != "-1")
		return "NO";
	
	stringstream ss;
	while (x--)
		ss << pat;
	
	int L = prefix_i(ss.str());
	int R = suffix_k(ss.str());

	if (L >= 0 && R >= 0 && L + 1 < R)
		return "YES";
	
	return "NO";
}

int main()
{
    int T, cas = 0;

    cin >> T;
    while (T--) {
		int L, X;
		string pattern;
		cin >> L >> X >> pattern;

		string ans = solve(pattern, X);
		cout << "Case #" << ++cas << ": " << ans << endl;
    }

    return 0;
}
