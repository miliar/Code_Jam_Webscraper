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

int solve(ll N) {
    set<int> s;
    for (int i = 1; ; ++i) {
        ll n = N * i;
        while (n) {
            s.insert(n % 10);
            n /= 10;
        }
        if (s.size() == 10) {
            return N * i;
        }
    }
    return 0;
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
        int N; in >> N;
        if (N == 0) {
            out << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
        } else {
            out << "Case #" << t + 1 << ": " << solve(N) << endl;
        }
    }
    return 0;
}
