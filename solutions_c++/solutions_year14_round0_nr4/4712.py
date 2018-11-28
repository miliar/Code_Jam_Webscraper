#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T; cin >> T;
    for (int I = 1; I <= T; I++) {
        int n; cin >> n;
        vector<double> a(n);
        vector<double> b(n);
        for (double &x : a) cin >> x;
        for (double &x : b) cin >> x;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = res; j < n; j++) {
                if (a[i] > b[j]) {
                        res++;
                        break;
                }
            }
        }
        int resb = 0;
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        vector<bool> c(n, false);
        for (int i = 0; i < n; i++) {
            double smallestBeating = -1;
            double smallestAtAll = -1;
            int bi, ci;
            for (int j = 0; j < n; j++) {
                if (!c[j]) {
                    // is free
                    if (b[j] > a[i]) {
                        // is beating
                        if (smallestBeating == -1 || b[j] < smallestBeating) {
                            smallestBeating = b[j];
                            bi = j;
                        }
                    }
                    // is small
                    if (smallestAtAll == -1 || b[j] < smallestAtAll) {
                        smallestAtAll = b[j];
                        ci = j;
                    }
                }
            }           
            if (smallestBeating != -1) {
                c[bi] = true;
            } else {
                c[ci] = true;
                resb++;
            }
        }
        cout << "Case #" << I << ": " << res << " " << resb << endl;
    }
}
