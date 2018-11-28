#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int a[4][4][4]={{{1,1,1,1}, {1,1,1,1}, {1,1,1,1}, {1,1,1,1}},
                {{0,1,0,1}, {1,1,1,1}, {0,1,0,1}, {1,1,1,1}},
                {{0,0,0,0}, {0,0,1,0}, {0,1,1,1}, {0,0,1,0}},
                {{0,0,0,0}, {0,0,0,0}, {0,0,0,1}, {0,0,1,1}}};
int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int x, y, z;
        scanf("%d%d%d", &x, &y, &z);
        x--, y--, z--;
        printf("Case #%d: ", ca++);
        if(a[x][y][z])
            puts("GABRIEL");
        else
            puts("RICHARD");
    }
    return 0;
}
