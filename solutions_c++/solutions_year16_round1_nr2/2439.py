#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        int n;
        scanf("%d", &n);
        vector<int> arr(2501, 0);
        for (int i = 0; i < 2 * n - 1; i++)
        {
            for (int j = 0; j < n; j++)
            {
                int t;
                scanf("%d", &t);
                arr[t]++;
            }
        }
        vector<int> res;
        for (int i = 0; i < 2501; i++)
        {
            if ((arr[i] & 1) == 1)
                res.push_back(i);
        }
        printf("Case #%d:", nc);
        for (int i = 0; i < res.size(); i++)
        {
            printf(" %d", res[i]);
        }
        printf("\n");
    }
}
