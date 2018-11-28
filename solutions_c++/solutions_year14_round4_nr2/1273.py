#define _CRT_SECURE_NO_WARNINGS
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
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

typedef unsigned int uint32;
typedef signed long long int64;
typedef unsigned long long uint64;

using namespace std;

#define ALL(a) a.begin(), a.end()
#define FOR(a) for (int i = 0; i < a; ++i)
#define D(a) #a << ": " << a << "\n"

int slow(vector<int> const& v)
{
    vector<int> perm = v;

    int qres = numeric_limits<int>::max();
    sort(ALL(perm));
    do 
    {
        bool ok = true;
        bool up = true;
        FOR(perm.size() - 1)
        {
            if (perm[i] < perm[i+1] && up)
                continue;

            if (perm[i] > perm[i+1])
            {
                up = false;
                continue;
            }

            ok = false;
            break;
        }

        if (ok)
        {
            int c = 0;
            vector<int> copy = perm;

            for (int i = 0; i < perm.size(); ++i)
            {
                int idx = i;

                while (copy[idx] != v[i])
                    ++idx;
                
                for (int a = idx; a > i; --a)
                    swap(copy[a-1], copy[a]), ++c;
            }

            qres = min(qres, c);
        }
    }
    while (next_permutation(ALL(perm)));

    return qres;
}

int main()
{
    srand(uint32(time(NULL)));
    cout << setprecision(15);
    int CASES = 100;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n = 1000;
        cin >> n;

        vector<int> v(n);
        FOR(n)
            scanf("%d", &v[i]);

        int qqqq = slow(v);
        printf("Case #%d: %d\n", CASE, qqqq);
    }

    return 0;
}
