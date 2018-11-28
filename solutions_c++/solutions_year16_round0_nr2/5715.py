#include <iostream>
#include <map>
#include <stdio.h>
#include <cstddef>
#include <sstream>
#include <vector>
#include <stdexcept>
#include <fstream>
#include <queue>

using namespace std;

vector < vector <int> > ans;

int solve(int n, int sz)
{
    return ans[sz][n];
}

void set_bit(int &n, int pos, int val)
{
    if (val) {
        n |= 1 << pos;
    } else {
        n &= ~(1 << pos);
    }
}

vector <int> swaps(int n, int len)
{
    vector <int> swp;
    for (int i = 0; i < len; i++) {
        int tmp = n;
        for (int j = 0; j < (i + 1) / 2; j++) {
            int b1 = (n & (1 << j));
            int b2 = (n & (1 << (i - j)));
            set_bit(tmp, j, !b2);
            set_bit(tmp, i - j, !b1);
        }
        if (i % 2 == 0) {
            tmp ^= (1 << (i / 2));
        }
        swp.push_back(tmp);
    }
    return swp;
}

void precalc()
{
    ans.resize(11, vector <int> (10000, 1000 * 1000 * 1000));
    for (int len = 1; len <= 10; len++) {
        ans[len][0] = 0;
        queue <int> q;
        q.push(0);
        while (!q.empty()) {
            int n = q.front();
            q.pop();
            vector <int> swp = swaps(n, len);
            for (auto &el : swp) {
                if (ans[len][el] > ans[len][n] + 1) {
                    ans[len][el] = ans[len][n] + 1;
                    q.push(el);
                }
            }
        }
    }
}

int main()
{
    precalc();

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        string s;
        cin >> s;
        int n = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            set_bit(n, i, s[i] == '-');
        }
        cout << "Case #" << i + 1 << ": " << solve(n, (int)s.size()) << endl;
    }
    return 0;
}
