#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        int k, c, s;
        cin >> k >> c >> s;
        
        cout << "Case #" << i + 1 << ": ";
        /* if (s < (k - c + 1)) cout << "IMPOSSIBLE" << endl;
        else {
            if (c == 1) {
                for (int j = 1; j <= k; j++) {
                    cout << j;
                    if (j < k) cout << " ";
                }
            } else if (k == 1) {
                cout << 1;
            } else {
                if (c > k) {
                    cout << (int) pow(k, c - 2) + k;
                } else {
                    for (long long j = pow(k, c - 1) + k * (c - 2) + c; j <= pow(k, c - 1) + k * (c - 1); j++) {
                        cout << j;
                        if (j < pow(k, c - 1) + k * (c - 1)) cout << " ";
                    }
                }
            }
            
            cout << endl;
        }
        */
        
        for (int j = 1; j <= k; j++) {
            cout << j;
            if (j < k) cout << " " ;
        }
        
        cout << endl;
    }
    
    return 0;
}