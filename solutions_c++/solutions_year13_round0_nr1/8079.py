#include <stdio.h>

int checkPlayer(char a, char b, char c, char d, char X)
{
    char arr[4];
    arr[0] = a;
    arr[1] = b;
    arr[2] = c;
    arr[3] = d;
    int cntT = 0;
    for(int i = 0; i<4; i++)
    {
        if(arr[i]!= X&&arr[i]!='T')
        {
            return 0;
        }
        else if(arr[i] == 'T')
        {
            if(cntT<1)
            {
                cntT++;
            }
            else
            {
                return 0;
            }
        }
    }
    return 1;
}

int check(char a, char b, char c, char d)
{
    if(checkPlayer(a,b,c,d, 'X'))
    {
        return 1;
    }

    if(checkPlayer(a,b,c,d, 'O'))
    {
        return 2;
    }

    return 0;
}


int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int n = 0;
    int res = 0;
    char mat[4][4];
    char a1,b1,c1,d1, a2,b2,c2,d2;
    int i, j;
    int rowChk = 0;
    int colChk = 0;
    char temp;

    while(scanf("%d", &n)!=EOF)
    {
        for(int k = 1 ; k<=n; k++)
        {
            res = 0;
            int blankSpace = 0;
            for( i = 0; i<4; i++)
            {
                for( j=0; j<4; j++)
                {
                    mat[i][j] = '\0';
                }
            }

            for( i = 0; i<4; i++)
            {
                for( j=0; j<4; j++)
                {
                    temp = '\0';
                    scanf("%c", &temp);
                    if(temp!='\n')
                    {
                        mat[i][j] = temp;
                    }
                    else
                    {
                        scanf("%c", &mat[i][j]);
                    }

                    if(temp == '.')
                    {
                        blankSpace = 1;
                    }
                }
            }

            for( i = 0; i<4; i++)
            {
                for( j=0; j<4; j++)
                {
                    switch(j)
                    {
                        case 0:
                            a1 = mat[i][j];
                            a2 = mat[j][i];
                        break;
                        case 1:
                            b1 = mat[i][j];
                            b2 = mat[j][i];
                        break;
                        case 2:
                            c1 = mat[i][j];
                            c2 = mat[j][i];
                        break;
                        case 3:
                            d1 = mat[i][j];
                            d2 = mat[j][i];
                        rowChk = check(a1,b1,c1,d1);
                        colChk = check(a2,b2,c2,d2);
                        if(rowChk)
                            res = rowChk;
                        else if(colChk)
                            res = colChk;
                        break;
                    }
                }
                if(res == 1)
                {
                    printf("Case #%d: X won\n", k);
                    break;
                }
                else if(res == 2)
                {
                    printf("Case #%d: O won\n", k);
                    break;
                }
            }

            if(i == 4)
            {
                int chkDiag1 = check(mat[0][0], mat[1][1], mat[2][2], mat[3][3]);
                int chkDiag2 = check(mat[3][0], mat[2][1], mat[1][2], mat[0][3]);

                if(chkDiag1)
                {
                    res = chkDiag1;
                }
                else if(chkDiag2)
                {
                    res = chkDiag2;
                }

                if(res == 1)
                {
                    printf("Case #%d: X won\n", k);
                }
                else if(res == 2)
                {
                    printf("Case #%d: O won\n", k);
                }
                else
                {
                    if(blankSpace==1)
                    {
                        printf("Case #%d: Game has not completed\n", k);
                    }
                    else
                    {
                        printf("Case #%d: Draw\n", k);
                    }
                }
            }
            scanf("%c", &temp);
        }
    }
    //es = check('X', 'T', 'X', 'T', 'X');
    //printf("%d", res);
    return 0;
}
