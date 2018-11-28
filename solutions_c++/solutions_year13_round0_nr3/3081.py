#include <iostream>
#include <functional>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool isp(int a) {
    vector<int> n;

    while (a) {
        n.push_back(a % 10);
        a /= 10;
    }


    for (int i = 0; i < n.size(); i++)
        if (n[i] != n[n.size() - i - 1]) {
            return false;
        }

    return true;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int h = 1; h <= t; h++) {
        int a, b, ans = 0;
        cin >> a >> b;

        for (int i = a; i <= b; i++)
            if (isp(i) && (floor(sqrt(1.0 * i)) - floor(sqrt(1.0 * i - 1)) == 1) && isp(floor(sqrt(1.0 * i))))
                ans++;

        cout << "Case #" << h << ": " << ans << endl;
    }
}

    
