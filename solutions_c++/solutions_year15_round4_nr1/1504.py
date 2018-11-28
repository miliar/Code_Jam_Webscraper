#include <stdio.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputAlarge.txt", "w", stdout);
    int t, r, c;
    scanf("%d", &t);
    int dir[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
    for (int testn = 1; testn <= t; testn++)
    {
        bool w = 0;

        scanf("%d%d\n", &r, &c);
        char a[r][c];
        int ans = 0;
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++) scanf("%c", &a[i][j]);
            scanf("\n");
        }
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++) if (a[i][j] != '.')
            {
                int k, i0 = i, j0 = j;
                if (a[i][j] == '<') k = 1;
                else if (a[i][j] == '>') k = 3;
                else if (a[i][j] == '^') k = 0;
                else k = 2;
                i0 += dir[k][0]; j0 += dir[k][1];


                bool w0 = false;
                while (true)
                {
                   if (i0 < 0 || j0 < 0 || i0 == r || j0 == c) { ans++; w0 = true; break; }
                   if (a[i0][j0] != '.') break;
                   i0 += dir[k][0]; j0 += dir[k][1];

                }
                if (w0)
                {
                    int q = 3;
                    for (int cnt = 0; cnt < 3; cnt++)
                    {
                        k = (k + 1) % 4;
                        i0 = i + dir[k][0]; j0 = j + dir[k][1];
                        while (true)
                        {
                            if (i0 < 0 || j0 < 0 || i0 == r || j0 == c) { q--; break; }
                            if (a[i0][j0] != '.') break;
                            i0 += dir[k][0]; j0 += dir[k][1];
                        }
                    }
                    if (q == 0) w = true;
                }


            }
        if (!w)
        {
            printf("Case #%d: %d\n", testn, ans);

        }
        else
        {
            printf("Case #%d: IMPOSSIBLE\n", testn);


        }
    }
    return 0;
}
