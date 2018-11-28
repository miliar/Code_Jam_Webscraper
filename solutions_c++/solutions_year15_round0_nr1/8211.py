#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        int m;
        cin >> m;
        
        int result = 0;
        int current = 0;
        char c;
        cin.get(c);
        for (int j = 0; j <= m; ++j) {
            cin.get(c);
            c -= 48;
            if (c > 0 && j - current - result > 0) {
                result += j - current - result;
            }
            current += c;
        }

        cout << "Case #" << i + 1 << ": " << result << "\n";
    }
}
