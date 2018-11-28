#include <cstdio>
#include <algorithm>
using namespace std;
const int MAX = 101;

int t[MAX][MAX][3];

void prep(int n, int m)
{
    for(int i = 0; i < n; ++ i){
        int maxnum = 0;

        for(int j = 0; j < m; ++ j){
            maxnum = max(t[i][j][0], maxnum);
            if(maxnum > t[i][j][0]) t[i][j][1] = 1;
        }
    }

    for(int i = 0; i < n; ++ i){
        int maxnum = 0;

        for(int j = m-1; j >= 0; -- j){
            maxnum = max(t[i][j][0], maxnum);
            if(maxnum > t[i][j][0]) t[i][j][1] = 1;
        }
    }

    for(int i = 0; i < m; ++ i){
        int maxnum = 0;

        for(int j = 0; j < n; ++ j){
            maxnum = max(t[j][i][0], maxnum);
            if(maxnum > t[j][i][0]) t[j][i][2] = 1;
        }
    }

    for(int i = 0; i < m; ++ i){
        int maxnum = 0;

        for(int j = n-1; j >= 0; -- j){
            maxnum = max(t[j][i][0], maxnum);
            if(maxnum > t[j][i][0]) t[j][i][2] = 1;
        }
    }
}

bool dasie(int n, int m)
{
    for(int i = 0; i < n; ++ i)
        for(int j = 0; j < m; ++ j)
            if( t[i][j][1] && t[i][j][2] )
                return 0;
    return 1;
}

int main()
{
    int z;
    scanf("%d", &z);
    int nr = 0;
    while(nr < z && ++ nr){
        printf("Case #%d: ", nr);

        int n, m;
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; ++ i)
            for(int j = 0; j < m; ++ j){
                scanf("%d", &t[i][j][0]);
                t[i][j][1] = t[i][j][2] = 0;
            }

        prep(n, m);

        if( dasie(n, m) ) puts("YES");
        else puts("NO");
    }
}
