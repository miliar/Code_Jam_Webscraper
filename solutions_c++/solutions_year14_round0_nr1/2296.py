#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <list>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    int r1, r2, ans=-1, cnt = 0, a[10][10], t1[10], t2[10];
    for (int tot = 1; tot <= T; tot++) {
        scanf("%d", &r1);
        for (int i = 1; i <= 4; i++) {
            for (int j = 0; j < 4; j++)
                scanf("%d", &a[i][j]);
        }
        for (int i = 0; i < 4; i++) 
            t1[i] = a[r1][i];
        
        scanf("%d", &r2);
        for (int i = 1; i <= 4; i++) {
            for (int j = 0; j < 4; j++)
                scanf("%d", &a[i][j]);
        }
        for (int i = 0; i < 4; i++) 
            t2[i] = a[r2][i];

        cnt = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (t1[i] == t2[j]) {
                    cnt++;
                    ans = t1[i];
                }
            }
        }
        
        printf("Case #%d: ", tot);\
        if (cnt == 0) {
            printf("Volunteer cheated!\n");
        }
        else if (cnt == 1)
            printf("%d\n", ans);
        else
            printf("Bad magician!\n");

    }
    return 0;
}
