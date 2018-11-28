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
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <string.h>
#include <assert.h>
#include <numeric>
using namespace std;

int T, N, M, a[105][105], b[105][105];

int main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    scanf("%d", &T);
    for(int case_num = 1; case_num <= T; case_num++){
        scanf("%d %d", &N, &M);
        for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            scanf("%d", &a[i][j]);
            b[i][j] = 100;
        }
        
        for(int i = 0; i < N; i++){
            int m = 0;
            for(int j = 0; j < M; j++)
                m = max(m, a[i][j]);
            
            for(int j = 0; j < M; j++)
                b[i][j] = min(b[i][j], m);
        }
        
        for(int j = 0; j < M; j++){
            int m = 0;
            for(int i = 0; i < N; i++)
                m = max(m, a[i][j]);
            
            for(int i = 0; i < N; i++)
                b[i][j] = min(b[i][j], m);
        }
        
        bool f = true;
        for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++){
            if(a[i][j] != b[i][j])f = false;
        }
        
        if(f)printf("Case #%d: YES\n", case_num);
        else printf("Case #%d: NO\n", case_num);
    }
    return 0;
}