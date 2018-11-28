#include <iostream>
using namespace std;
#include <fstream>
ifstream fin("A-large.in");
ofstream fout("A_data2.out");
#define cin fin
#define cout fout
int rx[10],cx[10],diag1,diag2;
char board[10][10];
bool Win(char x)
{
    int i,j;
    for(i=1;i<=4;i++)
    {
        rx[i]=0;
        cx[i]=0;
    }
    diag1=0;
    diag2=0;
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            if(board[i][j]==x||board[i][j]=='T')
                rx[i]++;
            if(board[j][i]==x||board[j][i]=='T')
                cx[i]++;
        }
    for(i=1;i<=4;i++)
        if(rx[i]==4||cx[i]==4)
            return true;
    for(i=1;i<=4;i++)
    {
        if(board[i][i]==x||board[i][i]=='T')
            diag1++;
        if(board[i][5-i]==x||board[i][5-i]=='T')
            diag2++;

    }
    if(diag1==4||diag2==4)
        return true;
    return false;


}
int main()
{
    int t,k,i,j;
    cin>>t;
    k=0;
    while(t--)
    {

        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                cin>>board[i][j];
        if(Win('X'))
            cout<<"Case #"<<++k<<": X won"<<endl;
        else if(Win('O'))
            cout<<"Case #"<<++k<<": O won"<<endl;
        else if(!Win('X')&&!Win('O'))
        {
            bool flag=true;
            for(i=1;i<=4;i++)
                for(j=1;j<=4;j++)
                    if(board[i][j]=='.')
                    {
                        flag=false;
                        break;
                    }
            if(flag)
                cout<<"Case #"<<++k<<": Draw"<<endl;
            else
                cout<<"Case #"<<++k<<": Game has not completed"<<endl;
        }


    }
    return 0;
}
