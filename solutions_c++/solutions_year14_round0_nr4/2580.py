#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <set>
#include <stdio.h>


using namespace std;

int getScore(double n[], double k[], int N){
    int d = 0;
    for (int i = N-1; i >= 0; i--) {
            if (n[i] > 0) {
                for (int j = i; j >= 0; j--) {
                    if (k[j] > 0 && n[i] > k[j]) {
                        d++;
                        n[i] = k[j] = 0;
                        break;
                    }
                }
            }
        }
    return d;
}

int main(int argc, char** argv) {
    
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int T;

    cin >> T;

    for (int c = 1; c <= T; c++) {
        int N, d = 0, w = 0;
        cin >> N;

        double *n = new double[N];
        double *k = new double[N];
        double *n2 = new double[N];
        double *k2 = new double[N];

        for (int i = 0; i < N; i++) {
            cin >> n[i];
            n2[i] = n[i];
        }
        for (int i = 0; i < N; i++) {
            cin >> k[i];
            k2[i] = k[i];
        }

        sort(n, n + N);
        sort(k, k + N);
        sort(n2, n2 + N);
        sort(k2, k2 + N);
        
        d = getScore(n, k, N);
        
        w = N - getScore(k2, n2, N);
        cout << "Case #" << c << ": " << d << ' ' << w << endl;
    }
    return 0;
}

