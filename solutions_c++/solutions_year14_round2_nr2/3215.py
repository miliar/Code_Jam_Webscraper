#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;


int T, A, B, K;
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i <<": ";
        cin >> A >> B >> K;
        int res = 0;
        for (int j = 0; j < A; j++)
            for (int k = 0; k < B; k++) {
                    int x = j & k;
                if (x < K) res++;
            }

        cout << res << endl;
    }
}
