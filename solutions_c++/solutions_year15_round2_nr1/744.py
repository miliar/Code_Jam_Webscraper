
#include <bits/stdc++.h>
using namespace std;

int reverse(int n) {
    int res = 0;
    while (n) {
        res = res * 10 + (n % 10);
        n /= 10;
    }
    return res;
}

main() {
    int T, N, i;
    int *A = new int[1000001];
    A[1] = 1;
    for (i = 1; i < 1000000; i++) {
        int a = i + 1, b = reverse(i), n = A[i] + 1;
        if (n < A[a] || !A[a]) A[a] = n;
        if (n < A[b] || !A[b]) A[b] = n;
    }
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> N;
        cout << "Case #" << (i + 1) << ": " << A[N] << endl;
    }
}
