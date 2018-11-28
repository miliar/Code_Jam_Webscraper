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
    ret_t solve(vector<string> a, int n) {
	ret_t ret = 0;
	vector<int> ind(n, 0);
	vector<int> num;
	while (ind[0] < a[0].size()) {
	    char c = a[0][ind[0]];
	    num = vector<int>(n, 0);
	    for (int i = 0; i < n; ++i) {
		while (ind[i] < a[i].size() && a[i][ind[i]] == c)
		    ++ind[i], ++num[i];
	    }
	    sort(num.begin(), num.end());
	    if (num[0] == 0)
		return -1;
	    for (int i = 0; i < n; ++i)
		ret += abs(num[i] - num[n/2]);
	}
	for (int i = 0; i < n; ++i)
	    if (ind[i] != a[i].size())
		return -1;
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
	stringstream A(s);
	int n;
	A >> n;
	vector<string> a(n);
	for (int i = 0; i < n; ++i) {
	    getline(cin, s);
	    stringstream A(s);
	    A >> a[i];
	}
	ret_t ret = solver.solve(a, n);
	
	// *** give output ***
	cout << "Case #" << no << ": ";
	if (ret >= 0)
	    cout << ret << endl; // one line
	else
	    cout << "Fegla Won" << endl;
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
	//cout << "Case #" << no << ":\n" << ret; // multi-line
	//cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
