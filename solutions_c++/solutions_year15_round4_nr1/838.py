#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;
typedef long long LL;
typedef unsigned int uint;

const int MOD = 1000000007;
const double PI = acos(-1.0);

const int MAXN = 100000;

char mp[110][110];
bool visit[110][110];
int r,c;
bool check(int row, int col) {
    int ans = 0;
    for(int i=0; i<r; i++) {
        if(i == row)    continue;
        if(mp[i][col] != '.') {
            ans++;
        }
    }
    for(int j=0; j<c; j++) {
        if(j == col) continue;
        if(mp[row][j] != '.') {
            ans++;
        }
    }
    if(ans == 0)    return false;
    return true;
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; cas++) {
        memset(visit, false, sizeof(visit));
        scanf("%d%d", &r, &c);
        for(int i=0; i<r; i++) {
            scanf("%s", mp[i]);
        }
        int ans = 0;
        bool has = true;
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                if(mp[i][j] != '.') {
                    if(check(i, j) == false) {
                        has = false;

                    }
                    if(mp[i][j] == '<') {
                        bool ok = false;
                        for(int k=j-1; k>=0; k--) {
                            if(mp[i][k] != '.') {
                                ok = true;
                            }
                        }
                        if(ok == false) {
                            ans ++;
                        }
                    }
                    else if(mp[i][j] == '>') {
                        bool ok = false;
                        for(int k=j+1; k<c; k++) {
                            if(mp[i][k] != '.') {
                                ok = true;
                            }
                        }
                        if(ok == false) {
                            ans++;
                        }
                    }
                    else if(mp[i][j] == '^') {
                        bool ok = false;
                        for(int k=i-1; k>=0; k--) {
                            if(mp[k][j] != '.') {
                                ok = true;
                            }
                        }
                        if(!ok) {
                            ans++;
                        }
                    }
                    else if(mp[i][j] == 'v') {
                        bool ok = false;
                        for(int k=i+1; k<r; k++) {
                            if(mp[k][j] != '.') {
                                ok = true;
                            }
                        }
                        if(!ok) {
                            ans++;
                        }
                    }
                }
            }

        }
        if(has)
        printf("Case #%d: %d\n", cas, ans);
        else {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        }
    }

    return 0;
}
