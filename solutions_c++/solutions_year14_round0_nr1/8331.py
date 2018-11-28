#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int T;

int a[5][5], b[5][5];

int main()
{
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        int r1, r2;
        scanf("%d", &r1);
        vi s1, s2;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
                scanf("%d", &a[i][j]);
        }
        scanf("%d", &r2);
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
                scanf("%d", &b[i][j]);
        }
        vi v(4);
        --r1; --r2;
        sort(a[r1], a[r1] + 4);
        sort(b[r2], b[r2] + 4);
        vi::iterator it = set_intersection(a[r1], a[r1]+4, b[r2], b[r2]+4, v.begin());
        v.resize(it - v.begin());
        if (v.size() == 1)
            printf("Case #%d: %d\n", t + 1, v[0]);
        else if (v.size() == 0)
           printf("Case #%d: Volunteer cheated!\n", t + 1 );
        else 
           printf("Case #%d: Bad magician!\n", t + 1 );
    }
    return 0;
}