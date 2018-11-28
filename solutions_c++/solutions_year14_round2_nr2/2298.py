#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <locale>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int T;
    cin >> T;

    for(int t = 1; t <= T; ++t) {
        int A, B, K;
        cin >> A >> B >> K;

        int result = 0;
        for(int i = 0; i < A; ++i) {
            for(int j = 0; j < B; ++j) {
                if((i & j) < K) {
                    ++result;
                }
            }
        }

        cout << "Case #" << t << ": ";
        cout << result << endl;
    }
    
    return 0;
}
