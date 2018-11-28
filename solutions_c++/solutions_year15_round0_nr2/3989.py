#include <iostream>
#include <vector>
using namespace std;

int solve() {
    int d, maxim;
    cin >> d;
    maxim = 0;
    vector <int> v(d);
    
    for (int i = 0; i < d; ++i) {
        cin >> v[i];
        maxim = max(v[i], maxim);
    }
    
    int ans = 1000000000;
    for (int i = 1; i <= maxim; ++i) {
        int penalty = 0;
        for (int j = 0; j < d; ++j) {
            if (v[j] <= i) continue;
            penalty += (v[j] / i) - 1;
            if (v[j] % i != 0) ++penalty;
        }
        ans = min(ans, i + penalty);
    }
    
    return ans;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
        cout << "Case #" << i +  1 << ": " << solve() << endl;
}