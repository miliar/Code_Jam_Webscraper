// CPPFLAGS=-std=gnu++11 -O3

#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <cstdlib>
#include <string>
#include <cstdint>
#include <iomanip>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
    os << "[";
    for (int i = 0; i < vec.size(); i++) {
        if (i > 0) os << ", ";
        os << vec[i];
    }
    return os << "]";
}

int main() {
    cout << setprecision(10);

    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        long long N, p, q, r, s;

        cin >> N >> p >> q >> r >> s;

        vector<long long> t(N), sum(N+1);
        long long total = 0;
        for (int i = 0; i < N; i++) {
            t[i] = ((i * p + q) % r) + s;
            total += t[i];
            sum[i+1] = total;
        }
        //D(cerr << t << endl);

        int a_ = lower_bound(sum.begin(), sum.end(), total/3) - sum.begin();
        int b_ = lower_bound(sum.begin(), sum.end(), (2*total)/3) - sum.begin();

        long long best = 0;
        for (int a = max(a_-3, 0); a <= a_+3 && a < N; a++) {
            for (int b = max(b_-3, 0); b <= b_+3 && b < N; b++) {
                long long solveig = max(sum[b]-sum[a], max(sum[a], sum[N]-sum[b]));
                long long arnar = total - solveig;
                best = max(best, arnar);
            }
        }

        double prob = (double) best / (double) total;

        cout << "Case #" << T << ": ";
        cout << prob;
        cout << endl;
    }
}
