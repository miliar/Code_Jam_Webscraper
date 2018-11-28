#include <iostream>
#include <string>

using namespace std;

char ga[4][4];

void startAnalyse();
void printAnalyse(int);
int horizontalCharAnalyse(char);
int verticalCharAnalyse(char);
int rightDiagonalCharAnalyse(char);
int leftDiagonalCharAnalyse(char);
int drawInc();

int main()
{
    int n,ni,i,j,k,cmp;
    cin >> n;
    string line;
    getline(cin,line);
    ni = 0;
    char array[n][4][4];
    while(ni!=n)
    {
        for(i=0;i<5;i++)
        {
            getline(cin,line);
            cmp = line.compare("\n");
            if(cmp != -1)
            {
                array[ni][i][0] = line[0];
                array[ni][i][1] = line[1];
                array[ni][i][2] = line[2];
                array[ni][i][3] = line[3];
            }
        }
        ni++;
    }
    for(i=0; i<n; i++)
    {
        cout << "Case #" << (i+1) << ": ";
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                ga[j][k] = array[i][j][k];
            }
        }
        startAnalyse();
        cout << "\n";
    }
    return 0;
}

void startAnalyse()
{
    int result = horizontalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }

     result = verticalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }

     result = rightDiagonalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }

    result = leftDiagonalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }



    result = horizontalCharAnalyse('O');
    if(result == 1)
    {
        printAnalyse(2);
        return;
    }
    /*esult = verticalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }*/
    result = verticalCharAnalyse('O');
    if(result == 1)
    {
        printAnalyse(2);
        return;
    }
    /*result = rightDiagonalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }*/
    result = rightDiagonalCharAnalyse('O');
    if(result == 1)
    {
        printAnalyse(2);
        return;
    }
    /*result = leftDiagonalCharAnalyse('X');
    if(result == 1)
    {
        printAnalyse(1);
        return;
    }*/
    result = leftDiagonalCharAnalyse('O');
    if(result == 1)
    {
        printAnalyse(2);
        return;
    }
    //now it is either a draw or an incomplete game
    //for a incomplete game, it should contain at least one '.'
    result = drawInc();
    if(result == 0)
    {
        printAnalyse(3); // draw game
    }
    else
        printAnalyse(4); // incomplete game
}

int drawInc()
{
    int i,j;
    char c;
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            c = ga[i][j];
            if(c == '.')
            {
                return 1;
            }
        }
    }
    return 0;
}

int horizontalCharAnalyse(char p)
{
    int i,j,count;
    char c;
    for(i=0;i<4;i++)
    {
        count = 0;
        for(j=0;j<4;j++)
        {
            c = ga[i][j];
            if(c == p || c == 'T')
            {
                count ++;
            }
            else
            {
                break;
            }
        }
        if(count == 4)
        {
            return 1;
        }
    }
    return 0;
}

int verticalCharAnalyse(char p)
{
    int i,j,count;
    char c;
    for(i=0;i<4;i++)
    {
        count = 0;
        for(j=0;j<4;j++)
        {
            c = ga[j][i];
            if(c == p || c == 'T')
            {
                count ++;
            }
            else
            {
                break;
            }
        }
        if(count == 4)
        {
            return 1;
        }
    }
    return 0;
}

int rightDiagonalCharAnalyse(char p)
{
    int i,count = 0 ;
    char c;
    for(i=0;i<4;i++)
    {
        c = ga[i][i];
        if(c == p || c == 'T')
        {
            count++;
        }
        else
        {
            break;
        }
    }
    if(count == 4)
    {
        return 1;
    }
    return 0;
}

int leftDiagonalCharAnalyse(char p)
{
    int i,count = 0 ;
    char c;
    for(i=0;i<4;i++)
    {
        c = ga[i][3-i];
        if(c == p || c == 'T')
        {
            count++;
        }
        else
        {
            break;
        }
    }
    if(count == 4)
    {
        return 1;
    }
    return 0;
}

void printAnalyse(int n)
{
    switch(n)
    {
        case 1 :
            cout << "X won";
            break;
        case 2 :
            cout << "O won";
            break;
        case 3 :
            cout << "Draw";
            break;
        case 4 :
            cout << "Game has not completed";
            break;
    }
}
