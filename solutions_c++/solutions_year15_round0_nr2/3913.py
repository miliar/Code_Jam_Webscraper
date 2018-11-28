#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <gmpxx.h>

using namespace std;

typedef mpz_class keyval;

map<keyval, int> mem;
int maxval;

int calc(const vector<int> &P) {
    if (P.size() == 0) return 0;
    keyval key = 0;
    keyval b = 1;
//    cout << "psize: " << P.size() << endl;
    for (int i = 0; i < P.size(); ++i) {
//        cout << P[i] << ' ';
        key += P[i] * b;
        b = b * maxval;
    }
//    cout << endl;
    if (mem.find(key) != mem.end()) return mem[key];

    int best = 100000;
    vector<int> newP;
    for (int i = 0; i < P.size(); ++i) {
        if (P[i] > 1) newP.push_back(P[i] - 1);
    }
    int val = calc(newP) + 1;
    if (val < best) best = val;
 
    for (int i = 0; i < P.size(); ++i) {
        if (i > 0 && P[i-1] == P[i]) continue;
        for (int j = 1; j <= P[i] / 2; ++j) {
            vector<int> newP = P;
            newP[i] -= j;
            newP.push_back(j);
            sort(newP.begin(), newP.end());
            int val = calc(newP) + 1;
            if (val < best) best = val;
        }
    }
    mem[key] = best;
    return best;
}

void doit() {
    int D;
    cin >> D;
    vector<int> P(D);
    maxval = 0;
    for (int i = 0; i < D; ++i) {
        cin >> P[i];
        maxval = max(maxval, P[i]);
    }

    sort(P.begin(), P.end());

    mem.clear();
    cout << calc(P) << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) { cout << "Case #" << i << ": "; doit(); }
    return 0;
}
