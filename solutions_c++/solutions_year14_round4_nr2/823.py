#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t;
int n;
int a[1111];

int main() {
    cin >> t;
    for (int x = 1; x <= t; x++) {
        cin >> n;
        vector<int> v;
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            v.push_back(a[i]);
        }
        sort(v.begin(), v.end());
        int c = 0;
        for (int i = 0; i < n; i++) {
            int k = -1;
            for (int j = 0; j < n; j++) {
                if (a[j] == v[i]) {k = j; break;}
            }
            int c1 = 0;
            for (int j = k-1; j >= 0; j--) {
                if (a[j] > a[k]) c1++;
                else break;
            }
            int c2 = 0;
            for (int j = k+1; j < n; j++) {
                if (a[j] > a[k]) c2++;
                else break;
            }
            if (c1 < c2) {
                c += c1;
                for (int j = k-1; j >= 0; j--) {
                    if (a[j] > a[j+1]) swap(a[j], a[j+1]);
                    else break;
                }
            } else {
                c += c2;
                for (int j = k+1; j < n; j++) {
                    if (a[j] > a[j-1]) swap(a[j], a[j-1]);
                }
            }
        }
        cout << "Case #" << x << ": " << c << "\n";
    }
}
