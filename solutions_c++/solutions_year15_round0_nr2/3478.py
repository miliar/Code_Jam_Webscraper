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

int T, D, P[1005], n;
int main(){
    freopen("B.txt", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    
    scanf("%d", &T);
    while(T--){
        scanf("%d", &D);
        for(int i = 0; i < D; i++)
            scanf("%d", &P[i]);
        
        sort(P, P + D);
        reverse(P, P + D);

        int res = 1 << 30;
        for(int mx = 1; mx <= 1000; mx++){
            int c = 0;
            for(int i = 0; i < D; i++)
                if(P[i] > mx)c += (P[i] - 1) / mx;
            res = min(res, c + mx);
        }
        printf("Case #%d: %d\n", ++n, res);
    }
    return 0;
}