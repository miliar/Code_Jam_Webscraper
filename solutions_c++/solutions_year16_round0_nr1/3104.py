#include <iostream>
#include <set>
using namespace std;

set<long long> breakdown(long long tar) {
    set<long long> ret;
    do {
        ret.insert(tar % 10);
        tar /= 10;
    } while(tar > 0);
    return ret;
} 

int solve(int n) {
    bool run = true;
    long long cur = 0;
    set<long long> all_set;
    int round = 0;

    if (n == 0)
        return 0;

    while(true) {
        round++;
        cur += n;
        set<long long> new_set = breakdown(cur);
        all_set.insert(new_set.begin(), new_set.end());
        if (all_set.size() == 10)
            return cur;
    }
    return 0;
}

int main() {
    int t;
    cin >> t;
    for (int round = 1; round <= t; ++round) {
        int n;
        cin >> n;
        int ret = solve(n);
        if (ret > 0) {
            cout << "Case #" << round << ": " << ret << endl;
        } else {
            cout << "Case #" << round << ": " << "INSOMNIA" << endl;
        }
    
    }
    return 0;
}
