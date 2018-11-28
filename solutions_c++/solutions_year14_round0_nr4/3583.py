#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, N;
    vector<double> A, B;
    
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        A.resize(N);
        B.resize(N);

        for (int j = 0; j < N; ++j)
            cin >> A[j];

        for (int j = 0; j < N; ++j)
            cin >> B[j];

        int ans1 = 0, ans2 = N;

        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

/*        for (int j = 0; j < N; ++j)
            cout << A[j] << " ";
        cout << endl;
        for (int j = 0; j < N; ++j)
            cout << B[j] << " ";
        cout << endl;*/

        int j = 0, k = 0;
        while(k < N && j < N) {
            while(k < N && B[k] < A[j]) {
                ++k;
            }

            if (k < N)
                --ans2;

            ++j;
            ++k;
        }

        j = k = 0;
        while (k < N && j < N) {
            while(k < N && A[k] < B[j]) {
                ++k;
            }

            if (k < N)
                ++ans1;
            ++j; ++k;
        }
        
        cout << "Case #" << i << ": " << ans1 << " " << ans2 << endl; 
        A.clear();
        B.clear();
    }
}
