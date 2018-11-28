
#include <iostream>
#include <vector>

using namespace std;

main() {
    int T, N, i, j;
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> N;
        vector<int> A(N);
        for (j = 0; j < N; j++)
            cin >> A[j];
        int res1 = 0, res2 = 0, rate = 0;
        for (j = 1; j < N; j++)
            if (A[j] < A[j - 1]) {
                int t = A[j - 1] - A[j];
                res1 += t;
                if (t > rate) rate = t;
            }
        for (j = 0; j < N - 1; j++) {
            res2 += std::min(A[j], rate);
        }
        cout << "Case #" << (i + 1) << ": " << res1 << " " << res2 << endl;
    }
}
