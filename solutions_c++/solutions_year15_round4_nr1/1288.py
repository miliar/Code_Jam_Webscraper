#include <cstdio>
#include <cstring>

int r, c;
char map[110][110];
int ans[110][110];

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; ++cas)
    {
        scanf("%d %d", &r, &c);
        for(int i=0; i<r; ++i)
            scanf("%s", map[i]);
        memset(ans, 0, sizeof(ans));

        for(int i=0; i<r; ++i) //left
        {
            int j=0;
            while(map[i][j]=='.'&&j<c) ++j;
            if(j<c) ans[i][j] += 1;
        }
        for(int i=0; i<r; ++i) //right
        {
            int j=c-1;
            while(map[i][j]=='.'&&j>=0) --j;
            if(j>=0) ans[i][j] += 2;
        }
        for(int j=0; j<c; ++j) //up
        {
            int i=0;
            while(map[i][j]=='.'&&i<r) ++i;
            if(i<r) ans[i][j] += 4;
        }
        for(int j=0; j<c; ++j) //down
        {
            int i=r-1;
            while(map[i][j]=='.'&&i>=0) --i;
            if(i>=0) ans[i][j] += 8;
        }

        bool imp = false;
        int no = 0;
        for(int i=0; i<r; ++i)
            for(int j=0; j<c; ++j)
            {
                if(ans[i][j] == 15) imp = true;
                if(ans[i][j] != 0)
                {
                    if(map[i][j] == '<') ans[i][j] &= 1;
                    if(map[i][j] == '>') ans[i][j] &= 2;
                    if(map[i][j] == '^') ans[i][j] &= 4;
                    if(map[i][j] == 'v') ans[i][j] &= 8;
                    if(ans[i][j] != 0) ++no;
                }
            }
        printf("Case #%d: ", cas);
        if(imp) puts("IMPOSSIBLE");
        else printf("%d\n", no);
    }
    return 0;
}
