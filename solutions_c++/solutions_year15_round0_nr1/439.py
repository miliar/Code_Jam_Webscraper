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
    ret_t solve(int n, string s) {
	ret_t ret = 0;
	int total = 0;
	for (int i = 0; i <= n; ++i) {
	    int here = (int)(s[i] - '0');
	    if (here > 0 && total < i) {
		int lack = i - total;
		ret += lack;
		total += lack;
	    }
	    total += here;
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
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int n; string shy;
        {
            stringstream A(s);
            A >> n >> shy;
        }
        ret_t ret = solver.solve(n, shy);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
