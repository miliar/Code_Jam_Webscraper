#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long long   li;
typedef long double ld;

const int N = 1000000000;
const int INF = 1000000000;
const ld EPS = 1E-10;

using namespace std;

bool solve(li b, int n, vector<li> sums, li value, ld& result)
{
    li sum = 0;    
    vector<li> bed(37);
    int minCount = 0;

    forn(i, 37)
    {
        if (sums[i] < value)
        {
            sum += value - sums[i];
            bed[i] = value - sums[i];
        }
        if (sums[i] <= value)
            minCount++;
    }

    if (sum > b)
        return false;

    result = -1E20;

    vector<li> bb;
    forn(i, 37)
        if (sums[i] <= value)
            bb.push_back(bed[i]);
    sort(bb.begin(), bb.end());

    forn(e, bb.size())
        if (sum + e <= b)
        {
            ld cad = - sum - e;
            for (int i = e; i < int(bb.size()); i++)
                cad += ld(1.0) * bb[i] * 36.0 / ld(bb.size() - e);
            if (cad > result)
            {
                // cout << "ee " << e << " " << cad << endl;
                result = cad;
            }
        }

    return true;
}

int main(int argc, char* argv[])
{
    // freopen("input.txt", "rt", stdin);

    int testCases;
    cin >> testCases;

    forn(testCase, testCases)
    {
        li b;
        int n;
        cin >> b >> n;
        
        vector<li> sums(37);
        forn(i, n)
            cin >> sums[i];

        ld result = -1E100;

        forn(i, 37)
        {
            ld cad;
            if (solve(b, n, sums, sums[i], cad))
                result = max(result, cad);
        }

        li l = 0;
        li r = 1E14;

        while (r - l > 1)
        {
            li mid = (l + r) / 2;

            ld cad;
            if (solve(b, n, sums, mid, cad))
                l = mid;
            else
                r = mid;
        }

        for (li i = max(l - 100000, 0LL); i <= r + 5LL; i++)
        {
            ld cad;
            if (solve(b, n, sums, i, cad))
                result = max(result, cad);
        }

        for (li i = 0; i <= 100000; i++)
        {
            ld cad;
            if (solve(b, n, sums, i, cad))
                result = max(result, cad);
        }

        cout << "Case #" << testCase + 1 << ": ";
        printf("%.10lf\n", double(result));
    }

    return 0;
}
