#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
#define MAXNUM 2000010


int map[5][5], map2[5][5];
int main()
{
    //freopen("A-small-attempt0.in","r", stdin);
    //freopen("A-small-attempt0.out","w", stdout);
    int t, a, b;
    cin >> t;
    for(int cas = 1; cas <= t; cas++){
        memset(map, 0, sizeof(map));
        memset(map2, 0, sizeof(map2));
        cin >> a;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> map[i][j];
            }
        }
        cin >> b;
        a--, b--;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin >> map2[i][j];
            }
        }
        int ans = 0, idx;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(map2[b][i] == map[a][j]){
                    ans++; idx = map[a][j]; break;
                }
            }
        }
        if(ans == 0){ printf("Case #%d: Volunteer cheated!\n", cas); }
        else if(ans == 1) printf("Case #%d: %d\n", cas, idx);
        else printf("Case #%d: Bad magician!\n", cas);
    }
    return 0;
}

