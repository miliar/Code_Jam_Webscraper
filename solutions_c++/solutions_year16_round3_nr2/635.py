#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    long long T, B, M, n_case = 1;
    cin >> T;
    while (T--) {
        cin >> B >> M;
        std::cout << "Case #" << n_case++ << ": ";
        int tmp = 0;
        long long sm = 1;
        sm <<= B-2;
        if (sm < M) {
            std::cout << "IMPOSSIBLE" << std::endl;
            continue;
        }
        vector<string> res (B, string(B, '0'));
        for (int i = 1; i < B-1; i++) {
            std::fill (res[i].begin()+i+1, res[i].end(), '1');
        }
        res[0].back() = '1';
        M--;
        for (int i = B-2; i > 0; i--, M >>= 1) {
            if (M&1) res[0][i] = '1';
        }
        std::cout << "POSSIBLE" << std::endl;
        for (auto& s : res)
            std::cout << s << std::endl;
    }

    return 0;
}
