#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <fstream>
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long int int64;

int main() {
    ofstream cout("output");
    int t;
    int n, j;
    cin >> t;
    cin >> n >> j;
    n /= 2;
    cout << "Case #1:\n";
    for (int i = 0; i < j; ++i) {
        vector <int> a(n);
        a[0] = 1;
        for (int k = 1, w = i; k < n - 1; ++k) {
            a[k] = w % 2;
            w /= 2;
        }
        a[n - 1] = 1;
        for (int i = n - 1; i >= 0; --i) {
            cout << a[i];
        }
        for (int i = n - 1; i >= 0; --i) {
            cout << a[i];
        }

        ////

        for (int base = 2; base <= 10; ++base) {
            int64 div = 0;
            for (int k = n - 1; k >= 0; --k) {
                div *= base;
                div += a[k];
            }
            cout << " " << div;
        }
        cout << "\n";
    }
    return 0;
}
