#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef double ret_t;

class Solver {
public:
    int n;
    vector<double> E;
    ret_t f(int m) {
	if (E[m] >= -.5) return E[m];
	if (m + 1 == (1 << n)) return 0;
	ret_t ret = 0;
	for (int i = 0; i < n; ++i) {
	    int j = i;
	    int p = n;
	    while (m & (1 << j)) {
		++j;
		--p;
		if (j == n) j = 0;
	    }
	    ret += f(m + (1 << j)) + p;
	}
	ret /= n;
	E[m] = ret;
	return ret;
    }
    ret_t solve(string s) {
	ret_t ret;

	n = s.size();
	E = vector<double>(1 << n, -1);
	int m = 0;
	for (int i = 0; i < n; ++i) if (s[i] == 'X') m += (1 << i);
	ret = f(m);

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
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        ret_t ret = solver.solve(s);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        cout << "Case #" << no << ": " << fixed << setprecision(10) << ret << endl; // float
    }
    return 0;
}
