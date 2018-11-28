#include <iostream>
#include <stdio.h>
using namespace std;
string str[1000];
int cAse =1;
bool checkRow(char ch)
{
    int i,j,cnt;
    for(i=0;i<4;i++)
    {
        cnt=0;
        for(j=0;j<4;j++)
        {
            if(ch==str[i][j]||str[i][j]=='T')cnt++;
        }
        //cout<<cnt<<endl;
        if(cnt ==4) return true;
    }

    return  false;
}
bool checkCol(char ch)
{
    int i,j,cnt;
    for(i=0;i<4;i++)
    {
        cnt=0;
        for(j=0;j<4;j++)
        {
            if(ch==str[j][i]||str[j][i]=='T')cnt++;
        }
        if(cnt ==4) return true;
    }

    return  false;
}
bool diagonal(char ch)
{
    int i,j,cnt;
    cnt=0;
    for(i=0;i<4;i++)
    {

        if(ch==str[i][i]||str[i][i]=='T')cnt++;

    }
    if(cnt ==4) return true;
    return  false;
}
bool antidiagonal(char ch)
{
    int i,j,cnt;
    j= 0;
    cnt =0;
    for(i=3;i>=0;i--,j++)
    {
        if(ch ==str[j][i] || str[j][i]=='T') cnt++;



    }
    if(cnt == 4 ) return true;
    return  false;
}
int main()
{
    int n,i,j;
    freopen ("A-large.in","r",stdin);
    freopen ("b.txt","w",stdout);
    while(cin>>n)
    {
      while(n--)
      {
            for(i=0;i<4;i++)
            {
                cin>>str[i];
            }
            int cntchar = 16;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(str[i][j]=='.')cntchar--;
                }
            }
            //cout<<"cnt"<<cntchar<<endl;
            bool chkR = false;
            int xwon = 0;
            int owon = 0;
            chkR = checkRow('X');
            if(chkR == true) xwon = 1;
            chkR = checkCol('X');
            if(chkR == true) xwon = 1;
            chkR = diagonal('X');
            if(chkR == true) xwon = 1;
            chkR = antidiagonal('X');
            if(chkR == true) xwon = 1;

            chkR = checkRow('O');
            if(chkR == true) owon = 1;
            chkR = checkCol('O');
            if(chkR == true) owon = 1;
            chkR = diagonal('O');
            if(chkR == true) owon = 1;
            chkR = antidiagonal('O');
            if(chkR == true) owon = 1;

            cout<<"Case #"<<cAse++<<": ";
            if(xwon == 1 ) cout<<"X won"<<endl;
            else if(owon == 1) cout<<"O won"<<endl;
            else
            {
                if(cntchar == 16)
                    cout <<"Draw"<<endl;
                else
                    cout<< "Game has not completed"<<endl;
            }

        }


    }
    return 0;
}
