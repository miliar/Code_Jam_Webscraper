/*************************************************************************
 * File Name:    C_large.cc
 * Author:       zero91
 * Mail:         jianzhang9102@gmail.com
 * Created Time: Sat 13 Apr 2013 07:12:51 PM CST
 * 
 * Description:  https://code.google.com/codejam/contest/2270488/dashboard#s=p2
 ************************************************************************/

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

#define MAXLEN 51

vector<string> palind, palind_square;

bool
lessab (const string &a, const string &b)
{
    if (a.size() != b.size()) return a.size() < b.size();
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) return a[i] < b[i];
    }
    return false;
}

bool largerab (const string &a, const string &b) { return lessab (b, a); }

bool
square_pal (const string &str, string &ret)
{
    size_t size = str.size() * 2 + 5;
    int res[size];
    size_t i, j;

    memset (res, 0, sizeof (res));
    for (i = 0; i < str.size(); ++i) {
        for (j = 0; j < str.size(); ++j) {
            res[i + j] += (str[i] - '0') * (str[j] - '0');
        }
    }
    for (i = 0; i < size - 1; ++i) {
        res[i + 1] += res[i] / 10;
        res[i] %= 10;
    }
    for (i = size - 1; i > 0; --i) {
        if (res[i] != 0) break;
    }
    for (j = 0; j < i - j; ++j) {
        if (res[j] != res[i - j]) return false;
    }
    ret = "";
    for (j = 0; j <= i; ++j) {
        ret = ret + char(res[j] + '0');
    }
    return true;
}

void
init_palind (int limit)
{
    palind.clear();

    palind.push_back("1");
    palind.push_back("2");
    palind.push_back("3");
    palind_square.push_back("1");
    palind_square.push_back("4");
    palind_square.push_back("9");

    size_t last = 0, len;
    string t, ret;
    while (1) {
        len = palind[last].size();
        if (len >= limit) break;

        for (int j = 0; j < 3; ++j) {
            if (len % 2 == 0) {
                t = palind[last].substr(0, len / 2) + char(j + '0') + palind[last].substr(len / 2);
            } else {
                t = palind[last].substr(0, len / 2) + palind[last][len / 2] + palind[last].substr(len / 2);
                j = 2;
            }
            if (square_pal(t, ret)) {
                palind.push_back(t);
                palind_square.push_back(ret);
            }
        }
        if (++last == palind.size()) break;
    }
    sort (palind_square.begin(), palind_square.end(), lessab);
}

int
main ()
{
    int T;
    long long ans;
    string a, b;
    vector<string>::iterator low, up;

    init_palind (MAXLEN);

    cin >> T;
    for (int k = 1; k <= T; ++k) {
        cin >> a >> b;

        low = lower_bound(palind_square.begin(), palind_square.end(), a, lessab);
        up = upper_bound(palind_square.begin(), palind_square.end(), b, lessab);

        ans = int(up - low);

        cout << "Case #" << k << ": " << ans << endl;
    }
    return 0;
}
