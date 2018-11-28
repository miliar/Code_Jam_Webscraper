#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
bool check(string s[4], char ch)
{
    int i, j;
    bool flag = true;
    for(i=0; i<4; i++)
    {
        flag = true;
        for(j=0; j<4; j++)
        {
            if(!(s[i][j] == ch || s[i][j] == 'T'))
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            return true;
        }
    }

    for(i=0; i<4; i++)
    {
        flag = true;
        for(j=0; j<4; j++)
        {
            if(!(s[j][i] == ch || s[j][i] == 'T'))
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            return true;
        }
    }

    for(i=0; i<4; i++)
    {
        flag = true;
        if(!(s[i][i] == ch || s[i][i] == 'T'))
        {
            flag = false;
            break;
        }
    }
    if(flag)
    {
        return true;
    }

    flag = true;

    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(i + j == 3)
            {
                if(!(s[i][j] == ch || s[i][j] == 'T'))
                {
                    flag = false;
                    break;
                }
            }
        }
    }

    if(flag)
    {
        return true;
    }
    return false;
}
bool gameOver(string s[4])
{
    int i, j;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(s[i][j] == '.')
            {
                return false;
            }
        }
    }
    return true;
}
bool draw(string s[4])
{
    int i, j;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            if(s[i][j] == '.')
            {
                return false;
            }
        }
    }
    return true;
}
int main ()
{
    freopen("A-large.in", "r",stdin);
    freopen("out.txt", "w", stdout);
    int T,caseno = 1;
    cin >> T;
    while(T--)
    {
        string s[4];
        int i, j;
        for(i=0; i<4; i++)
        {
            cin >>s[i];
        }

        bool doesXWin = check(s, 'X');
        bool doesOWin = check(s, 'O');
        bool isGameOver = gameOver(s);
        bool isDraw = draw(s);

        if(doesXWin)
        {
            cout<<"Case #"<<caseno<<": X won"<<endl;
        }
        else if(doesOWin)
        {
            cout<<"Case #"<<caseno<<": O won"<<endl;
        }
        else if(isDraw)
        {
            cout<<"Case #"<<caseno<<": Draw"<<endl;
        }
        else if(!isGameOver)
        {
            cout<<"Case #"<<caseno<<": Game has not completed"<<endl;
        }
        caseno++;
    }
    return 0;
}
