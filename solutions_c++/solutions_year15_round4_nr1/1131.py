#include <cstdio>
#define scanf(args...) (scanf(args) ? : 0)
const int MAXN = 1005;

char T[MAXN][MAXN];

int main() {
    int t;
    scanf("%d", &t);

    for (int test=0; test<t; test++) {
        int r, c;
        scanf("%d%d", &r, &c);
        
        for (int i=0; i<r; i++)
            scanf("%s", T[i]);
        
        int res = 0;
        bool fail = false;
        for (int i=0; i<r; i++)
            for (int j=0; j<c; j++) {
                if (T[i][j] == '.')
                    continue;
                bool founddown = false;
                bool foundup = false;
                bool foundleft = false;
                bool foundright = false;
                bool any = false;
                    
                for (int k=i+1; k<r; k++)
                    if (T[k][j] != '.')
                        founddown = true;
                for (int k=0; k<i; k++)
                    if (T[k][j] != '.')
                        foundup = true;
                for (int k=j+1; k<c; k++)
                    if (T[i][k] != '.')
                        foundright = true;
                for (int k=0; k<j; k++)
                    if (T[i][k] != '.')
                        foundleft = true;

                any = founddown || foundup || foundleft || foundright;

                if (!any)
                    fail = true;

                if (T[i][j] == '<') {
                    if (!foundleft)
                        res++;
                }
                else if (T[i][j] == '^') {
                    if (!foundup)
                        res++;
                }
                else if (T[i][j] == '>') {
                    if (!foundright)
                        res++;
                }
                else if (T[i][j] == 'v')
                    if (!founddown)
                        res++;
            }

        printf("Case #%d: ", test+1);

        if (fail)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", res);
    }
}

