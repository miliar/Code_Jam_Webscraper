#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

int a[4][4], b[4][4], cnt[17];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for (int q = 0; q < t; q++)
    {
        int n1, n2;
        for (int i = 0; i < 17; i++)
            cnt[i] = 0;
        scanf("%d", &n1);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &a[i][j]);
        scanf("%d", &n2);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d", &b[i][j]);
        for (int i = 0; i < 4; i++)
            cnt[a[n1 - 1][i]]++;
        int ans = 0, k = 0;
        for (int i = 0; i < 4; i++)
            if (cnt[b[n2 - 1][i]])
            {
                ans = b[n2 - 1][i];
                k++;
            }
        printf("Case #%d: ", q + 1);
        if (k == 1)
            cout << ans << "\n";
        else if (k == 0)
            cout << "Volunteer cheated!\n";
        else cout << "Bad magician!\n";
    }
    return 0;
}
