#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>

using namespace std;

typedef long long ll;
typedef double ret_t;

class Solver {
public:
    ret_t solve(int n, double V, vector<double> R, vector<double> C) {
	bool hi = false;
	bool lo = false;
	for (int i = 0; i < n; ++i) {
	    if (C[i] < 1e-9)
		lo = true;
	    if (C[i] > -1e-9)
		hi = true;
	}
	if (!hi && !lo)
	    return -1;

	vector<pair<double, double> > h;
	h.push_back(make_pair(0.0, 0.0));
	for (int i = 0; i < n; ++i) {
	    int sz = h.size();
	    for (int j = 0; j < sz; ++j) {
		h.push_back(make_pair(h[j].first + R[i], h[j].second + C[i]));
	    }
	}
	int sz = h.size();

	ret_t ret = 1e9;
	for (int i = 1; i < sz; ++i) {
	    double R1 = h[i].first;
	    double C1 = h[i].second;
	    //if (C1 >= -1e-9 && C1 <= 1e-9) {
	    if (fabs(C1) < 1e-9) {
		ret = min(ret, V / R1);
	    }
	    else for (int j = 0; j < i; ++j) {
		double R2 = h[j].first;
		double C2 = h[j].second;
		if (fabs(C1 - C2) < 1e-9)
		    continue;
		double coef2 = C2 / (C2 - C1);
		double coef1 = 1 - coef2;
		if (coef2 < 0 || coef1 < 0)
		    continue;
		ret = min(ret, V / (coef1 * R2 + coef2 * R1));
	    }
	}

	if (ret > 1e8)
	    ret = -1;
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
        int n;
	double V, X;
        {
            stringstream A(s);
            A >> n >> V >> X;
        }
	vector<double> R(n);
	vector<double> C(n);
	for (int i = 0; i < n; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> R[i] >> C[i];
	    C[i] -= X;
	    C[i] *= R[i];
	}
        ret_t ret = solver.solve(n, V, R, C);

        // *** give output ***
	cout << "Case #" << no << ": ";
	if (ret < -.5)
	    cout << "IMPOSSIBLE" << endl;
	else
	    cout << fixed << setprecision(7) << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
