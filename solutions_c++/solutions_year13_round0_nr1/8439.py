#include<stdio.h>
#include<iostream>
#include<fstream>

using namespace std;

int won(char a[4][4],char ch)
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[i][j]==ch||a[i][j]=='T')
            {
                if(j==3)
                return 1;
            }
            else
            break;
        }
    }
     for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(a[j][i]==ch||a[j][i]=='T')
            {
                if(j==3)
                return 1;
            }
            else
            break;
        }
    }
    for(i=0;i<4;i++)
    {
        if(a[i][i]==ch||a[i][i]=='T')
            {
                if(i==3)
                return 1;
            }
            else
            break;
    }
    for(i=0;i<4;i++)
    {
        if(a[i][3-i]==ch||a[i][3-i]=='T')
            {
                if(i==3)
                return 1;
            }
            else
            break;
    }
    return 0;

}


int main()
{
    int test;
  //  ifstream in;
    //in.open("2.txt",ios::in);
 //   ofstream out;
   // out.open("ee.txt",ios::out);
    cin>>test;
    int x;
    for(x=1;x<=test;x++)
    {
        int i,j;

        char a[4][4]={0};
        int left=0;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            cin>>a[i][j];
            if(a[i][j]=='.')
            left=1;
        }
        cout<<"Case #"<<x<<": ";
        if(won(a,'X')==1)
        {
                cout<<"X won"<<endl;
        }
        else if(won(a,'O')==1)
        {
            cout<<"O won"<<endl;
        }
        else if(left==1)
        {
            cout<<"Game has not completed"<<endl;
        }
        else
        {
            cout<<"Draw"<<endl;
        }

    }

}
