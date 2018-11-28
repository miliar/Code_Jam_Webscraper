#include <iostream>
#include <vector>
#include <utility>

using namespace std;
typedef vector<pair<int, int> > vp;

inline bool solved(vector<int> &p) {
    for (int i= 0; i< p.size();++i) {
        if (p[i] != 0) return false;
    }
    return true;
}
inline void apply(int i, int j, vector<int> &p) {
    if (i < p.size()) --p[i];
    if (j < p.size()) --p[j];
}
inline void revert(int i, int j, vector<int> &p) {
    if (i < p.size()) ++p[i];
    if (j < p.size()) ++p[j];
}
inline bool check(int i, int j, vector<int> &p) {

    bool revert = false;
    int sum = 0;
    for (int l = 0;!revert && l < p.size(); ++l) {
        if (p[l] < 0) {
            revert = true;
        }
        sum += p[l];
    }
    for (int l = 0; !revert && l < p.size(); ++l) {
        if (p[l]*2 >sum) {
            revert =true;
        }
    }

    return !revert;
}
bool solve(vp &res, vector<int> &p) {
    if (solved(p)) return true;
    for (int i = 0; i < p.size(); ++i) {
        for (int j=0; j <= p.size(); ++j) {
            apply(i, j, p);
            if (check(i, j, p)) {
                if (solve(res, p)) {
                    res.push_back(make_pair(i, j));
                    return true;
                } 
            }
            revert(i, j, p);
        }
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for (int t=0; t < T; ++t) {
        int N;
        cin >> N;
        vector<int> p(N, 0);
        for (int s= 0; s<N;++s) {
            cin >> p[s];
        }
        vp res;
        solve(res, p);

        cout << "Case #" << t+1 << ":";
        for (int i = res.size()-1; i >= 0; --i) {
            cout << " ";

            if (res[i].first < p.size()) cout.put('A' + res[i].first);
            if (res[i].second < p.size()) cout.put('A' + res[i].second);

        }
        cout << endl;
    }
    return 0;
}
