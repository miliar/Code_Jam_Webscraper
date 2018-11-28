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

int solve(vector<int>& levels) {
    int ret = 0;
    int size = levels.size();
    int sum = levels[0];
    for (int i = 1; i < size; i++) {
        if (i > sum) {
            ret += i - sum;
            sum += i - sum;
        }
        sum += levels[i];
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
        int S; in >> S;
        string s; in >> s;
        vector<int> levels(S + 1);
        for (int i = 0; i <= S; i++) {
            levels[i] = s[i] - '0';
        }
        out << "Case #" << t + 1 << ": " << solve(levels) << endl;
    }
    return 0;
}
