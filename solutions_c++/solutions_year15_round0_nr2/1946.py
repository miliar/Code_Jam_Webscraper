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

const int MAX_S = 1005;
const int MAX_D = 1005;

int p[MAX_D];

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
        int d;
        cin >> d;
        for (int i = 0; i < d; ++i)
        {
            cin >> p[i];
        }

        int best = INT_MAX;
        for (int s = 0; s < MAX_S; ++s)
        {
            priority_queue<iii> q;
            for (int i = 0; i < d; ++i)
            {
                q.push(mt(p[i], 1, p[i]));
            }

            for (int i = 0; i < s; ++i)
            {
                iii m = q.top();
                q.pop();
                int dto = m.second.first + 1;
                int v = (m.second.second + dto - 1) / dto;
                q.push(mt(v, dto, m.second.second));
            }
            int loc_best = s + q.top().first;
            best = min(best, loc_best);
        }

        printf("Case #%d: %d\n", tc + 1, best);
    }

    return 0;
}