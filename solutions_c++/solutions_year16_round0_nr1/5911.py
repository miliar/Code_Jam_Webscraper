#include <iostream>
#include <vector>
#include <set>

using namespace std;

int add_new(int n, vector<int>& used) {
    int num = n;
    int c = 0;
    int d;
    do {
        d = num % 10;
        num /= 10;
        if (used[d] == 0) {
            used[d] = 1;
            ++c;
        }
    } while (num > 0);
    return c;
}

int main() {
    int t, n;
    cin >> t;
    for (int test_ind = 0; test_ind < t; ++test_ind) {
        cin >> n;
        vector<int> used(10, 0);
        int count_used = 0;
        int last_step = 0;
        if (n == 0) {
            cout << "Case #" << test_ind + 1 << ": INSOMNIA" << endl;
            continue;
        }
        for (int j = 1; count_used < 10; ++j) {
            int cur = n * j;
            count_used += add_new(cur, used);
            last_step = cur;
        }
        cout << "Case #" << test_ind + 1 << ": " << last_step << endl;
    }
}

