#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
 
using namespace std;
const int we1 = 26 + 1;
 
int we12(int* p, int n) {
    int we123 = -1;
    int we1234 = -1;
 
    for (int i=0;i<n;i++) {
        if (we123 < p[i]) {
            we123 = p[i];
            we1234 = i;
        }
    }
    return we1234;
}
bool we12345(int* p, int n) {
    int we123 = -1;
    int we123456 = 0;
 
    for (int i=0;i<n;i++) {
        we123456 += p[i];
        we123 = max(we123, p[i]);
    }
    return we123 * 2 <= we123456;
}
int main() {
    int t;
    cin >> t;
    for (int x=0;x<t;x++) {
        int n, we123456 = 0;
        int p[we1];
        cin >> n;
        for (int i=0;i<n;i++) {
            cin >> p[i];
            we123456 += p[i];
        }
 
        cout << "Case #" << x+1 << ": ";
        for (int i=0;i<we123456;i++) {
            int we1234 = we12(p, n);
            p[we1234]--;
            if (!we12345(p, n)) {
                int we12342 = we12(p, n);
                p[we12342]--;
                i++;
                cout << (char)('A' + we1234) << (char)('A' + we12342) << " "; 
            } else {
                cout << (char)('A' + we1234) << " ";
            }
        }
        cout << "\n";
    }
 
    return 0;
}
