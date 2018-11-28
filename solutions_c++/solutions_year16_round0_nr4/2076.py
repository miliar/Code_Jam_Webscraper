
#include <vector>
#include <iostream>
using namespace std;

bool checkValid(int K, int C, int S) {
    return K <= C*S;
}

vector<long> calculateValid(int K, int C, int S) {
    vector<long> ret = {};
    if (!checkValid(K, C, S)) return ret;

    vector<long> KCs(C, 0);
    long N = 1;
    for (int i = 0; i < C; ++i) {
        KCs[i] = N;
        N *= K;
    }

    for (int j = 0; j < min(S, (K%C)?(K/C+1):(K/C)); ++j) {
        int start = j * C;
        long num = 0;
        for (int i = 0; i < C; ++i) {
            if (start + i < K)
                num += (start + i) * KCs[C-1-i];
        }
        ret.push_back(num+1);
    }
    return ret;
}

int main(void) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int K, C, S;
        cin >> K >> C >> S;
        vector<long> res = calculateValid(K, C, S);
        cout << "Case #" << i+1 <<": ";
        if (res.empty()) cout << "IMPOSSIBLE" << endl;
        else {
            for (int j = 0; j < res.size(); ++j) {
                cout << res[j] << " ";
            }
            cout << endl;
        }
    }
    return 1;
}
