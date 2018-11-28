#include <iostream>
#include <queue>
#include <vector>
#include <functional>
#include <set>
#include <cmath>

using namespace std;

int GetMinMinutes() {
    int D;
    cin >> D;
    
    priority_queue<int, vector<int>, less<int> > s;
    for (int i = 0; i < D; ++i) {
        int p;
        cin >> p;
        s.push(p);
    }
    
    int minMinutes = s.top();
    for (int i = 0; i < 10000; ++i) {
        int maxPancakes = s.top();
        minMinutes = min(minMinutes, maxPancakes + i);
        s.pop();
        s.push(maxPancakes / 2);
        s.push(maxPancakes - maxPancakes / 2);
    }
    
    return minMinutes;
}

int ans;

int GetMaxVal(const vector<int>& s) {
    int ma = -1;
    for (int i = 0; i < s.size(); ++i) {
        ma = max(ma, s[i]);
    }
    
    return ma;
}

set< vector<int> > used;

void dfs(vector<int>& s, int moves) {
    
    if (moves >= ans) {
        return;
    }
    
    int maxVal = GetMaxVal(s);
    if (maxVal <= 1) {
        return;
    }
    
    ans = min(ans, maxVal + moves);
    
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] <= 3) {
            continue;
        }
        int val = s[i];
        s[i] = 0;
        for (int j = 1; j <= val / 2; ++j) {
            s.push_back(j);
            s.push_back(val - j);
            dfs(s, moves + 1);
            s.pop_back();
            s.pop_back();
        }
        s[i] = val;
    }
}

long long Clever() {
    int D;
    cin >> D;
    
    vector<int> s;
    for (int i = 0; i < D; ++i) {
        int p;
        cin >> p;
        s.push_back(p);
    }
    
    int maxVal = GetMaxVal(s);
    long long ans = maxVal;
    
    for (int k = 2; k <= maxVal; ++k) {
        long long moves = 0;
        for (int i = 0; i < s.size(); ++i) {
            moves += max(ceil((double)s[i] / k) - 1, 0.0);
        }
        ans = min(ans, moves + k);
    }
    
    return ans;
}

void Solve() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": " << Clever() << endl;
    }
}

int main(int argc, const char * argv[]) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    Solve();
    return 0;
}
