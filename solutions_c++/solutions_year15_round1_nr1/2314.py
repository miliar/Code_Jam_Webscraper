#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;

int main() {
    int T; cin >> T;
    for (int i = 0; i < T; ++i) {
        int N; cin >> N; vi m;
        for (int j = 0; j < N; ++j) { int mi; cin >> mi; m.push_back(mi); }


        int min_a = 0;
        for (int j = 0, n = m.size(); j < n - 1; ++j) {
            if (m[j] > m[j + 1]) { min_a += m[j] - m[j + 1]; }
        }

        int min_b = 0;
        int l = 0;
        for (int j = 0, n = m.size(); j < n - 1; ++j) {
            l = max(l, m[j] - m[j + 1]);
        }
        for (int j = 0, n = m.size(); j < n - 1; ++j) {
            min_b += min(l, m[j]);
        }

        cout << "Case #" << (i + 1) << ": " << min_a << " " << min_b << endl;
    }

    return 0;
}
