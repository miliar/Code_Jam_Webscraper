#include <iostream>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B_large.out", "w", stdout);
    int t;
    cin >> t;
    for (int j = 0; j < t; ++j) {
        string data;
        cin >> data;
    
        char cur = data[0];
        int res = 0, n = data.length();
        for (int i = 1; i < n; ++i)
            if (data[i] != cur) {
                res++;
                cur = data[i];
            }

        if (data[n - 1] == '-')
            res++;

        cout << "Case #" << j + 1 << ": " << res << endl;
    }
    return 0;
}