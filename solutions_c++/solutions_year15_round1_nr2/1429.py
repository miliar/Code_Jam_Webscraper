
#include <iostream>
#include <vector>

using namespace std;

main() {
    int T, B, N, i, j;
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> B >> N;
        vector<int> M(B);
        for (j = 0; j < B; j++)
            cin >> M[j];

        double rate = 0;
        for (j = 0; j < B; j++)
            rate += 1.0 / M[j];
        //cout << rate << endl;

        int res, D = 10;
        long long k, t;
        for (res = 0; res < B; res++) {
            t = (N / rate) / M[res];
            for (k = t - D; k <= t + D; k++) {
                if (k < 0) continue;
                long long z = k * M[res], n = 0;
                for (j = 0; j < B; j++) {
                    n += z / M[j] + 1;
                    if (z % M[j] == 0 && j > res) n--;
                }
                //cout << res << ' ' << z << ' ' << n << endl;
                if (n == N) goto end;
            }
        }
end:
        cout << "Case #" << (i + 1) << ": " << (res + 1) << endl;
        if (res == B) cout << "ERROR" << endl;
    }
}
