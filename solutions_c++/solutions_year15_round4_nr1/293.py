#include <stdio.h>

int r, c;

char a[110][110];
char good[128];

int ans;

int main()
{
    int t0, t;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        scanf("%d%d", &r, &c);
        for(int i = 0; i < r; i++)
            scanf("%s", a[i]);
        ans = 0;
        int bad = 0;
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++){
                int k;
                if(a[i][j] == '.')
                    continue;
                int possible = 0;
                //good['v'] = good['^'] = good['<'] = goo
                for(k = i-1; k >= 0 && a[k][j] == '.' ; k--);
                possible |= good['^'] = k >= 0;
                for(k = i+1; k < r && a[k][j] == '.' ; k++);
                possible |= good['v'] = k < r;
                for(k = j-1; k >= 0 && a[i][k] == '.' ; k--);
                possible |= good['<'] = k >= 0;
                for(k = j+1; k < c && a[i][k] == '.' ; k++);
                possible |= good['>'] = k < c;
                if (!possible)
                    bad = 1;
                if (!good[a[i][j]])
                    ans++;
                }
        if(bad)
            printf("Case #%d: IMPOSSIBLE\n", t0 + 1);
        else
            printf("Case #%d: %d\n", t0 + 1, ans);
        }

    return 0;
}
