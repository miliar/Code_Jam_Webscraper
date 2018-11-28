// CPPFLAGS=-std=gnu++11 -O3

#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <cstdlib>
#include <string>
#include <cstdint>

#define D(x) x

using namespace std;

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
    os << "[";
    for (int i = 0; i < vec.size(); i++) {
        if (i > 0) os << ", ";
        os << vec[i];
    }
    return os << "]";
}

int main() {
    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        int N, X;
        cin >> N >> X;

        vector<int> S(N);
        for (int i = 0; i < N; i++) {
            cin >> S[i];
        }

        sort(S.begin(), S.end());
        reverse(S.begin(), S.end());

        int discs = N;
        multiset<int> gaps;
        for (int i = 0; i < N; i++) {
            multiset<int>::iterator it = gaps.lower_bound(S[i]);
            if (it != gaps.end()) {
                gaps.erase(it);
                discs--;
            } else {
                gaps.insert(X-S[i]);
            }
        }

        cout << "Case #" << T << ": ";
        cout << discs;
        cout << endl;
    }
}
