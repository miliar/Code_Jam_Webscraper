#include <bits/stdc++.h>

using namespace std;

string solve() {
    string cakes;
    int k;
    cin >> cakes >> k;

    int answer = 0;
    for (int i = 0; i + k - 1 < int(cakes.length()); i++) {
        if (cakes[i] == '-') {
            answer++;
            for (int j = i; j < i + k; j++) {
                cakes[j] = cakes[j] == '-' ? '+' : '-';
            }
        }
    }

    if (find(cakes.begin(), cakes.end(), '-') != cakes.end()) {
        return "IMPOSSIBLE";
    } else {
        return to_string(answer);
    }
}

int main() {
    int t;
    cin >> t;

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": " << solve() << endl;
    }
}
