#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>

using namespace std;

typedef long long u64;

int bysize[4];

void preprocess() {
    bysize[0] = 1;
    bysize[1] = 10;
    bysize[2] = 100;
    bysize[3] = 1000;
}

bool matches(int num, string const &str) {
    //cerr << " matching " << num << " to " << str << endl;
    int ssz = str.size();
    int ss;
    for (ss=0; ss<ssz; ++ss) {
        if (str[ss] == '?') {
            //cerr << "  matching with ?" << endl;
            continue;
        }
        //cerr << "  (num/bysize[ssz-ss-1])%10)) = " << ((num/bysize[ssz-ss-1])%10) << endl;
        //cerr << "  str[ss] = " << str[ss] << endl;
        if ((str[ss]-'0') == ((num/bysize[ssz-ss-1])%10)) {
            continue;
        }
        //cerr << "    false..." << endl;
        return false;
    }
    //cerr << "    true..." << endl;
    return true;
}

void solve() {
    string C, J;
    cin >> C >> J;
    int csz = C.size();
    int cc, jj;
    int maxnum = bysize[csz];
    int bestdiff = maxnum+1;
    int bestcc = -1, bestjj = -1;
    for (cc=0; cc<maxnum; ++cc) {
        if (not matches(cc, C)) continue;
        for (jj=0; jj<maxnum; ++jj) {
            if (not matches(jj, J)) continue;
            if (abs(cc-jj) < bestdiff) {
                bestdiff = abs(cc-jj);
                bestcc = cc;
                bestjj = jj;
            } else if (abs(cc-jj) == bestdiff) {
                if (cc < bestcc) {
                    bestcc = cc;
                    bestjj = jj;
                } else if (cc == bestcc) {
                    if (jj < bestjj) {
                        bestjj = jj;
                    }
                }
            }
        }
    }
    if (csz == 1) {
        printf("%01d %01d", bestcc, bestjj);
    } else if (csz == 2) {
        printf("%02d %02d", bestcc, bestjj);
    } else if (csz == 3) {
        printf("%03d %03d", bestcc, bestjj);
    }
}

int main() {
    preprocess();
    int T;
    cin >> T;
    int tt;
    for (tt=1; tt<=T; ++tt) {
        cout << "Case #" << tt << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

