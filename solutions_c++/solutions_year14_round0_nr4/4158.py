#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

#define SIZELIMIT 51

using namespace std;


int main()
{
    int t, n;
    int y, z;
    double tmp;
    vector<double> naomi, ken;

    scanf("%d", &t);
    for(int k = 1; k <= t; ++k)
    {
        scanf("%d", &n);

        for(int i = 0; i < n; ++i)
        {
            scanf("%lf", &tmp);
            naomi.push_back(tmp);
        }

        for(int i = 0; i < n; ++i)
        {
            scanf("%lf", &tmp);
            ken.push_back(tmp);
        }

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        // play war
        z = 0;
        int p = 0, q = n-1;
        for(int i = n - 1; i >= 0; --i)
        {
            if(ken[q] < naomi[i])
            {
                ++p;
                ++z;
            }
            else
            {
                --q;
            }
        }

        // play deceitful war
        y = 0;
        p = 0;
        q = n-1;
        for(int i = n - 1; i >= 0; --i)
        {
            if(naomi[q] < ken[i])
            {
                ++p;
            }
            else
            {
                ++y;
                --q;
            }
        }

        printf("Case #%d: %d %d\n", k, y, z);
        ken.clear();
        naomi.clear();
    }

    return 0;
}
