#include <iostream>
#include <algorithm>

using namespace std;

typedef long double ld;

#define MAXN 1010

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;

        ld N[MAXN], K[MAXN];
        for (int j = 0; j < n; j++) {
            cin >> N[j];
        }

        for (int j = 0; j < n; j++) {
            cin >> K[j];
        }

        int warScore = 0, deceitfulWarScore = 0;
        sort(N, N + n);
        sort(K, K + n);

        if (false) {
            cout << "N: " << endl;
            for (int j = 0; j < n; j++) {
                cout << N[j] << ", ";
            }
            cout << endl;

            cout << "K: " << endl;
            for (int j = 0; j < n; j++) {
                cout << K[j] << ", ";
            }
            cout << endl;
        }

        int get = n - 1;
        for (int j = n - 1; j >= 0; j--) {
            if (N[j] > K[get]) {
                warScore++;
            } else {
                get--;
            }
        }

        int r = n - 1, l = 0;
        for (int j = 0; j < n; j++) {
            if (N[j] < K[l]) {
                r--;
            } else {
                l++;
                deceitfulWarScore++;
            }
        }

        cout << "Case #" << i << ": " << deceitfulWarScore << " " << warScore << endl;
    }

    return 0;
}
