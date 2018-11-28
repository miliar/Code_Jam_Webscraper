#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ret_t;

class Solver {
public:
    ret_t solve(int n, int p) {
	ll will, could;

	if (p == ((ll)1) << n)
	    will = (((ll)1) << n) - 1;
	else
	{
	    ll test = 0;
	    int i = 0;
	    do {
		++i;
		test += ((ll)1) << (n - i);
	    } while (test < p);
	    will = (((ll)1) << i) - 2;
	}

	{
	    ll test = 0;
	    int i = 0;
	    while (test < p) {
		test += ((ll)1) << i;
		++i;
	    };
	    --i;
	    test -= ((ll)1) << i;
	    could = (test << (n - i));
	}

	ret_t ret;
      	ret.first = will;
	ret.second = could;
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
        int n, p;
        {
            stringstream A(s);
            A >> n >> p;
        }
        ret_t ret = solver.solve(n, p);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
        cout << "Case #" << no << ": " << ret.first << " " << ret.second << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
