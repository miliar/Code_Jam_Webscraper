#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef ll ret_t;

class Solver {
public:
    ret_t solve(ll A, ll B, ll K) {
	ret_t ret = 0;
	for (int a = 0; a < A; ++a)
	    for (int b = 0; b < B; ++b)
		if ((a & b) < K) ++ret;
	return ret;
	/*
	ret_t ret = 0;
	if (K >= A || K >= B) return A * B;
	for (int k = 29; k >= 0; --k) {
	    if (K & (1 << k)) {
		int lo = (K & ~((1 << (k + 1)) - 1));
		int hi = lo + (1 << k);
		ret += 
	    }
	}
	return ret;*/
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
        int a, b, k;
        {
            stringstream A(s);
            A >> a >> b >> k;
        }
        ret_t ret = solver.solve(a, b, k);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
