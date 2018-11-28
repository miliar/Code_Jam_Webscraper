#include <iostream>

using namespace std;


int main() {
    long long t, k, c, s;


    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> k >> c >> s;
    
        cout << "Case #" << i << ":";
    
        if (s*c < k) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        for (long long cur = 0; cur < k; ) {
            long long num = 0; 
            long long r = 1;
           for (long long j = 0; j < c; j++) {
                if (cur >= k)
                    break;
                num += r*cur;
                r *= k;
//                cout << cur << " "<<k << " "<<num << endl;
                cur++;
            }
            cout << " "<< num+1;
        }
        cout << endl;
    }
}
