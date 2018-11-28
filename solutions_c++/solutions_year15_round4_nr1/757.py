#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int R,C;
char M[105][105];

bool check(int r, int c, int dr, int dc){
    while(r >= 0 && r < R && c >= 0 && c < C){
        if(M[r][c] != '.')
            break;
        else{
            r += dr;
            c += dc;
        }
    }

    if(r == -1 || r == R || c == -1 || c == C)
        return false;

    return true;
}

int main(){
    //ios::sync_with_stdio(0);

    int T;

    scanf("%d",&T);

    for(int tc = 1;tc <= T;++tc){
        scanf("%d %d",&R,&C);

        for(int i = 0;i < R;++i)
            scanf("%s",M[i]);

        int ans = 0;

        for(int i = 0;i < R && ans != -1;++i){
            for(int j = 0;j < C && ans != -1;++j){
                if(M[i][j] == '.') continue;
                int dr,dc;

                if(M[i][j] == '>') dr = 0,dc = 1;
                if(M[i][j] == '<') dr = 0,dc = -1;
                if(M[i][j] == '^') dr = -1,dc = 0;
                if(M[i][j] == 'v') dr = 1,dc = 0;

                bool ok = check(i + dr,j + dc,dr,dc);

                if(!ok){
                    if(!check(i,j + 1,0,1) && !check(i,j - 1,0,-1) && !check(i - 1,j,-1,0) && !check(i + 1,j,1,0))
                        ans = -1;
                    else
                        ++ans;
                }
            }
        }

        printf("Case #%d: ",tc);
        if(ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);
    }

    return 0;
}