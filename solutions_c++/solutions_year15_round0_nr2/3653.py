#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int solve_thres(const int thres, const vector<int> &numbers) {
    int ans = thres;
    for (int num : numbers) {
        while (num > thres) {
            ++ans;
            num -= thres;
        }
    }
    return ans;
}

void solve() {
    int N;
    cin >> N;
    vector<int> numbers;
    int highest = 0;
    for (int i = 0; i < N; ++i) {
        int cur;
        cin >> cur;
        highest = max(cur, highest); 
        numbers.push_back(cur);
    }
    int ans = 1<<30;
    for (int i = 1; i <= highest; ++i) {
        const int result = solve_thres(i, numbers);
        ans = min(result, ans);
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }   
}
