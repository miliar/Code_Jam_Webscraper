#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 4;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T, A1, A2, a[maxn][maxn], b[maxn][maxn], vis[20], kase = 0;
    scanf("%d", &T);
    while(T--) {
        scanf("%d", &A1);
        A1--;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d", &a[i][j]);
        memset(vis, 0, sizeof(vis));
        for(int i = 0; i < 4; i++) vis[a[A1][i]] = true;
        scanf("%d", &A2);
        A2--;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                scanf("%d", &b[i][j]);
        int cnt = 0, ret;
        for(int i = 0; i < 4; i++)
            if(vis[b[A2][i]]) {
                cnt++;
                ret = b[A2][i];
            }

        if(cnt == 0) printf("Case #%d: Volunteer cheated!\n", ++kase);
        else if(cnt == 1) printf("Case #%d: %d\n", ++kase, ret);
        else printf("Case #%d: Bad magician!\n", ++kase);
    }
    return 0;
}

/*

3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Case #1: 7
Case #2: Bad magician!
Case #3: Volunteer cheated!

*/
