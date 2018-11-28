#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<ll> ret_t;

class Solver {
public:
    ret_t solve(int n, vector<ll> e, vector<ll> f) {
	ret_t ret;
	int nz = 0;
	{
	    ll t = f[0];
	    while (t > 1) {
		t = (t >> 1);
		++nz;
	    }
	}
	for (int i = 0; i < n; ++i)
	    f[i] = (f[i] >> nz);
	ll lo = e[0];
	ll num = 0;
	for (int i = 0; i < n; ++i)
	    num += f[i];
	vector<ll> d(0);
	vector<ll> g(n, 0);
	g[0] = 1;
	vector<ll> h(g);
	ll gnum = 1;

	int read = 1;
	/*while (num > 1) {
	    while (f[read] == 0)
		++read;
	    ll step = e[read] - lo;
	    for (int i = 0; i < f[read]; ++i)
		d.push_back(step);
	    
		}*/
	while (gnum < num) {
	    while (f[read] == g[read])
		++read;
	    ll step = e[read] - lo;
	    ll times = f[read] - g[read];
	    for (int i = 0; i < times; ++i) {
		d.push_back(step);
	    ll todo = gnum;
	    int j = 1;
	    h = g;
	    for (int i = 0; i < n; ++i) {
		ll numhere = g[i];
		if (numhere == 0)
		    continue;
		while (e[j] < e[i] + step)
		    ++j;
		// (assert here)
		h[j] += numhere;// * times;
		gnum += numhere;// * times;
		todo -= numhere;
		if (todo <= 0) break;
	    }
	    swap(g, h);
	    /*
	    for (int i = 0; i < n; ++i)
		cerr << g[i] << ' ';
		cerr << endl;*/
	    }
	}
	for (int i = 0; i < nz; ++i)
	    ret.push_back(0);
	for (int i = 0; i < d.size(); ++i)
	    ret.push_back(d[i]);
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
        int p;
        {
            stringstream A(s);
            A >> p;
        }
	vector<ll> e(p);
	vector<ll> f(p);
	getline(cin, s);
	{
	    stringstream A(s);
	    for (int i = 0; i < p; ++i)
		A >> e[i];
	}
	getline(cin, s);
	{
	    stringstream A(s);
	    for (int i = 0; i < p; ++i)
		A >> f[i];
	}
        ret_t ret = solver.solve(p, e, f);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
	cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
