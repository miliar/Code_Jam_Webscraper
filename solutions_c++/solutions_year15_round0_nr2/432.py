#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
    ret_t solve(int n, vector<int> p) {
	ret_t ret;
	sort(p.rbegin(), p.rend());
	ret = p.front();
	for (int eat = p.front() - 1; eat >= 2; --eat) {
	    int here = eat;
	    for (int i = 0; i < n && p[i] > eat; ++i) {
		here += ((p[i] - 1) / eat);
	    }
	    ret = min(ret, here);
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
        cerr << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int D;
        {
            stringstream A(s);
            A >> D;
        }
	vector<int> p(D);
	getline(cin, s);
	stringstream A(s);
	for (int i = 0; i < D; ++i) {
	    A >> p[i];
	}
        ret_t ret = solver.solve(D, p);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
