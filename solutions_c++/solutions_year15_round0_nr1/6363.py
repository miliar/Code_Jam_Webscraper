#include <iostream>
#include <string>
using namespace std;

int main() {
    int n; cin >> n;
    for (int c = 1; c <= n; c++) {
        int sum = 0;
        int sol = 0;
        int k;
        string s; cin >> k >> s;
        for (int i = 0; i < s.size(); i++) {
            int u = s[i] - '0';
            if (sum < i && u) {
                sol += i - sum;
                sum += i - sum;
            }
            sum += u;
        }
        cout << "Case #" << c << ": " << sol << endl;
    }
    return 0;
}
