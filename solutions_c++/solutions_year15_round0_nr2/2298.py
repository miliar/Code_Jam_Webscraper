#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    cin >> T;
    for (int test = 0; test < T; test++) {
        int N;
        cin >> N;
        vector<int> ar;
        for (int i = 0; i < N; i++) {
            int a;
            cin >> a;
            ar.push_back(a);
        }
        sort(ar.begin(), ar.end());
        reverse(ar.begin(), ar.end());
        int bestTime = 1000;
        for (int i = 1; i <= ar[0]; i++) {
            int k = 0;
            for (int j = 0; j < N; j++) {
                if (ar[j] <= i)
                    break;
                else
                    k += ((ar[j] + i - 1) / i) - 1;
            }
            if (bestTime > k + i) {
                bestTime = k + i;
            }
        }
        cout << "Case #" << test + 1 << ": " << bestTime << endl;
    }
    return 0;
}

