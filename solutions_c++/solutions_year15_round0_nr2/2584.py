// ================================================================================================
//  B - Infinite House of Pancakes.cpp
//  Written by Luis Garcia, 2015
// ================================================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ15_01B, "GCJ15 01B")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)


int f(vector<int> & t, map<vector<int>, int> & found) {
    auto c = found.find(t);
    if (c != found.end()) return c->second;

    int ans = 0x7fffffff;

    if (t.empty())
        ans = 0;
    else {
        {
            vector<int> newSet;
            for (auto x : t) if (x > 1) newSet.push_back(x - 1);
            ans = min(ans, f(newSet, found) + 1);
        }

        for (auto it = t.begin(); it != t.end(); ++it) {
            vector<int> newSet;
            newSet.insert(newSet.end(), t.begin(), it);
            newSet.insert(newSet.end(), it + 1, t.end());
            for (int y = 1; y < * it; ++y) {
                auto newSetCopy = newSet;
                newSetCopy.push_back(y);
                newSetCopy.push_back(* it - y);
                sort(newSetCopy.begin(), newSetCopy.end());
                ans = min(ans, f(newSetCopy, found) + 1);
            }
        }
    }

    found[t] = ans;
    return ans;
}

int main() {
    map<vector<int>, int> found;

    {
        vector<int> temp = {9, 9, 9, 9, 9, 9};
        f(temp, found);
    }

    int T, D;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%d", &D);

        vector<int> items;
        for (int i = 0, t; i < D; ++i) {
            scanf("%d", &t);
            items.push_back(t);
        }
        sort(items.begin(), items.end());

        printf("Case #%d: %d\n", _T, f(items, found));
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
