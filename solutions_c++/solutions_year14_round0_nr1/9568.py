//In the name of Allah

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <bitset>
#include <math.h>
#include <queue>
#include <map>
#include <set>
#include <limits.h>
#include <limits>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
using namespace std;

int T, g1[4][4], g2[4][4], b[20], r1, r2;
int main(){
    freopen("a.out", "w", stdout);
    
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%d", &r1);
        r1--;
        
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            scanf("%d", &g1[i][j]);
    
        scanf("%d", &r2);
        r2--;
        
        for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            scanf("%d", &g2[i][j]);

        memset(b, 0, sizeof b);
        
        for(int i = 0; i < 4; i++)b[g1[r1][i]]++;
        
        int c = 0, x;
        for(int i = 0; i < 4; i++){
            if(b[g2[r2][i]] > 0)c++, x = i;
        }
        
        if(c == 1)printf("Case #%d: %d\n", t, g2[r2][x]);
        else if(c > 1)printf("Case #%d: Bad magician!\n", t);
        else printf("Case #%d: Volunteer cheated!\n", t);
    }
    
    return 0;
}