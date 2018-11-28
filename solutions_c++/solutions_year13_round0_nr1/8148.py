#include<cstdio>
#include<iostream>
#include <algorithm>
#include<cmath>

using namespace std;

int main()
{
    int t;
    scanf("%d\n",&t);
    for(int z=0;z<t;z++)
    {
        char a[4][4],ss[256];
        int nx=0,no=0,nt=0,nd=0,flag=0;
        string res;
        for(int i=0;i<4;i++)
        {
                cin.getline(ss,256);
                a[i][0]=ss[0];
                a[i][1]=ss[1];
                a[i][2]=ss[2];
                a[i][3]=ss[3];
        }
        cin.getline(ss,2);
        cout<<"Case #"<<(z+1)<<": ";
        for(int i=0;i<4&&flag==0;i++)
        {
            nx=nt=no=0;
            for(int j=0;j<4;j++)
            {
                    if(a[i][j]=='X') nx++;
                    else if(a[i][j]=='O') no++;
                    else if(a[i][j]=='T') nt++;
                    else if(a[i][j]=='.') nd++;
            }
            if(nx+nt==4)
            {
                cout<<"X won"<<endl;
                flag=1;
            }
            else if(no+nt==4)
            {
                cout<<"O won"<<endl;
                flag=1;
            }
        }
        nx=nt=no=0;
        for(int j=0;j<4&&flag==0;j++)
        {
              nx=nt=no=0;
            for(int i=0;i<4;i++)
            {
                    if(a[i][j]=='X') nx++;
                    else if(a[i][j]=='O') no++;
                    else if(a[i][j]=='T') nt++;
                    else if(a[i][j]=='.') nd++;
            }
            if(nx+nt==4)
            {
                cout<<"X won"<<endl;
                flag=1;
            }
            else if(no+nt==4)
            {
                cout<<"O won"<<endl;
                flag=1;
            }
        }

        nx=nt=no=0;
        for(int i=0;i<4&&flag==0;i++)
        {
                    if(a[i][i]=='X') nx++;
                    else if(a[i][i]=='O') no++;
                    else if(a[i][i]=='T') nt++;
                    else if(a[i][i]=='.') nd++;
        }
        if(nx+nt==4)
        {
                cout<<"X won"<<endl;
                flag=1;
        }
        else if(no+nt==4)
        {
                cout<<"O won"<<endl;
                flag=1;
        }
        if(flag==0){
        nx=nt=no=0;
        if(a[0][3]=='X') nx++;
        else if(a[0][3]=='O') no++;
        else if(a[0][3]=='T') nt++;
        else if(a[0][3]=='.') nd++;

        if(a[1][2]=='X') nx++;
        else if(a[1][2]=='O') no++;
        else if(a[1][2]=='T') nt++;
        else if(a[1][2]=='.') nd++;

        if(a[2][1]=='X') nx++;
        else if(a[2][1]=='O') no++;
        else if(a[2][1]=='T') nt++;
        else if(a[2][1]=='.') nd++;

        if(a[3][3]=='X') nx++;
        else if(a[3][0]=='O') no++;
        else if(a[3][0]=='T') nt++;
        else if(a[3][0]=='.') nd++;

        if(nx+nt==4)
        {
                cout<<"X won"<<endl;
                flag=1;
        }
        else if(no+nt==4)
        {
                cout<<"O won"<<endl;
                flag=1;
        }
        }
        if(flag==0)
        {
            if(nd==0)
                cout<<"Draw"<<endl;
            else
                cout<<"Game has not completed"<<endl;
        }
     }
    return 0;
}

