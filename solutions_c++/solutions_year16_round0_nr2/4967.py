#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i++) {
        string k;
        cin >> k;

        k += '+';
        bool flag = true;
        for (int j = 0; j < k.size(); j++) {
            if (k[j] == '-')
                flag = false;
        }
        int res = 0;
        if (!flag) {
            for (int i = 0; i < k.size() - 1; i++) {
                if (k[i] != k[i + 1])
                    res++;
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }
}