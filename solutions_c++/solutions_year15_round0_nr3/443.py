#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef bool ret_t;

char quatmult(char a, char b) {
    char ret = 'h'; // sign = 1 (represented by 'h')
    if ((a & 3) && (b & 3)) {
	int d = (a & 3) - (b & 3);
	if (d != -1 && d != 2)
	    ret = 'l';
    }
    //if ((a & 3) == 0) return (b & 3) ^ ret;
    //if ((b & 3) == 0) return (a & 3) ^ ret;
    return ((a ^ b) & 7) ^ ret;
}

class Solver {
public:
    ret_t solve(ll n, ll times, string s) {
	if (n == 1) return false; // only +/- 1
	if (times == 1 && n < 3) return false; // no 3 nonempty substrings

	char T[10000][8];
	for (int j = 0; j < 8; ++j) T[0][j] = quatmult((char)('h' + j), s[0]);
	for (int i = 1; i < n; ++i) {
	    for (int j = 0; j < 8; ++j)
		T[i][j] = quatmult(T[i-1][j], s[i]);
	}

	if (T[n-1][0] == 'h') return false; // doesn't make ijk = -1
	if (T[n-1][0] == 'l') {
	    if (times % 2 != 1) return false; // odd powers make ijk
	}
	else {
	    if (times % 4 != 2) return false;
	}

	ll it = 0;
	int found = 0;
	char seek = 'i';
	int i = 0;
	int j = 0;
	vector<bool> vis(8, false);
	while (true) {
	    if (T[i][j] == seek) {
		++found;
		if (found == 2) return true;
		seek = 'k'; // ij = k
		for (int k = 0; k < 8; ++k) vis[k] = false;
	    }

	    ++i;
	    if (i == n) {
		++it;
		if (it == times) return false;
		j = (int)(T[n-1][j] - 'h');
		if (vis[j]) return false;
		vis[j] = true;
		i = 0;
	    }
	}
	return false;
    }
};

int main(int argc, char ** argv) {
    {
	for (char a = 'h'; a <= 'o'; ++a) {
	    for (char b = 'h'; b <= 'o'; ++b) {
		cerr << ' ' << quatmult(a, b);
	    }
	    cerr << endl;
	}
    }
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
        ll len, times; string s2;
        {
            stringstream A(s);
            A >> len >> times;
        }
	getline(cin, s);
	{
	    stringstream A(s);
	    A >> s2;
	}
        ret_t ret = solver.solve(len, times, s2);

        // *** give output ***
        cout << "Case #" << no << ": " << (ret ? "YES" : "NO") << endl; // one line
	//cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
