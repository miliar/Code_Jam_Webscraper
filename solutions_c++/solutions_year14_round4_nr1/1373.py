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

int main()
{
    srand(uint32(time(NULL)));
    cout << setprecision(15);
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n, x;
        cin >> n >> x;

        multiset<int, greater<int> > ms;
        FOR(n)
        {
            int tmp;
            scanf("%d", &tmp);
            ms.insert(tmp);
        }
        int res = 0;
        while (!ms.empty())
        {
            int one = *ms.begin();
            ms.erase(ms.begin());

            auto itr = ms.lower_bound(x - one);

            if (itr != ms.end())
                ms.erase(itr);

            ++res;
        }

        printf("Case #%d: %d\n", CASE, res);
    }

    return 0;
}
