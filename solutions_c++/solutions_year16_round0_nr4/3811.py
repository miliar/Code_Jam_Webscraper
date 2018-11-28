#include <cassert>
#include <iostream>

using namespace std;

int  main() {
        size_t T, K, C, S;
        cin >> T;
        for (size_t i {1}; i <= T; ++i) {
                cin >> K >> C >> S;
                assert(K == S);
                cout << "Case #" << i << ":";
                for (size_t j {1}; j <= K; ++j) {
                        cout << ' ' << j;
                }
                cout << '\n';
        }
        return 0;
}