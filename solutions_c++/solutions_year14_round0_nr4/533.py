#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int T;
int N;
int main() {
    //freopen("D-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);

    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        float *A = new float[N];
        float *B = new float[N];
        float x;
        for (int j = 0; j < N; j++) {
            cin >> x;
            A[j] = x;
        }
        for (int j = 0; j < N; j++) {
            cin >> x;
            B[j] = x;
        }
        sort(A, A + N);
        sort(B, B + N);
        int k = 0;
        int s = 0;
        for (int j = 0; j < N; j++) {
            if (k < N && B[k] < A[j]) {
                    s++; k++;
            }
        }
        k = N - 1;
        int t = 0;
        int n = 0;
        for (int j = N - 1; j >= 0; j--) {
            if (k >= n && B[k] < A[j]) {
                t++;
                n++;
            }
            else if (k >= n && B[k] > A[j]) {
                k--;
            }
        }
        cout << "Case #" << i << ": " << s << " " << t << endl;
    }
}
