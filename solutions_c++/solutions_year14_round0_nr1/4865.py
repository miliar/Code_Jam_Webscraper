#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <fstream>
using namespace std;
int cases, f[8][8], s[8][8];
int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &cases);
    for(int t = 1; t <= cases; t++)
    {
        int cnt = 0, num = 0, rf, rs;
        scanf("%d", &rf);
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &f[i][j]);
        scanf("%d", &rs);
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                scanf("%d", &s[i][j]);
        for(int i = 1; i <= 4; i++)
        for(int j = 1; j <= 4; j++)
            if(f[rf][i]==s[rs][j]) cnt++, num = f[rf][i];
        printf("Case #%d: ", t);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if (cnt>1) printf("Bad magician!\n");
        else printf("%d\n", num);
    }
    return 0;
}
