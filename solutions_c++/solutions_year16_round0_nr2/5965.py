#include <iostream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
using namespace std;

inline bool all(vector<bool> &v) {
    for (vector<bool>::const_iterator i = v.begin(); i != v.end(); ++i) {
        if (!(*i)) return false;
    }
    return true;
}

template <class K, class V>
inline bool contains(K &e, map<K, V> m) {
    return m.find(e) != m.end();
}

inline vector<bool> flip(vector<bool> res, int f) {
    for (int i = 0; (i<<1) <= f; ++i) {
        // negate and swap
        bool t = !res[i];
        res[i] = !res[f-i];
        res[f-i] = t;
    }
    return res;
}

int main() {
    int T;
    cin >> T; 
    for (int t = 0; t < T; ++t) {
        map<vector<bool>, int> distance;
        queue<vector<bool> > q;
        {
            string s;
            cin >> s;
            vector<bool> initial;
            for (int i = 0; i < s.size(); ++i) {
                initial.push_back(s[i] == '+');
            } 
            q.push(initial);
            distance[initial] = 0;
        }
        int d = 0;
        while (!q.empty()) {
            vector<bool> & current = q.front();
            d = distance[current];
            if (all(current)) break;
            int n = current.size()-1;
            while (current[n]) --n;
            for (int i = 0; i <= n; ++i) {
                vector<bool> v = flip(current, i);
                if (contains(v, distance)) continue;
                distance[v] = d + 1;
                q.push(v);
            }
            q.pop();
        }
        cout << "Case #" << t+1 << ": " << d << endl;
    }
    return 0;
}
