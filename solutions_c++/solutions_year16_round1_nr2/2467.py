#include <algorithm>
#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int hash[2501] = {0};
        int N; cin >> N;
        for (int j = 0; j < N*(2*N-1); ++j) {
            int n; cin >> n;
            ++hash[n];
        }
        vector<int> out; out.reserve(N);
        for (int i = 0; i < 2501; ++i) {
            if (hash[i] & 1) out.push_back(i);
        }
        cout << "Case #" << i+1 << ": ";
        copy(begin(out), end(out), ostream_iterator<int>(cout, " "));
        cout << "\n";
    }
    return 0;
}