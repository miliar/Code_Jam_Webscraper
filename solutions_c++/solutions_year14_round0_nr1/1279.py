#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef int ret_t;

class Solver {
public:
  ret_t solve(vector<vector<int> > c, vector<int> a) {
    ret_t ret = -1;
    vector<int> count(17, 0);
    for (int i = 0; i < 2; ++i)
      for (int j = 0; j < 4; ++j) {
	count[c[i][4*(a[i]-1)+j]]++;
      }
    for (int i = 1; i <= 16; ++i) {
      if (count[i] == 2) {
	if (ret < 0)
	  ret = i;
	else
	  ret = 0;
      }
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
	vector<vector<int> > c(2, vector<int>(16, 0));
        vector<int> a(2, 0);
        for (int i = 0; i < 2; ++i) {
	  getline(cin, s);
	  stringstream A(s);
	  A >> a[i];
	  for (int j = 0; j < 4; ++j) {
	    getline(cin, s);
	    stringstream A(s);
	    for (int k = 0; k < 4; ++k) A >> c[i][4*j+k];
	  }
        }
        ret_t ret = solver.solve(c, a);

        // *** give output ***
        cout << "Case #" << no << ": ";
	if (ret > 0)
	  cout << ret;
	else if (ret == 0)
	  cout << "Bad magician!";
	else
	  cout << "Volunteer cheated!";
	cout << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
