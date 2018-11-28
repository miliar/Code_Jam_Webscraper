#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef int ret_t;

class Solver {
public:
    ret_t solve(int a, int n, vector<int> x) {
	sort(x.begin(), x.end());
	int hi = x[x.size()-1];
	vector<vector<int> > dp(n+1, vector<int>(n+1, 0));
	dp[0][0] = a;
	for (int i = 0; i < n; ++i) {
	    for (int j = 0; j <= n; ++j) {
		if (dp[i][j] == 0)
		    continue;
		if (dp[i][j] > hi)
		    dp[i][j] = hi + 1;

		if (x[i] < dp[i][j])
		    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + x[i]);
		if (j < n)
		    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]);
		if (j < n)
		    dp[i][j+1] = max(dp[i][j+1], 2 * dp[i][j] - 1);
	    }
	}
	for (int j = 0; j <= n; ++j)
	    if (dp[n][j] > 0)
		return j;
	return n;
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
        int a, n;
        {
            stringstream A(s);
            A >> a >> n;
        }
	getline(cin, s);
	vector<int> x(n);
	{
	    stringstream A(s);
	    for (int i = 0; i < n; ++i)
		A >> x[i];
	}
        ret_t ret = solver.solve(a, n, x);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
