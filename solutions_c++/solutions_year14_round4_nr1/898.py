#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define all(o) (o).begin(), (o).end()
#define allr(o) (o).rbegin(), (o).rend()
const int INF = 2147483647;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> int size(T &x) { return x.size(); }

// assert or gtfo

int main()
{
    int ts;
    scanf("%d\n", &ts);

    for (int t = 0; t < ts; t++)
    {
        printf("Case #%d: ", t+1);

        int n, m;
        scanf("%d %d\n", &n, &m);

        vi sz(n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &sz[i]);
        }

        sort(all(sz));

        int cnt = 0;
        vector<bool> used(n, false);
        for (int i = n - 1; i >= 0; i--)
        {
            if (used[i]) continue;

            bool found = false;
            for (int j = i - 1; j >= 0; j--)
            {
                if (sz[i] + sz[j] <= m && !used[j])
                {
                    found = true;
                    used[i] = true;
                    used[j] = true;
                    cnt++;
                    break;
                }
            }

            if (!found)
            {
                cnt++;
                used[i] = true;
            }
        }

        printf("%d\n", cnt);

// 
//         int lo = 0,
//             hi = n / 2;
// 
//         do
//         {
//             int mid = hi - (hi - lo) / 2;
// 
//             printf("%d\n", mid);
// 
//             bool ok = true;
//             vector<bool> used(n);
//             for (int i = 0; i < mid * 2; i++)
//             {
//                 if (used[i]) continue;
// 
//                 printf("looking for %d(%d)\n", i, sz[i]);
// 
//                 bool found = false;
//                 for (int j = mid * 2 - 1; j > i; j--)
//                 {
//                     if (sz[i] + sz[j] <= m && !used[j])
//                     {
//                         printf("found %d(%d)\n", j, sz[j]);
//                         used[i] = true;
//                         used[j] = true;
//                         found = true;
//                         break;
//                     }
//                 }
// 
//                 if (!found)
//                 {
//                     ok = false;
//                     break;
//                 }
//             }
// 
//             if (ok) lo = mid;
//             else hi = mid - 1;
// 
//         } while (lo < hi);

        // printf("%d\n", hi * 2 + (n - hi * 2));
        // printf("%d\n", hi * 2);
        // printf("%d\n", n - 4 * hi + 2 * hi);
    }

    return 0;
}

