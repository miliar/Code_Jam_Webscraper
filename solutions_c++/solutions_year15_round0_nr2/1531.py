
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void debug(const vector<int> &A) {
    int n = A.size(), i;
    for (i = 0; i < n; i++)
        cerr << A[i] << (i < n - 1 ? ' ' : '\n');
}

main() {
    int T, D, i, j, k;
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> D;
        vector<int> A(D);
        for (j = 0; j < D; j++)
            cin >> A[j];
        sort(A.begin(), A.end());

        int res = A.back();
        for (j = 1; j < res; j++) {
            int sum = j;
            for (k = 0; k < (int)A.size(); k++)
                sum += (A[k] - 1) / j;
            if (sum < res)
                res = sum;
        }
        cout << "Case #" << (i + 1) << ": " << res << endl;
    }
}
