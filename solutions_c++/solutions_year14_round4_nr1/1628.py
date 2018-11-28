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
    ret_t solve(int n, int C, vector<int> a) {
	ret_t ret = 0;
	sort(a.begin(), a.end());
	int i = 0;
	int j = n - 1;
	while (i <= j) {
	    if (i == j) {
		++ret;
		break;
	    }
	    if (a[i] + a[j] <= C) {
		++i;
		--j;
		++ret;
		continue;
	    }
	    else {
		--j;
		++ret;
		continue;
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
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        int n, C;
        {
            stringstream A(s);
            A >> n >> C;
        }
	getline(cin, s);
	stringstream A(s);
	vector<int> a(n);
	for (int i = 0; i < n; ++i) {
	    A >> a[i];
	}
        ret_t ret = solver.solve(n, C, a);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
