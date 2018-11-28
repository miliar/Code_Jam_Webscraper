#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    ret_t solve(int r, int c, vector<string> m) {
	ret_t ret = 0;

	for (int i = 0; i < r; ++i) {
	    for (int j = 0; j < c; ++j) {
		if (m[i][j] != '.') {
		    bool any = false;
		    bool safe = false;
		    for (int i2 = i - 1; i2 >= 0; --i2) {
			if (m[i2][j] != '.') {
			    any = true;
			    if (m[i][j] == '^')
				safe = true;
			}
		    }
		    for (int i2 = i + 1; i2 < r; ++i2) {
			if (m[i2][j] != '.') {
			    any = true;
			    if (m[i][j] == 'v')
				safe = true;
			}
		    }
		    for (int j2 = j - 1; j2 >= 0; --j2) {
			if (m[i][j2] != '.') {
			    any = true;
			    if (m[i][j] == '<')
				safe = true;
			}
		    }
		    for (int j2 = j + 1; j2 < c; ++j2) {
			if (m[i][j2] != '.') {
			    any = true;
			    if (m[i][j] == '>')
				safe = true;
			}
		    }
		    if (!any)
			return -1;
		    if (!safe)
			++ret;
		}
	    }
	}

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
        int r, c;
        {
            stringstream A(s);
            A >> r >> c;
        }
	vector<string> m(r);
	for (int i = 0; i < r; ++i) {
	    getline(cin, m[i]);
	    //cerr << m[i] << endl;
	}
        ret_t ret = solver.solve(r, c, m);

        // *** give output ***
        cout << "Case #" << no << ": ";
	if (ret < 0)
	    cout << "IMPOSSIBLE" << endl;
	else
	    cout << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
