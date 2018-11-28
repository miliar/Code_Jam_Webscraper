#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <float.h>
#include <fstream>

using namespace std;

typedef long long ll;

int N;
int X;

int solve(vector<int> S) {
    int ret = 0;
    sort(S.rbegin(), S.rend());
    while (S.size() != 0) {
        ret++;
        int n = S[0];
        S.erase(S.begin());
        for (int i = 0; i < S.size(); i++) {
            if (S[i] <= X - n) {
                S.erase(S.begin() + i);
                break;
            }
        }
    }
    return ret;
}

#define LARGE

int main() {

#ifndef LARGE
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
#else
    ifstream in("A-large.in");
    ofstream out("A-large.out");
#endif

    int T; in >> T;
    for (int t = 0; t < T; t++) {
        in >> N >> X;
        vector<int> S(N);
        for (int n = 0; n < N; n++) {
            in >> S[n];
        }
        out << "Case #" << t + 1 << ": " << solve(S) << endl;
    }
    return 0;
}
