#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int cache[101][201][1001];
int h[101];
int g[100];
int dshot;
int tshot;
int n;

int maxGold(int monster, int hp, int spare) {
    if (monster == n)
        return 0;
    if (hp <= 0) {
        monster++;
        hp = h[monster];
        return maxGold(monster, hp, spare);
    }
    if (cache[monster][hp][spare] != -1)
        return cache[monster][hp][spare];
    int ans = 0;
    //take a free shot
    if (spare > 0) {
        if (hp <= dshot)
            ans = max(ans, g[monster] + maxGold(monster+1, h[monster+1], spare-1));
        else
            ans = max(ans, maxGold(monster, hp-dshot, spare-1));
    }
    
    //take an actual shot
    if (hp <= dshot)
        ans = max(ans, g[monster] + maxGold(monster+1, h[monster+1]-tshot, 0));
    else
        ans = max(ans, maxGold(monster, hp-dshot-tshot, 0));
    
    //do nothing
    ans = max(ans, maxGold(monster, hp-tshot, spare+1));
    cache[monster][hp][spare] = ans;
    return ans;
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d %d %d", &dshot, &tshot, &n);
        int i, j, k;
        for (i = 0; i < n; i++)
            scanf("%d %d", &h[i], &g[i]);
        
        for (i = 0; i < n; i++)
            for (j = 0; j < 201; j++)
                for (k = 0; k < 1001; k++)
                    cache[i][j][k] = -1;
        
        printf("%d\n", maxGold(0, h[0], 0));
    }
}