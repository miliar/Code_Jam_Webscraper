
#include <iostream>
#include <string>

using namespace std;

main() {
    int T, N, i, j;
    cin >> T;
    for (i = 0; i < T; i++) {
        string S;
        cin >> N >> S;
        int res = 0, sum = 0;
        for (j = 0; j <= N; j++) {
            if (sum < j) { res += j - sum; sum = j; }
            sum += S[j] - '0';
        }
        cout << "Case #" << (i + 1) << ": " << res << endl;
    }
}
