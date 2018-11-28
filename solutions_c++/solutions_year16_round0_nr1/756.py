#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
    long T, N;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N;
        set<char> seen;
        int i;
        for (i = 1; i <= 100; i++) {
            string s = to_string(i * N);
            for (char c : s) seen.insert(c);
            if (seen.size() == 10) break;
        }
        cout << "Case #" << t << ": ";
        if (i == 101) cout << "INSOMNIA" << endl;
        else cout << i * N << endl;;
    }
}
