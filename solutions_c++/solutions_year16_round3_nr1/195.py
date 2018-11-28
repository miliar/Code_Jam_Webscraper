#include <bits/stdc++.h>

using namespace std;

void solution() {
    int n;
    cin >> n;
    vector <pair <int, char>> alph(n);
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        alph[i] = {a, 'A' + i};
    }
    sort(alph.begin(), alph.end());
    reverse(alph.begin(), alph.end());
    while (alph[0].first > alph[1].first) {
        alph[0].first--;
        cout << alph[0].second << ' ';
    }
    for (int i = 2; i < n; i++) {
        while (alph[i].first > 0) {
            alph[i].first--;
            cout << alph[i].second << ' ';
        }
    }
    while (alph[0].first > 0) {
        alph[0].first--;
        cout << alph[0].second << alph[1].second << ' ';
    }
}

int  main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        solution();
        cout << '\n';
    }
    return 0;
}
