#include <string>
#include <queue>
#include <stack>
#include <vector>
#include <sstream>
#include <algorithm>
#include <deque>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <list>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <climits>
#include <bitset>
#include <functional>
#include <numeric>

using namespace std;

int main()
{
    int t;
    cin >> t;
    getchar();
    for (int i = 0; i < t; i++)
    {
        string s;
        getline(cin, s);
        int cnt = 0;
        for (int i = s.size() - 1; i >= 0; i--)
        {
            char &c = s[i];
            bool flip = (c == '-');
            if (cnt % 2 == 1)
                flip = !flip;
            if (flip)
                cnt++;
        }
        printf("Case #%d: %d\n", i + 1, cnt);
    }
    return 0;
}