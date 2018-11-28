#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define inf 1000000000
#define MAXN 100

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for (int qwertz = 0; qwertz < t; ++qwertz) {
        int n, m;
        scanf("%d%d", &n, &m);
        
        int lawn[MAXN][MAXN], row[MAXN] = {0}, column[MAXN] = {0};
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &lawn[i][j]);
                
                if (lawn[i][j] > row[i]) row[i] = lawn[i][j];
                if (lawn[i][j] > column[j]) column[j] = lawn[i][j];
            }
        }
        
        bool canMakeIt = true;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (lawn[i][j] < row[i] && lawn[i][j] < column[j]) canMakeIt = false;
            }
        }
        
        printf("Case #%d: %s\n", qwertz+1, canMakeIt ? "YES" : "NO");
    }
    
    return 0;
}
