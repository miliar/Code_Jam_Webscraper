#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef string ret_t;

class Solver {
public:
    ret_t solve(int N, int M, vector<vector<int> > a) {
        vector<int> r(N, 0);
	vector<int> c(M, 0);
	for (int i = 0; i < N; ++i) {
	    for (int j = 0; j < M; ++j) {
		r[i] = max(r[i], a[i][j]);
		c[j] = max(c[j], a[i][j]);
	    }
	}
	for (int i = 0; i < N; ++i) {
	    for (int j = 0; j < M; ++j) {
		if (a[i][j] != min(r[i], c[j]))
		    return "NO";
	    }
	}
	return "YES";
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
        int N, M;
	vector<vector<int> > a;
        {
            stringstream A(s);
            A >> N >> M;
	    a = vector<vector<int> >(N, vector<int>(M, 0));
	    for (int i = 0; i < N; ++i) {
		getline(cin, s);
		stringstream A(s);
		for (int j = 0; j < M; ++j) A >> a[i][j];
	    }
        }
        ret_t ret = solver.solve(N, M, a);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
