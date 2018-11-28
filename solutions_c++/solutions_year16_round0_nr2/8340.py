#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstring>
#include <cmath>
#include <climits>
#include <ctime>
#include <cctype>
#include <fstream>

using namespace std;

typedef long long ll;

int solve(string& S) {
    string s;
    s += S[0];
    for (int i = 1; i < S.length(); ++i) {
        if (S[i] != S[i - 1]) {
            s += S[i];
        }
    }
    if (s[s.length() - 1] == '+') {
        return s.length() - 1;
    }
    return s.length();
}

//#define SAMPLE
#define LARGE

int main() {

#ifdef SAMPLE
    ifstream in("B-samle.in");
    ofstream out("B-sample.out");
#else
#ifndef LARGE
    ifstream in("B-small-attempt0.in");
    ofstream out("B-small-attempt0.out");
#else
    ifstream in("B-large.in");
    ofstream out("B-large.out");
#endif
#endif

    int T; in >> T;
    for (int t = 0; t < T; t++) {
        string S; in >> S;
        out << "Case #" << t + 1 << ": " << solve(S) << endl;
    }
    return 0;
}
