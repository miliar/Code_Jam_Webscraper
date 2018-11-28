#include <fstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int max_calls;
int tmin;

void solve_r(const vector<int>& p, bool eat, int call) {
    if (p.empty() || call == max_calls)
        return;

    int pmax = p[0];
    // Let eat until no more pancakes left?
    if (call + pmax < tmin)
        tmin = call + pmax;

    vector<int> pp = p;
    if (eat) {
        transform(pp.begin(), pp.end(), pp.begin(), [](const int d){ return d - 1; });
        pp.erase(remove(pp.begin(), pp.end(), 0), pp.end());
    }
    else {
        // Split the dish with more pancakes
        if (pmax % 2 == 0) {
            int nd = pmax / 2;
            pp[0] = nd;
            pp.push_back(nd);
        }
        else {
            int nd1 = int(floor(pmax / 2.0));
            int nd2 = nd1 + 1;
            if (nd1 > 1) {
                nd1--;
                nd2++;
            }
            pp[0] = nd1;
            pp.push_back(nd2);
        }
    }
    sort(pp.begin(), pp.end(), greater<int>());
    solve_r(pp, true, call + 1);
    solve_r(pp, false, call + 1);
}

void solve(const vector<int>& p) {
    max_calls = p[0];
    tmin = p[0];
    solve_r(p, true, 0);
    solve_r(p, false, 0);
}

int main() {
    ifstream input("B-small-attempt1.in");
    ofstream output("B-small-attempt1.out");

    int T, tc = 1;
    input >> T;
    while (T--) {
        int D;
        input >> D;

        vector<int> p;
        for (int i = 0; i < D; ++i) {
            int pi;
            input >> pi;
            p.push_back(pi);
        }
        sort(p.begin(), p.end(), greater<int>());

        solve(p);

        output << "Case #" << tc++ << ": " << tmin << endl;
    }
}