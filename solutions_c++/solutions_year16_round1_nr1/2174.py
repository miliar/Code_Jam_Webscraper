#include <iostream>
#include <vector>
#include <string>

#include <gmpxx.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T;) {
        string S, beginning = "", end = "";
        cin >> S;
        vector<int> M;
        M.reserve(S.length());
        M.push_back(0);
        for (int j = 1; j < S.length(); ++j) {
            if (S[j] >= S[M[j - 1]]) {
                M.push_back(j);
            } else {
                M.push_back(M[j - 1]);
            }
        }
        int endIndex = S.length();
        while (endIndex) {
            int nextEI = M[endIndex - 1];
            beginning += S[nextEI];
            end = S.substr(nextEI + 1, endIndex - (nextEI + 1)) + end;
            endIndex = nextEI;
        }
        cout << "Case #" << (++i) << ": " << beginning << end << endl;
    }
    return 0;
}
