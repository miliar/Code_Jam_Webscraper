#include <iostream>
#include <conio.h>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("results.out", "w", stdout);
    int n;
    cin>>n;
    for(int count=0;count<n;count++)
    {
        string input[4];
        for(int i=0;i<4;i++)
        {
            cin>>input[i];
        }
        cout<<"Case #"<<count+1<<": ";
        for(int i=0;i<4;i++)
        {
            if((input[i][0]=='X'||input[i][0]=='T')&&(input[i][1]=='X'||input[i][1]=='T')&&(input[i][2]=='X'||input[i][2]=='T')&&(input[i][3]=='X'||input[i][3]=='T'))
            {
                cout<<"X won"<<endl;
                goto end;
            }
            else if((input[i][0]=='O'||input[i][0]=='T')&&(input[i][1]=='O'||input[i][1]=='T')&&(input[i][2]=='O'||input[i][2]=='T')&&(input[i][3]=='O'||input[i][3]=='T'))
            {
                cout<<"O won"<<endl;
                goto end;
            }
        }
        for(int i=0;i<4;i++)
        {
            if((input[0][i]=='X'||input[0][i]=='T')&&(input[1][i]=='X'||input[1][i]=='T')&&(input[2][i]=='X'||input[2][i]=='T')&&(input[3][i]=='X'||input[3][i]=='T'))
            {
                cout<<"X won"<<endl;
                goto end;
            }
            else if((input[0][i]=='O'||input[0][i]=='T')&&(input[1][i]=='O'||input[1][i]=='T')&&(input[2][i]=='O'||input[2][i]=='T')&&(input[3][i]=='O'||input[3][i]=='T'))
            {
                cout<<"O won"<<endl;
                goto end;
            }
        }
        if((input[0][0]=='X'||input[0][0]=='T')&&(input[1][1]=='X'||input[1][1]=='T')&&(input[2][2]=='X'||input[2][2]=='T')&&(input[3][3]=='X'||input[3][3]=='T'))
        {
            cout<<"X won"<<endl;
            goto end;
        }
        else if((input[0][0]=='O'||input[0][0]=='T')&&(input[1][1]=='O'||input[1][1]=='T')&&(input[2][2]=='O'||input[2][2]=='T')&&(input[3][3]=='O'||input[3][3]=='T'))
        {
            cout<<"O won"<<endl;
            goto end;
        }
        if((input[0][3]=='X'||input[0][3]=='T')&&(input[1][2]=='X'||input[1][2]=='T')&&(input[2][1]=='X'||input[2][1]=='T')&&(input[3][0]=='X'||input[3][0]=='T'))
        {
            cout<<"X won"<<endl;
            goto end;
        }
        else if((input[0][3]=='O'||input[0][3]=='T')&&(input[1][2]=='O'||input[1][2]=='T')&&(input[2][1]=='O'||input[2][1]=='T')&&(input[3][0]=='O'||input[3][0]=='T'))
        {
            cout<<"O won"<<endl;
            goto end;
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(input[i][j]=='.')
                {
                    cout<<"Game has not completed"<<endl;
                    goto end;
                }
            }
        }
        cout<<"Draw"<<endl;
        end:
        count=count;
    }
    return 0;
}
