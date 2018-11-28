#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("/Users/linsina/Downloads/B-large.in", "r", stdin);
    freopen("/Users/linsina/Downloads/B-large.out", "w", stdout);
    
    int n;
    cin >> n;
    for (int k = 0; k < n; k++) {
        int result = INT_MAX;
        int time = 0;
        int D;
        cin >> D;
        vector<int> P(D);
        int maxn = 0;
        for (int i = 0; i < D; i++) {
            cin >> P[i];
            maxn = max(maxn, P[i]);
        }
        for (int i = 1; i <= maxn; i++) {
            time = i;
            for (int j = 0; j < D; j++) {
                time += (P[j] + i - 1) / i - 1;
            }
            result = min(result, time);
        }
        cout << "Case #" << k + 1 << ": " << result << endl;
    }
    
    return 0;
}


