#include<iostream>
#include<stdio.h>
using namespace std;

int checkDiag(char a[4][4], char s)
{
    int i, c=0;
    for (i = 0; i < 4; i++)
    {
            if (a[i][i] == s)
                c++;
           // cout << "c diag " << c << endl;
    }
   //cout << "Check DIAG " <<c <<endl;
    if (c == 4)
        return 1;
    else
        return 0;
}

int checkReverseDiag(char a[4][4], char s)
{
    int i, c=0;
    for (i = 0; i < 4; i++)
    {
        if (a[i][3-i] == s)
                c++;
    }
    //cout << "Check REVERSE DIAG" <<c<<endl;
    if (c == 4)
        return 1;
    else
        return 0;
}

int checkRows(char a[4][4], char s)
{
    int i, j ,c=0;
    for (i = 0; i<4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            if (a[i][j] == s)
                c++;
            //cout << "c1 = " <<c <<"\n";
            if (c == 4)
                return 1;
        }
        c = 0;
    }
    return 0;
}

int checkCols(char a[4][4], char s)
{
    int i, j ,c=0;
    for (i = 0; i<4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            if (a[j][i] == s)
                c++;
           // cout << "c2 = " <<c <<"\n";
            if (c == 4)
                return 1;
        }
        c = 0;
    }
    return 0;
}

int checkForX(char a[4][4])
{
    int pxt, pyt, i, j, c1=0, c2=0, c3=0, c4=0, f=0;

    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            if (a[i][j] == 'T')
            {
                pxt = i;
                pyt = j;
                a[i][j] = 'X';
                f=1;
                break;
            }
        }
    }
    c1 = checkDiag(a, 'X');
    c2 = checkReverseDiag(a, 'X');//iag(a, 'X');
    c3 = checkRows(a, 'X');
    c4 = checkCols(a, 'X');
    if (f==1)
        a[pxt][pyt] = 'T';

    if (c1 ==1 || c2 ==1|| c3 == 1|| c4 == 1)
        return 1;
    else
        return 0;
}

int checkForO(char a[4][4])
{
    int pxt, pyt, i, j, c1=0, c2=0, c3=0, c4=0, f=0;
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            if (a[i][j] == 'T')
            {
                pxt = i;
                pyt = j;
                a[i][j] = 'O';
                f = 1;
                break;
            }
        }
    }
    c1 = checkDiag(a, 'O');
    c2 = checkReverseDiag(a, 'O');//iag(a, 'X');
    c3 = checkRows(a, 'O');
    c4 = checkCols(a, 'O');
    if (f == 1)
        a[pxt][pyt] = 'T';

    if (c1 ==1 || c2 ==1|| c3 == 1|| c4 == 1)
        return 1;
    else
        return 0;
}

int checkForDraw(char a[4][4])
{
    int i, j;
    for (i = 0; i < 4; i++)
    {
        for (j =0; j < 4; j++)
        {
            if (a[i][j] == '.')
            {
                return 0;
            }
        }
    }
    return 1;
}

int main()
{
    long testcases,x;
    int i, j;
    int d=2;
    char a[4][4];// op[4][4];
    freopen("A-large.in","r",stdin);
    freopen("op.txt","w", stdout);
    cin >> testcases;
    for (x = 0; x < testcases; x++)
    {
    for (i=0; i<4; i++)
        for (j=0; j<4; j++)
            cin >> a[i][j];

    i = checkForX(a);
    j = checkForO(a);
    if (i == 1)
        cout <<"Case #"<<x+1<<": X won\n";
    else if (j == 1)
        cout <<"Case #"<<x+1<<": O won\n";
    else
    {
        d = checkForDraw(a);
        if (d == 1)
            cout <<"Case #"<<x+1<<": Draw\n";
        else
            cout <<"Case #"<<x+1<<": Game has not completed\n";
    }
    }
    return 0;
}
