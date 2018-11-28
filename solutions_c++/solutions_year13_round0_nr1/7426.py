#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N,th=0;
    cin>>N;
    while(N--)
    {
        th++;
        char c[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>c[i][j];
            }
        }
        int bj=0;
        for(int i=0;i<4;i++)
        {
            if(c[i][0]=='X' && c[i][1]=='X' && c[i][2]=='X' && c[i][3]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[i][0]=='T' && c[i][1]=='X' && c[i][2]=='X' && c[i][3]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[i][0]=='X' && c[i][1]=='T' && c[i][2]=='X' && c[i][3]=='X')
            {
               // cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }if(c[i][0]=='X' && c[i][1]=='X' && c[i][2]=='T' && c[i][3]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }if(c[i][0]=='X' && c[i][1]=='X' && c[i][2]=='X' && c[i][3]=='T')
            {
               // cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }

            if(c[i][0]=='O' && c[i][1]=='O' && c[i][2]=='O' && c[i][3]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[i][0]=='T' && c[i][1]=='O' && c[i][2]=='O' && c[i][3]=='O')
            {
               // cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[i][0]=='O' && c[i][1]=='T' && c[i][2]=='O' && c[i][3]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[i][0]=='O' && c[i][1]=='O' && c[i][2]=='T' && c[i][3]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[i][0]=='O' && c[i][1]=='O' && c[i][2]=='O' && c[i][3]=='T')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }

        }
        for(int i=0;i<4;i++)
        {
            if(c[0][i]=='X' && c[1][i]=='X' && c[2][i]=='X' && c[3][i]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[0][i]=='T' && c[1][i]=='X' && c[2][i]=='X' && c[3][i]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[0][i]=='X' && c[1][i]=='T' && c[2][i]=='X' && c[3][i]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[0][i]=='X' && c[1][i]=='X' && c[2][i]=='T' && c[3][i]=='X')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }
            if(c[0][i]=='X' && c[1][i]=='X' && c[2][i]=='X' && c[3][i]=='T')
            {
                //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
                bj=1;
                break;
            }

            if(c[0][i]=='O' && c[1][i]=='O' && c[2][i]=='O' && c[3][i]=='O')
            {
               // cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[0][i]=='T' && c[1][i]=='O' && c[2][i]=='O' && c[3][i]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[0][i]=='O' && c[1][i]=='T' && c[2][i]=='O' && c[3][i]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[0][i]=='O' && c[1][i]=='O' && c[2][i]=='T' && c[3][i]=='O')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }
            if(c[0][i]=='O' && c[1][i]=='O' && c[2][i]=='O' && c[3][i]=='T')
            {
                //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
                bj=2;
                break;
            }

        }
        if(c[0][0]=='X' && c[1][1]=='X' && c[2][2]=='X' && c[3][3]=='X')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][0]=='T' && c[1][1]=='X' && c[2][2]=='X' && c[3][3]=='X')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][0]=='X' && c[1][1]=='T' && c[2][2]=='X' && c[3][3]=='X')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][0]=='X' && c[1][1]=='X' && c[2][2]=='T' && c[3][3]=='X')
        {
           // cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][0]=='X' && c[1][1]=='X' && c[2][2]=='X' && c[3][3]=='T')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }

        if(c[0][0]=='O' && c[1][1]=='O' && c[2][2]=='O' && c[3][3]=='O')
        {
           // cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][0]=='T' && c[1][1]=='O' && c[2][2]=='O' && c[3][3]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][0]=='O' && c[1][1]=='T' && c[2][2]=='O' && c[3][3]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" win"<<endl;
            bj=2;
        }
        if(c[0][0]=='O' && c[1][1]=='O' && c[2][2]=='T' && c[3][3]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][0]=='O' && c[1][1]=='O' && c[2][2]=='O' && c[3][3]=='T')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }

        if(c[0][3]=='X' && c[1][2]=='X' && c[2][1]=='X' && c[3][0]=='X')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][3]=='T' && c[1][2]=='X' && c[2][1]=='X' && c[3][0]=='X')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][3]=='X' && c[1][2]=='T' && c[2][1]=='X' && c[3][0]=='X')
        {
           // cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][3]=='X' && c[1][2]=='X' && c[2][1]=='T' && c[3][0]=='X')
        {
           // cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }
        if(c[0][3]=='X' && c[1][2]=='X' && c[2][1]=='X' && c[3][0]=='T')
        {
            //cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
            bj=1;
        }

        if(c[0][3]=='O' && c[1][2]=='O' && c[2][1]=='O' && c[3][0]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][3]=='T' && c[1][2]=='O' && c[2][1]=='O' && c[3][0]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][3]=='O' && c[1][2]=='T' && c[2][1]=='O' && c[3][0]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][3]=='O' && c[1][2]=='O' && c[2][1]=='T' && c[3][0]=='O')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }
        if(c[0][3]=='O' && c[1][2]=='O' && c[2][1]=='O' && c[3][0]=='T')
        {
            //cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
            bj=2;
        }

        if(bj==0)
        {
            for(int i=0;i<4;i++)
            {
                if(bj==2)
                    break;
                for(int j=0;j<4;j++)
                {
                    if(c[i][j]=='.')
                    {
                        bj=3;
                        //cout<<"Case #"<<th<<": Game has not completed"<<endl;
                        break;
                    }
                }
            }
        }
        if(bj==0)
        {
            cout<<"Case #"<<th<<": Draw"<<endl;
        }
        if(bj==1)
        {
            cout<<"Case #"<<th<<": "<<'X'<<" won"<<endl;
        }
        if(bj==2)
        {
            cout<<"Case #"<<th<<": "<<'O'<<" won"<<endl;
        }
        if(bj==3)
        {
            cout<<"Case #"<<th<<": Game has not completed"<<endl;
        }
    }
}
