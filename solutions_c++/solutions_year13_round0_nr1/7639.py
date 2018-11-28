#include <stdio.h>

int i;
char board[4][4];
FILE *in;
FILE *out;

bool CheckHor()
{
    for (int j = 0; j < 4; j++)
    {
        for (int k = 0, x = 4, o = 4; k < 4; k++)
        {
            if (board[j][k] == 'X' || board[j][k] == 'T')
                x--;
            if (board[j][k] == 'O' || board[j][k] == 'T')
                o--;

            if (!x)
            {
                fprintf(out, "Case #%d: X won\n", i+1);
                return true;
            }
            if (!o)
            {
                fprintf(out, "Case #%d: O won\n", i+1);
                return true;
            }
        }
    }

    return false;
}

bool CheckVer()
{
    for (int j = 0; j < 4; j++)
    {
        for (int k = 0, x = 4, o = 4; k < 4; k++)
        {
            if (board[k][j] == 'X' || board[k][j] == 'T')
                x--;
            if (board[k][j] == 'O' || board[k][j] == 'T')
                o--;

            if (!x)
            {
                fprintf(out, "Case #%d: X won\n", i+1);
                return true;
            }
            if (!o)
            {
                fprintf(out, "Case #%d: O won\n", i+1);
                return true;
            }
        }
    }

    return false;
}

bool CheckDia()
{
    for (int j = 0, k = 0, x = 4, o = 4; j < 4; j++, k++)
    {
        if (board[j][k] == 'X' || board[j][k] == 'T')
            x--;
        if (board[j][k] == 'O' || board[j][k] == 'T')
            o--;

        if (!x)
        {
            fprintf(out, "Case #%d: X won\n", i+1);
            return true;
        }
        if (!o)
        {
            fprintf(out, "Case #%d: O won\n", i+1);
            return true;
        }
    }

    for (int j = 3, k = 0, x = 4, o = 4; j >= 0; j--, k++)
    {
        if (board[j][k] == 'X' || board[j][k] == 'T')
            x--;
        if (board[j][k] == 'O' || board[j][k] == 'T')
            o--;

        if (!x)
        {
            fprintf(out, "Case #%d: X won\n", i+1);
            return true;
        }
        if (!o)
        {
            fprintf(out, "Case #%d: O won\n", i+1);
            return true;
        }
    }

    return false;
}

int main()
{
    in = fopen("A-large.in", "r");
    out = fopen("A-large.out", "w");

	int n;

	fscanf(in, "%d\n", &n);

	for (i = 0; i < n; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			fscanf(in, "%c%c%c%c\n", &board[j][0], &board[j][1], &board[j][2], &board[j][3]);
		}

        if (CheckHor()) continue;
        if (CheckVer()) continue;
        if (CheckDia()) continue;

        bool flag = true;
        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                if (board[j][k] == '.')
                    flag = false;
            }
        }

        if (flag)
        {
            fprintf(out, "Case #%d: Draw\n", i+1);
            continue;
        }

        fprintf(out, "Case #%d: Game has not completed\n", i+1);
	}

	return 0;
}
