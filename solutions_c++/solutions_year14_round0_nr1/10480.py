#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string.h>
#include <vector>
#include <ctime>
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define sqr(x) (x) * (x)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;
 
int T;
int a[4][4];

int main()
{
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        int u, v;
        cin >> u;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> a[j][k];
        cin >> v;
        vector<int> g (16, 0);
        for (int j = 0; j < 4; j++)
            g[a[u - 1][j] - 1]++;
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 4; k++)
                cin >> a[j][k];
        for (int j = 0; j < 4; j++)
            g[a[v - 1][j] - 1]++;
        int ans = -1;
        for (int j = 0; j < 16; j++)
            if (g[j] == 2)
            {
                if (ans == -1 && ans != -2)
                    ans = j + 1;
                else
                    ans = -2;
            }
        if (ans == -2)
            printf("Bad magician!\n");
        else if (ans == -1)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}