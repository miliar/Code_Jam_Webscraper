#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef bool ret_t;

class Solver {
public:
    ret_t solve(int x, int r, int c) {
	if (r < c) swap(r, c);
	if ((r * c) % x) return false;
	if (r < x) return false;
	if (c < (x + 1) / 2) return false;
	if (x <= 3) {
	    return true;
	}
	else if (x == 4) {
	    if (c == 2) return false; // T/S/Z cause bad division
	    return true;
	}
	else if (x == 5) {
	    if (r == 5 && c == 3) return false; // W
	    return true;
	}
	else if (x == 6) {
	    if (c == 3) return false; // asymmetric T
	}
	return false; // x >= 7: can have a small hole
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
        int x, r, c;
        {
            stringstream A(s);
            A >> x >> r >> c;
        }
        ret_t ret = solver.solve(x, r, c);

        // *** give output ***
        cout << "Case #" << no << ": " << (ret ? "GABRIEL" : "RICHARD") << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
