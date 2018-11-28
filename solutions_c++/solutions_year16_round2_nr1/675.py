/* Task solution for GCJ 2015
 * Tested with GCC
 * Build command line:
 *  g++ -std=gnu++11 -O2 -o <executable> <source.cpp>
 */

#include <cstdio>
#include <iostream>

using namespace std;

const struct {
    int i;
    char c;
    const char s[10];
} d[] = {
    {0, 'Z', "ZERO"},
    {2, 'W', "TWO"},
    {4, 'U', "FOUR"},
    {1, 'O', "ONE"},
    {3, 'R', "THREE"},
    {5, 'F', "FIVE"},
    {6, 'X', "SIX"},
    {7, 'S', "SEVEN"},
    {8, 'G', "EIGHT"},
    {9, 'I', "NINE"}
};

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TN;
    cin >> TN;
    for (int T = 1; T <= TN; T++) {
        string s;
        cin >> s;
        int a['Z' - 'A' + 1] = {0};
        for (auto c : s) {
            ++a[c - 'A'];
        }

        int k[10];
        for (auto v : d) {
            k[v.i] = a[v.c - 'A'];
            for (auto t : v.s) {
                a[t - 'A'] -= k[v.i];
            }
        }

        cout << "Case #" << T << ": ";
        for (int i = 0; i <= 9; ++i) {
            for (int j = 0; j < k[i]; ++j) {
                cout << i;
            }
        }
        cout << endl;
    }
    return 0;
}
