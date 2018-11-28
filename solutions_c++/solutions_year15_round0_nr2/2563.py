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

int solve(int cnt, priority_queue<int> q) {
    int ret = 1000;
    int hi = q.top();
    q.pop();
    ret = min(ret, cnt + hi);
    if (hi > 3) {
        {
            priority_queue<int> qq = q;
            qq.push(hi / 2);
            qq.push(hi - hi / 2);
            ret = min(ret, solve(cnt + 1, qq));
        }
        {
            priority_queue<int> qq = q;
            qq.push(hi / 2 - 1);
            qq.push(hi - (hi / 2 - 1));
            ret = min(ret, solve(cnt + 1, qq));
        }
    }
    return ret;
}

int main() {

#ifndef LARGE
    ifstream in("B-small-attempt2.in");
    ofstream out("B-small-attempt2.out");
#else
    ifstream in("B-large.in");
    ofstream out("B-large.out");
#endif

    int T; in >> T;
    for (int t = 0; t < T; t++) {
        int D; in >> D;
        priority_queue<int> q;
        for (int d = 0; d < D; d++) {
            int diner; in >> diner;
            q.push(diner);
        }
        out << "Case #" << t + 1 << ": " << solve(0, q) << endl;
    }
    return 0;
}
