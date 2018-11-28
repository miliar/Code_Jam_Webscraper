/*
 * @author: zhenpeng.fang
 * @nickname: dumpling
 */
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <time.h>
#include <stdlib.h>
#include <stack>
#include <queue>
using namespace std;

#define mp make_pair

//%llu
typedef unsigned long long uint64;
typedef long long int64;
typedef pair<int, int> pair2;

const double eps = 1e-8;

int card[5][5];
bool frt[17], snd[17];

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T, row;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        memset(card, 0, sizeof (card));
        memset(frt, 0, sizeof (frt));
        memset(snd, 0, sizeof (snd));
        scanf("%d", &row);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &card[i][j]);
        for (int i = 1; i <= 4; ++i)
            frt[card[row][i]] = true;
        
        scanf("%d", &row);
        for (int i = 1; i <= 4; ++i)
            for (int j = 1; j <= 4; ++j)
                scanf("%d", &card[i][j]);
        for (int i = 1; i <= 4; ++i)
            snd[card[row][i]] = true;
        
        int cnt = 0, ans = 0;
        for (int i = 1; i <= 16; ++i)
            if (frt[i] && snd[i]) {
                ans = i;
                ++cnt;
            }
        if (cnt == 1)
            printf("Case #%d: %d\n", t, ans);
        else if(cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", t);
        else
            printf("Case #%d: Bad magician!\n", t);
    }
    return 0;
}