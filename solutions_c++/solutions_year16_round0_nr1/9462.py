#include <iostream>
#include <unordered_set>
using namespace std;

void solver(int n) {
    unordered_set<int> myset;
    myset.clear();
    if (n == 0) {
        cout << "INSOMNIA" << endl;
    } else {
        int i = 1;
        while (myset.size() < 10) {
            int curr_n = (i++) * n;
            while ( curr_n > 0) {
                myset.insert( curr_n % 10);
                curr_n = curr_n / 10;
            }
        }
        cout << (i-1) * n << endl;
    }
}

int main() {
    int t, n;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        cout << "Case #" << i << ": ";
        solver(n);
    }
}
