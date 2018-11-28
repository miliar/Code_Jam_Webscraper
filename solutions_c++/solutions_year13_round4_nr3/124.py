#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef vector<int> ret_t;

class Solver {
public:
    int n;
    vector<string> g;
    void setle(int i, int j) {
	g[i][j] = '<';
	g[j][i] = '>';
    }
    void add(vector<int> A, bool isA) {
	for (int i = 0; i < n; ++i) {
	    int lastpre = -1;
	    for (int j = (isA ? 0 : n-1); isA ? (j < i) : (j > i); isA ? ++j : --j) {
		if (A[j] >= A[i]) setle(i, j);
		if (A[j] == A[i] - 1) lastpre = j;
	    }
	    if (lastpre >= 0) setle(lastpre, i);
	}
    }
    ret_t solve(int _n, vector<int> A, vector<int> B) {
	n = _n;
	ret_t ret(n, -1);
	g = vector<string>(n, string(n, '?'));
	add(A, true);
	add(B, false);
	/*	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		for (int k = 0; k < n; ++k)
		    if (g[j][i] != '?' && g[j][i] == g[i][k])
		    g[j][k] = g[j][i];*/
	//for (int i = 0; i < n; ++i) cerr << g[i] << endl;
	vector<int> smaller(n, 0);
	for (int i = 0; i < n; ++i)
	    for (int j = 0; j < n; ++j)
		if (g[i][j] == '>') ++smaller[i];
	for (int i = 1; i <= n; ++i) {
	    int j;
	    for (j = 0; j < n && smaller[j] > 0; ++j)
		;
	    ret[j] = i;
	    smaller[j] = n + 1;
	    for (int k = 0; k < n; ++k)
		if (g[j][k] == '<')
		    --smaller[k];
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
	int n;
        {
            stringstream A(s);
            A >> n;
        }
	vector<int> a(n), b(n);
	getline(cin, s);
	{
	    stringstream A(s);
	    for (int i = 0; i < n; ++i) A >> a[i];
	}
	getline(cin, s);
	{
	    stringstream A(s);
	    for (int i = 0; i < n; ++i) A >> b[i];
	}
        ret_t ret = solver.solve(n, a, b);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
	cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl;
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
