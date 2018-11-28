#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

string bf(string s)
{
    set<string> res, res2;
    string q; q += s[0];
    res.insert(q);

    for (int i = 1; i < s.size(); ++i)
    {
        for (string b : res)
        {
            res2.insert(b + s[i]);
            res2.insert(s[i] + b);
        }

        swap(res, res2);
        res2.clear();
    }

    return *res.rbegin();
}

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        string s, r;
        cin >> s;
        //for (int i = 0; i < 15; ++i)
            //s += rand() % + ('Z' - 'A') + 'A';

        r += s[0];

        for (int i = 1; i < s.size(); ++i)
        {
            if (r[0] <= s[i])
                r = s[i] + r;
            else
                r += s[i];
        }

        //string r2 = bf(s);
        //assert(r == r2);

        printf("Case #%d: ", CASE);
        cout << r << endl;
    }


    return 0;
}
