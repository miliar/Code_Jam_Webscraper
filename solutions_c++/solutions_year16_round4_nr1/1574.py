#include <bits/stdc++.h>

using namespace std;

inline bool better(char a, char b)
{
    return (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R');
}

inline bool check(vector<char> a)
{
    vector<char> b;
    while (a.size() != 1) {
        b.resize(a.size() / 2);
        for (int j = 0; j < a.size(); j+=2) {
            if (a[j] == a[j+1]) {
                return false;
            } else if (better(a[j], a[j+1])) {
                b[j/2] = a[j];
            } else {
                b[j/2] = a[j + 1];
            }
        }
        a = b;
    }
    return true;
}

void solve(int test_num)
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;

    vector<char> types(1 << n);
    for (int i = 0; i < p; i++) {
        types[i] = 'P';
    }
    for (int i = p; i < p + r; i++) {
        types[i] = 'R';
    }
    for (int i = p + r; i < p + r + s; i++) {
        types[i] = 'S';
    }

    cout << "Case #" << test_num + 1 << ": ";

    do {
        if (check(types)) {
            for (int i = 0; i < types.size(); i++) {
                cout << types[i];
            }
            cout << '\n';
            return;
        }
    } while (next_permutation(types.begin(), types.end()));
    cout << "IMPOSSIBLE" << '\n';;
}

int main()
{
    int T;
    ios_base::sync_with_stdio(false);
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i);
    }
}
