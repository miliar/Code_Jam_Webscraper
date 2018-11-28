#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef ll ret_t;
const ll MOD = 1000000007;
ll dp[101][5];

class Solver {
public:
    int r, c;
    void add(int i, int j, ll num) {
	if (i == r) {
	    dp[i][j] += num;
	    dp[i][j] %= MOD;
	}
	else if (i + 2 <= r) {
	    dp[i+2][j] += num;
	    dp[i+2][j] %= MOD;
	}
    }
    ret_t solve(int _r, int _c) {
	ret_t ret;
	r = _r; c = _c;
	for (int i = 0; i <= r; ++i)
	    for (int j = 0; j < 5; ++j)
		dp[i][j] = 0;
	dp[0][0] = 1;
	dp[2][0] = 1;
	// meaning of j: lcm of periods is 1,4,3,6,12
	for (int i = 0; i < r; ++i) {
	    for (int j = 0; j < 5; ++j) {
		// row of 2s
		add(i + 1, j, dp[i][j]);
	    }
	    // 1 2 2
	    // 1 2 2
	    if (c % 3 == 0) {
		add(i + 2, 2, dp[i][0] + 3*dp[i][2]);
		add(i + 2, 3, 3*dp[i][3]);
		add(i + 2, 4, dp[i][1] + 3*dp[i][4]);
	    }
	    // 1 1 2 2 2 2
	    // 2 2 2 1 1 2
	    if (c % 6 == 0) {
		add(i + 2, 3, dp[i][0] + 3*dp[i][2] + 6*dp[i][3]);
		add(i + 2, 4, 2*dp[i][1] + 6*dp[i][4]);
	    }
	    // 1 2 2 2
	    // 1 2 1 2
	    // 2 2 1 2
	    if (c % 4 == 0) {
		add(i + 3, 1, dp[i][0] + 4*dp[i][1]);
		add(i + 3, 4, dp[i][2] + 2*dp[i][3] + 4*dp[i][4]);
	    }
	    // (all separated by two rows of 3s)
	}
	ret = 0;
	for (int j = 0; j < 5; ++j)
	    ret += dp[r][j];
	ret %= MOD;
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
        ret_t ret = solver.solve(r, c);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
