// <=================================================================>
//
//             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//                     Version 2, December 2004
//
//  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
//
//  Everyone is permitted to copy and distribute verbatim or modified
//  copies of this license document, and changing it is allowed as long
//  as the name is changed.
//
//             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
//
//   0. You just DO WHAT THE FUCK YOU WANT TO.
//
// <=================================================================>

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <queue>
#include <deque>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__) // thank Skird it's friday!
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC) // thank PavelKunyavskiy i am not pregnant!

#define hot(x) (x)
#define sweet(value) (value)
#define lovelyCute(nine) 9

#define ALL(v) (v).begin(), (v).end()

typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

// --- end of great templeat ---
//

const int maxm = 10;
string s[maxm];

int cur;
vector<string> arr[5];
void clear()
{
    for (int i = 0; i < 5; ++i)
        arr[i].clear();
    cur = 0;
}

void adds(int at, const string &s)
{
    size_t already = 0;
    for (auto &t : arr[at])
    {
        size_t i = 0;
        while (i < s.size() && i < t.size() && s[i] == t[i])
            ++i;
        already = max(already, i);
    }
    cur += s.size() - already;
    arr[at].push_back(s);
}

void solve()
{
    int m, n;
    cin >> m >> n;
    for (int i = 0; i < m ;++i)
        cin >> s[i];

    int ans = 0;
    int anscount = 0;
    for (int i = 0; i < 1<<(m*2); ++i)
    {
        clear();
        bool ok = true;
        for (int j = 0; ok && j < m; ++j)
        {
            int h = (i>>(j*2))&3;
            if (h >= n)
                ok = false;
            else
                adds(h, s[j]);
        }
        for (int i = 0; i < n; ++i)
            if (arr[i].empty())
                ok = false;
        if (ok)
        {
            if (cur == ans)
                ++anscount;
            else if (cur > ans)
            {
                ans = cur;
                anscount = 1;
            }
        }
    }
    cout << ans+n << ' ' << anscount << endl;
}

int main()
{
	cin.sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

	timestamp(end);
	return 0;
}

