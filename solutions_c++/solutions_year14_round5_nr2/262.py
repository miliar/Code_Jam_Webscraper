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

#define D(x)

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

struct memo_key {
    vector<int> H;
    bool myTurn;

    bool operator==(const memo_key& o) const {
        return (H==o.H) && (myTurn==o.myTurn);
    }
};

size_t key_hash(const memo_key& key) {
    size_t hash = 0;
    for (int i = 0; i < key.H.size(); i++) {
        hash *= 37;
        hash ^= key.H[i];
    }
    hash *= 37;
    if (key.myTurn) hash++;
    return hash;
}

int dfs(const vector<int>& H, const vector<int>& G, int P, int Q, bool myTurn, int depth, unordered_map<memo_key, int, function<decltype(key_hash)>>& memo) {
    memo_key key;
    key.H = H;
    key.myTurn = myTurn;
    unordered_map<memo_key, int, function<decltype(key_hash)>>::const_iterator it = memo.find(key);
    if (it != memo.end()) {
        return it->second;
    }

    for (int i = 0; i < depth; i++) D(cerr << "  ");
    D(cerr << "H=" << H << " myTurn=" << myTurn << endl);

    if (myTurn) {
        bool anyAlive = false;
        int best = 0;

        for (int i = 0; i < H.size(); i++) {
            if (H[i] > 0) {
                anyAlive = true;

                vector<int> H2 = H;
                H2[i] = max(H2[i]-P, 0);
                int reward = 0;
                if (H2[i] <= 0) {
                    for (int i = 0; i < depth+1; i++) D(cerr << "  ");
                    D(cerr << "reward=" << G[i] << endl);
                    reward = G[i];
                }

                best = max(best, reward + dfs(H2, G, P, Q, false, depth+1, memo));
            }
        }
        if (!anyAlive) {
            memo[key] = 0;
            return 0;
        }
        
        best = max(best, dfs(H, G, P, Q, false, depth+1, memo));
        memo[key] = best;
        return best;
    } else {
        vector<int> H2 = H;
        for (int i = 0; i < H.size(); i++) {
            if (H2[i] > 0) {
                vector<int> H2 = H;
                H2[i] = max(H2[i]-Q, 0);
                int result = dfs(H2, G, P, Q, true, depth+1, memo);
                memo[key] = result;
                return result;
            }
        }
        memo[key] = 0;
        return 0;
    }
}

int main() {
    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        int P, Q, N;
        cin >> P >> Q >> N;

        vector<int> H(N), G(N);
        for (int i = 0; i < N; i++) {
            cin >> H[i] >> G[i];
        }

        unordered_map<memo_key, int, function<decltype(key_hash)>> memo(100, key_hash);
        int result = dfs(H, G, P, Q, true, 0, memo);

        cout << "Case #" << T << ": ";
        cout << result;
        cout << endl;
    }
}
