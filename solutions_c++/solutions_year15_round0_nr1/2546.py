#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
using namespace std;
typedef long long int ll;
typedef long double ld;

class CaseSolver {
    public:
        void static precompute();
        void read(istream& in);
        void solve();
        void write(ostream& out);
    private:
        int s;
        string audience;
        int added;
};

void CaseSolver::precompute() {
}

void CaseSolver::read(istream& in) {
    in >> s >> audience;
}

void CaseSolver::solve() {
    int current = 0;
    added = 0;
    for (int i = 0; i <= s; ++i) {
        if (current < i) {
            ++added;
            ++current;
        }
        int a = audience[i] - '0';
        current += a;
    }
}

void CaseSolver::write(ostream& out) {
    out << added;
}


int main() {
    CaseSolver::precompute();
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        CaseSolver caseSolver;
        caseSolver.read(cin);
        caseSolver.solve();
        cout << "Case #" << testCase << ": ";
        caseSolver.write(cout);
        cout << "\n";
	}
}
