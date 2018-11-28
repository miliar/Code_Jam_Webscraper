#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef double ret_t;

class Solver {
public:
    ret_t solve(int n, int x, int y) {
	if (x < 0)
	    x = -x;
	int inLayer = (x + y) / 2 + 1;
	int layers = 0;
	int needs;
	while (true) {
	    needs = 4 * layers + 1;
	    if (n < needs)
		break;
	    n -= needs;
	    ++layers;
	}
	if (inLayer <= layers)
	    return 1.0;
	if (inLayer > layers + 1)
	    return 0.0;
	if (x == 0)
	    return 0.0;
	cerr << " [layers = " << layers << ", n = " << n << "] ";
	int side = 2 * layers;
	vector<double> p(side + 1, 0);
	p[0] = 1.0;
	for (int i = 0; i < side && n > 0; ++i, --n) {
	    for (int j = i; j >= 0; --j) {
		double halfp = p[j] / 2;
		p[j+1] += halfp;
		p[j] = halfp;
	    }
	}
	for (int i = 0; i < side && n > 0; ++i, --n) {
	    for (int j = side - 1; j > i; --j) {
		double halfp = p[j] / 2;
		p[j+1] += halfp;
		p[j] = halfp;
	    }
	    p[i+1] += p[i];
	    p[i] = 0.0;
	}
	double ret = 0;
	for (int j = side; j > y; --j)
	    ret += p[j];
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
        int n, x, y;
        {
            stringstream A(s);
            A >> n >> x >> y;
        }
        ret_t ret = solver.solve(n, x, y);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
