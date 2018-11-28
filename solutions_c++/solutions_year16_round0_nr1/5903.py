#include <iostream>
using namespace std;
inline void tick_digits(long long int x, bool *seen) {
    while(x != 0) {
        seen[x % 10] = true;
        x = x / 10;
    }
}

inline bool all(bool * seen, int n) {
    for (int i = 0; i < n; ++i) {
        if (!seen[i]) return false;
    }
    return true;
}
int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        long long int N;
        cin >> N;
        bool seen[10];
        for (int i = 0; i < 10; ++i) {
            seen[i] = false;
        }
        long long int i = 0;
        if (N == 0)  {
            cout << "Case #" << t + 1 << ": INSOMNIA" << endl;
            continue;
        }
        while (!all(seen, 10)) {
            ++i;
            long long int x = N * i;
            tick_digits(x, seen);
        } 

        
        long long int x = N * i;
        cout << "Case #" << t + 1 << ": " << x << endl;  
    }


    return 0;
}
