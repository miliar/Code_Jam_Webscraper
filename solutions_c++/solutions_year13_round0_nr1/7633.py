# include <iostream>
# include <conio.h>
# include <fstream>
using namespace std;
ifstream fr ("input.txt");
ofstream fw ("output.txt");
int solve()
{   char arr[4][4],temp[4][4],ch;
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
            fr>>arr[i][j];

    for (int i=0;i<4;i++)
    {   for (int j=0;j<4;j++)
        {   ch=arr[i][j];
            if(ch=='T')
                ch='X';
            temp[i][j]=ch;
        }
    }
    cout <<temp[0][0]<<" "<<temp[0][1]<<" "<<temp[0][2]<<" "<<temp[0][3]<<endl;
    cout <<temp[1][0]<<" "<<temp[1][1]<<" "<<temp[1][2]<<" "<<temp[1][3]<<endl;
    cout <<temp[2][0]<<" "<<temp[2][1]<<" "<<temp[2][2]<<" "<<temp[2][3]<<endl;
    cout <<temp[3][0]<<" "<<temp[3][1]<<" "<<temp[3][2]<<" "<<temp[3][3]<<endl;

    if((temp[0][0]==temp[0][1])&&(temp[0][0]==temp[0][2])&&(temp[0][0]==temp[0][3])&&(temp[0][0]=='X'))
        return 1;
    if((temp[1][0]==temp[1][1])&&(temp[1][0]==temp[1][2])&&(temp[1][0]==temp[0][3])&&(temp[1][0]=='X'))
        return 1;
    if((temp[2][0]==temp[2][1])&&(temp[2][0]==temp[2][2])&&(temp[2][0]==temp[2][3])&&(temp[2][0]=='X'))
        return 1;
    if((temp[3][0]==temp[3][1])&&(temp[3][0]==temp[3][2])&&(temp[3][0]==temp[3][3])&&(temp[3][0]=='X'))
        return 1;
    if((temp[0][0]==temp[1][0])&&(temp[0][0]==temp[2][0])&&(temp[0][0]==temp[3][0])&&(temp[0][0]=='X'))
        return 1;
    if((temp[0][1]==temp[1][1])&&(temp[0][1]==temp[2][1])&&(temp[0][1]==temp[3][1])&&(temp[0][1]=='X'))
        return 1;
    if((temp[0][2]==temp[1][2])&&(temp[0][2]==temp[2][2])&&(temp[0][0]==temp[3][2])&&(temp[0][2]=='X'))
        return 1;
    if((temp[0][3]==temp[1][3])&&(temp[0][3]==temp[2][3])&&(temp[0][3]==temp[3][3])&&(temp[0][3]=='X'))
        return 1;
    if((temp[0][0]==temp[1][1])&&(temp[0][0]==temp[2][2])&&(temp[0][0]==temp[3][3])&&(temp[0][0]=='X'))
        return 1;
    if((temp[0][3]==temp[1][2])&&(temp[0][3]==temp[2][1])&&(temp[0][3]==temp[3][0])&&(temp[0][3]=='X'))
        return 1;

    for (int i=0;i<4;i++)
    {   for (int j=0;j<4;j++)
        {   ch=arr[i][j];
            if(ch=='T')
                ch='O';
            temp[i][j]=ch;
        }
    }
    if((temp[0][0]==temp[0][1])&&(temp[0][0]==temp[0][2])&&(temp[0][0]==temp[0][3])&&(temp[0][0]=='O'))
        return 2;
    if((temp[1][0]==temp[1][1])&&(temp[1][0]==temp[1][2])&&(temp[1][0]==temp[0][3])&&(temp[1][0]=='O'))
        return 2;
    if((temp[2][0]==temp[2][1])&&(temp[2][0]==temp[2][2])&&(temp[2][0]==temp[2][3])&&(temp[2][0]=='O'))
        return 2;
    if((temp[3][0]==temp[3][1])&&(temp[3][0]==temp[3][2])&&(temp[3][0]==temp[3][3])&&(temp[3][0]=='O'))
        return 2;
    if((temp[0][0]==temp[1][0])&&(temp[0][0]==temp[2][0])&&(temp[0][0]==temp[3][0])&&(temp[0][0]=='O'))
        return 2;
    if((temp[0][1]==temp[1][1])&&(temp[0][1]==temp[2][1])&&(temp[0][1]==temp[3][1])&&(temp[0][1]=='O'))
        return 2;
    if((temp[0][2]==temp[1][2])&&(temp[0][2]==temp[2][2])&&(temp[0][0]==temp[3][2])&&(temp[0][2]=='O'))
        return 2;
    if((temp[0][3]==temp[1][3])&&(temp[0][3]==temp[2][3])&&(temp[0][3]==temp[3][3])&&(temp[0][3]=='O'))
        return 2;
    if((temp[0][0]==temp[1][1])&&(temp[0][0]==temp[2][2])&&(temp[0][0]==temp[3][3])&&(temp[0][0]=='O'))
        return 2;
    if((temp[0][3]==temp[1][2])&&(temp[0][3]==temp[2][1])&&(temp[0][3]==temp[3][0])&&(temp[0][3]=='O'))
        return 2;

    for (int i=0;i<4;i++)
    {    for (int j=0;j<4;j++)
        {    if(arr[i][j]=='.')
                return  3;
        }
    }

   return 0;
    getch();
}


int main()
{   int t,sol;
    fr>>t;
    for (int i=0;i<t;i++)
    {   sol=solve();
        cout <<sol;
        if(sol==0)
            fw<<"Case #"<<i+1<<": "<<"Draw"<<endl;
        if(sol==1)
            fw<<"Case #"<<i+1<<": "<<"X won"<<endl;
        if(sol==2)
            fw<<"Case #"<<i+1<<": "<<"O won"<<endl;
        if(sol==3)
            fw<<"Case #"<<i+1<<": "<<"Game has not completed"<<endl;
    }
    getch();
}
















