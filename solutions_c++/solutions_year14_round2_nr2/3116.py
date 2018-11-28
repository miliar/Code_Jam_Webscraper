#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void solve(unsigned long long int A, unsigned long long int B, unsigned long long int K) {
    unsigned long long int a,b;
    unsigned long long int ans = 0;

    for (a=0; a<A; a++) {
        for (b=0; b<B; b++) {
            if ((a&b) < K) {
                ans++;
            }
        }
    }

    cout << ans << endl;
}

int main() {
    int T, prob=1;
    unsigned long long int A, B, K;

    for (cin >> T; T--;) {
        cin >> A >> B >> K;

        cout << "Case #" << prob++ << ": ";
        solve(A, B, K);
    }
}
