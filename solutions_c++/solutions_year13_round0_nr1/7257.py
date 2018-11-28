#include <cstdio>

char m[4][4];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out", "w", stdout);

    int T;
    int bola, xis;
    bool over, win;

    scanf("%d", &T);

    for (int i=1; i<=T; i++)
    {
        scanf("%s", m[0]);
        scanf("%s", m[1]);
        scanf("%s", m[2]);
        scanf("%s", m[3]);

        /*for (int j=0; j<4; j++)
            for (int k=0; k<4; k++)
                printf("%c\n", m[j][k]);*/

        win = false;
        over = true;

        for (int j=0; j<4 && win==false; j++)
        {
            bola = xis = 0;
            for (int k=0; k<4; k++)
            {
                if (m[j][k]=='X')
                    xis++;
                else if (m[j][k]=='O')
                    bola++;
                else if (m[j][k]=='T')
                {
                    xis++;
                    bola++;
                }
                else
                    over = false;
            }
            if (xis==4 || bola==4)
                win=true;
        }

        for (int k=0; k<4 && win==false; k++)
        {
            bola = xis = 0;
            for (int j=0; j<4; j++)
            {
                if (m[j][k]=='X')
                    xis++;
                else if (m[j][k]=='O')
                    bola++;
                else if (m[j][k]=='T')
                {
                    xis++;
                    bola++;
                }
            }
            if (xis==4 || bola==4)
                win=true;
        }

        if (win == false)
        {
            bola = xis = 0;
            for (int j=0; j<4; j++)
            {
                if (m[j][j]=='X')
                    xis++;
                else if (m[j][j]=='O')
                    bola++;
                else if (m[j][j]=='T')
                {
                    xis++;
                    bola++;
                }
            }

            if (xis==4 || bola==4)
                win=true;
        }

        if (win == false)
        {
            bola = xis = 0;
            for (int j=0; j<4; j++)
            {
                if (m[j][3-j]=='X')
                    xis++;
                else if (m[j][3-j]=='O')
                    bola++;
                else if (m[j][3-j]=='T')
                {
                    xis++;
                    bola++;
                }
            }

            if (xis==4 || bola==4)
                win=true;
        }

        if (win==false)
        {
            if (over)
                printf("Case #%d: Draw\n", i);
            else
                printf("Case #%d: Game has not completed\n", i);
        }
        else
        {
            if (xis==4)
                printf("Case #%d: X won\n", i);
            else
                printf("Case #%d: O won\n", i);
        }

    }

    return(0);
}
