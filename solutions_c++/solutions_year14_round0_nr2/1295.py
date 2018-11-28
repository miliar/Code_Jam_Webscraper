#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef double ret_t;

class Solver {
public:
  ret_t solve(double c, double f, double x) {
    ret_t ret = x;
    double rate = 2.0;
    double time = 0.0;
    while (true) {
      double finish = time + (x / rate);
      if (finish < ret) {
	ret = finish;
	time += (c / rate);
	rate += f;
      }
      else
	break;
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
        double c, f, x;
        {
            stringstream A(s);
            A >> c >> f >> x;
        }
        ret_t ret = solver.solve(c, f, x);

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
