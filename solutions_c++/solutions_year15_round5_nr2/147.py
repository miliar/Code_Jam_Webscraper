#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define all(a) (begin(a)), (end(a))

int solve_case();

int main() {
    ios::sync_with_stdio(false);
    int num_case;
    cin >> num_case;
    for (int i=1; i<=num_case; i++) {
        auto ans = solve_case();
        cout << "Case #" << i << ": " << ans << '\n';
    }
    return 0;
}

int solve_case() {
    int n, k;
    cin >> n >> k;
    // sums[x] = val[x] + .. + val[x+k-1]
    // -10000 ... 10000
    vector<int> sums(n-k+1);
    for (int &x: sums)
        cin >> x;
    // diffs[x] = val[x+k] - val[x]
    // -20000 ... 20000
    vector<int> diffs(n-k);
    for (int i=0; i<n-k; i++)
        diffs[i] = sums[i+1] - sums[i];

    // 0 ... 20,000,000
    vector<int> max_up(k, 0);
    vector<int> max_down(k, 0);
    for (int i=0; i<k; i++) {
        int curr_sum = 0;
        for (int j=i; j<n-k; j+=k) {
            curr_sum += diffs[j];
            max_up[i] = max(max_up[i], curr_sum);
            max_down[i] = max(max_down[i], -curr_sum);
        }
    }

    int offset_sum = (sums[0] % k + k) % k;
    for (int i=0; i<k; i++)
        offset_sum = (offset_sum - (max_down[i] % k) + k) % k;

    vector<int> ranges(k);
    for (int i=0; i<k; i++)
        ranges[i] = max_up[i] + max_down[i];
    sort(all(ranges));
    int max_range = ranges.back();

    /*
    cout << "ranges:";
    for (int x: ranges)
        cout << ' ' << x;
    cout << '\n';
    cout << "offset_sum: " << offset_sum << '\n';
    */

    int remain = offset_sum;
    for (int x: ranges) {
        remain -= max_range - x;
        if (remain <= 0)
            return max_range;
    }
    return max_range + 1;
}
