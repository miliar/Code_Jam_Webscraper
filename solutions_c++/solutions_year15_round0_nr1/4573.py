#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define BARSUK_ALEXEY_PSKOV

int tests;

int main()
{
#ifdef BARSUK_ALEXEY_PSKOV
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    scanf("%d", &tests);
    for (int t = 1; t <= tests; t++) {
        int Smax;
        scanf("%d", &Smax);
        int audience[Smax + 1];
        memset(audience, 0, sizeof(audience));
        int people_cnt = 0;
        for (int i = 0; i <= Smax; i++) {
            scanf("%1d", audience + i);
            people_cnt += audience[i];
        }
        int people_standing = 0;
        for (int i = 0; i <= Smax; i++) {
            if (people_standing < i && audience[i] != 0) {
                people_standing += (i - people_standing);
            }
            people_standing += audience[i];
        }
        cout << "Case #" << t << ": " << (people_standing - people_cnt) << endl;
    }

    return 0;
}

