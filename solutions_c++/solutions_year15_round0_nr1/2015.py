#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

int main()
{
#ifdef DEBUGAGA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
#elif defined(CONTEST)
    freopen(CONTEST ".in", "r", stdin);
    freopen(CONTEST ".out", "w", stdout);
#endif

    int tests;
    cin >> tests;

    for (int tc = 0; tc < tests; ++tc)
    {
        int smax;
        cin >> smax;

        int stand = 0;
        int added = 0;
        for (int shy = 0; shy <= smax; ++shy)
        {
            if (stand < shy)
            {
                added += shy - stand;
                stand = shy;
            }

            char c;
            cin >> c;
            int cur = c - '0';
            stand += cur;
        }

        printf("Case #%d: %d\n", tc + 1, added);
    }

    return 0;
}