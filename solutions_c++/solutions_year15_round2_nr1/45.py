#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef ll ret_t;

string itos(ll n) {
    stringstream s;
    s << n;
    return s.str();
}

class Solver {
public:
    ll f(ll a, ll b) {
	if (a == b) return 1;

	string s = itos(b);
	int len = s.size();
	
	ll ret = b;
	if (b % 10 == 0)
	    ret = f(a, b - 1) + 1;
	for (int div = 1; div <= len; ++div) {
	    string s1 = s.substr(0, div);
	    string s2 = s.substr(div);
	    reverse(s1.begin(), s1.end());
	    stringstream A1(s1);
	    ll v1;
	    A1 >> v1;
	    stringstream A2(s2);
	    ll v2;
	    A2 >> v2;

	    if (v2 == 0) continue;
	    int x = 0;
	    if (v1 != 1) x = 1;
	    ll here = v1 + v2 + x;
	    ret = min(ret, here);
	}
	//cerr << b << '\t' << ret << endl;
	return ret;
    }
    ret_t solve(ll n) {
	ret_t ret;
	string s = itos(n);
	int len = s.size();
	if (len == 1) return n;
	ret = 9;
	ll p10 = 10;
	for (int i = 2; i < len; ++i) {
	    ret += f(p10, 10 * p10 - 1);
	    p10 *= 10;
	}
	ret += f(p10, n);
	return ret;
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr //<< "Case "
	    << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        ll n;
        {
            stringstream A(s);
            A >> n;
        }
        ret_t ret = solver.solve(n);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
