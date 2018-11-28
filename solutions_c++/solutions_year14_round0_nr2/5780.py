#include <algorithm>
#include <stack>
#include <bitset>
#include <cassert>
#include <map>
#include <string>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))
#define REP(i,n) for(int (i) = 0; (i) < (n); ++(i))
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define square(a) (a)*(a)
#define mp(a,b) make_pair((a),(b))

const int oo = numeric_limits<int>::max();

int main() {
    int T;
    double C, F, X;
    cin >> T;
    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(7);
    for (int t = 1; t <= T; t++) {
        cin >> C >> F >> X;
        double time = 0;
        double per_sec = 2;
        double best_time = numeric_limits<double>::max();
        for (int f = 0; f < X; f++) {
            double time_farm = C/per_sec,
                   time_win = X/per_sec;

            //cout << time << " " << time_win<<endl;
            best_time = min(best_time, time+time_win);
            time += time_farm;
            per_sec += F;
        }
        cout << "Case #" << t << ": " << best_time << endl;
    }
}
