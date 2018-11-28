#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void print_answer(int id, bool can) {
    cout << "Case #" << id << ": " << (can ? "GABRIEL" : "RICHARD") << endl;
}

bool test_xomino(int x, int r, int c) {
    int smin = min(r, c);
    int smax = max(r, c);
    int sq = smin * smax;
    if (x == 1)
        return true;
    if (sq % x != 0)
        return false;
    if (x > smax)
        return false;
    if (x == 2 && sq >= 2)
        return true;
    if (x == 3 && smax >= 3 && smin >= 2)
        return true;
    if ((x + 1) / 2 > smin)
        return false;
    if (x >= 7)
        return false;
    if (smin == 2 && x >= 5)
        return false;
    if (x > 2 && (3 * x > sq))
        return false;
    return true;
}

void process_test(int id) {
    int x, r, c;
    cin >> x >> r >> c;
    bool result = test_xomino(x, r, c);
    cerr << id << " -> " << x << " " << r << " " << c << ": " << result << endl;
    print_answer(id, result);

}

int main() {
    int test_count;
    cin >> test_count;
    for (int i = 0; i < test_count; ++i) {
        process_test(i + 1);
    }
    return 0;
}