#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("tictactoe.txt","r",stdin);
    freopen("output.txt","w+",stdout);

    int tc,i,j,flag,count,cases;
    char board[4][4],ch;
    cin>>tc;

    for(cases=1; cases<=tc;cases++)
    {
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>board[i][j];

        //rows check...
        flag=0;
        for(i=0;i<4;i++)
        {
            count=0;
            for(j=0;j<3;j++)
            {
                if((board[i][j]==board[i][j+1] && board[i][j]!='.') || board[i][j]=='T' || board[i][j+1]=='T')
                {
                    count++;
                }
            }

            if(count==3)
            {
                flag=1;
                if(board[i][0]!='T')
                    cout<<"Case #"<<cases<<": "<<board[i][0]<<" won\n";

                else
                    cout<<"Case #"<<cases<<": "<<board[i][1]<<" won\n";
            }

            if(flag==1)
                break;
        }

        if(flag==1)
            continue;

        //cols check...
        flag=0;
        for(j=0;j<4;j++)
        {
            count=0;
            for(i=0;i<3;i++)
            {
                if((board[i][j]==board[i+1][j] && board[i][j]!='.') || board[i][j]=='T' || board[i+1][j]=='T')
                {
                    count++;
                }
            }

            if(count==3)
            {
                flag=1;
                if(board[0][j]!='T')
                    cout<<"Case #"<<cases<<": "<<board[0][j]<<" won\n";

                else
                    cout<<"Case #"<<cases<<": "<<board[1][j]<<" won\n";
            }

            if(flag==1)
                break;
        }
        if(flag==1)
            continue;

        //diag check...
        count=0;
        flag=0;
        for(i=0,j=0;i<3;i++,j++)
        {
            if((board[i][j]==board[i+1][j+1] && board[i][j]!='.') || board[i][j]=='T' || board[i+1][j+1]=='T')
            {
                count++;
            }
        }

        if(count==3)
        {
            flag=1;
            if(board[0][0]!='T')
                cout<<"Case #"<<cases<<": "<<board[0][0]<<" won\n";

            else
                cout<<"Case #"<<cases<<": "<<board[1][1]<<" won\n";
        }
        if(flag==1)
            continue;

        //diag check...
        count=0;
        flag=0;
        for(i=3,j=0;j<3;i--,j++)
        {
            if((board[i][j]==board[i-1][j+1] && board[i][j]!='.') || board[i][j]=='T' || board[i-1][j+1]=='T')
            {
                count++;
            }
        }

        if(count==3)
        {
            flag=1;
            if(board[3][0]!='T')
                cout<<"Case #"<<cases<<": "<<board[3][0]<<" won\n";

            else
                cout<<"Case #"<<cases<<": "<<board[2][1]<<" won\n";
        }
        if(flag==1)
            continue;

        flag=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(board[i][j]=='.')
                {
                    flag=1;
                    break;
                }
            }
            if(flag==1)
                break;
        }

        if(flag==1)
            cout<<"Case #"<<cases<<": "<<"Game has not completed\n";

        else
            cout<<"Case #"<<cases<<": "<<"Draw\n";

    }
    return 0;
}
