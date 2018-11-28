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

bool next_combination(vector<int>& v, int limit) {
    for (int i = 0; i < v.size(); i++) {
        v[i]++;
        if (v[i] == limit) {
            v[i] = 0;
        } else {
            return true;
        }
    }
    return false;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        int M, N;
        cin >> M >> N;

        vector<string> S(M);
        for (int i = 0; i < M; i++) {
            cin >> S[i];
        }
        
        vector<int> assignment(M);
        int worst = 0, worstCombos = 0;
        do {
            vector<set<string>> prefixes(N);
            for (int i = 0; i < M; i++) {
                set<string>& current = prefixes[assignment[i]];
                for (int j = 0; j <= S[i].length(); j++) {
                    current.insert(S[i].substr(0, j));
                }
            }

            int nodes = 0;
            for (int i = 0; i < N; i++) {
                nodes += prefixes[i].size();
            }

            if (nodes > worst) {
                worst = nodes;
                worstCombos = 1;
            } else if (nodes == worst) {
                worstCombos = (worstCombos+1) % 1000000007;
            }
        } while (next_combination(assignment, N));

        cout << "Case #" << T << ": ";
        cout << worst << " " << worstCombos;
        cout << endl;
    }
}
