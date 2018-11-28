#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
ifstream cin("/Users/yangsiyu/Documents/HelloWorld/HelloWorld/in.txt");
ofstream cout("/Users/yangsiyu/Documents/HelloWorld/HelloWorld/out.txt");

char a[10][10];

void work()
{
    int i,j;
    bool flag;
    //row
    for (i=1;i<=4;i++)
    {
        for (j=0;j<=3;j++)
            if (a[i][j]!='X'&&a[i][j]!='T') break;
        if (j==4)
        {
            //printf("X won");
            cout<<"X won";
            return;
        }
    }
    for (i=1;i<=4;i++)
    {
        for (j=0;j<=3;j++)
            if (a[i][j]!='O'&&a[i][j]!='T') break;
        if (j==4)
        {
            //printf("O won");
            cout<<"O won";
            return;
        }
    }
    //clu
    for (j=0;j<=3;j++)
    {
        for (i=1;i<=4;i++)
            if (a[i][j]!='X'&&a[i][j]!='T') break;
        if (i==5)
        {
            //printf("X won");
            cout<<"X won";
            return;
        }
    }
    for (j=0;j<=3;j++)
    {
        for (i=1;i<=4;i++)
            if (a[i][j]!='O'&&a[i][j]!='T') break;
        if (i==5)
        {
            //printf("O won");
            cout<<"O won";
            return;
        }
    }
    //de
    for (i=0;i<=3;i++)
        if (a[i+1][i]!='X'&&a[i+1][i]!='T') break;
    if (i==4)
    {
        //printf("X won");
        cout<<"X won";
        return;
    }
    for (i=0;i<=3;i++)
        if (a[i+1][i]!='O'&&a[i+1][i]!='T') break;
    if (i==4)
    {
        //printf("O won");
        cout<<"O won";
        return;
    }
    for (i=0;i<=3;i++)
        if (a[i+1][3-i]!='X'&&a[i+1][3-i]!='T') break;
    if (i==4)
    {
        //printf("X won");
        cout<<"X won";
        return;
    }
    for (i=0;i<=3;i++)
        if (a[i+1][3-i]!='O'&&a[i+1][3-i]!='T') break;
    if (i==4)
    {
        //printf("O won");
        cout<<"O won";
        return;
    }
    //draw
    flag=false;
    for (i=1;i<=4;i++)
        for (j=0;j<=3;j++)
            if (a[i][j]=='.') flag=true;
    if (flag)
    {
        //printf("Game has not completed");
        cout<<"Game has not completed";
        return;
    }
    else
    {
        //printf("Draw");
        cout<<"Draw";
        return;
    }
}

int main()
{
    int t,i,count=0;
    //scanf("%d",&t);
    cin>>t;
    while (t--)
    {
        count++;
        for (i=1;i<=4;i++)
            //scanf("%s",a[i]);
            cin>>a[i];
        //printf("Case #%d: ",count);
        cout<<"Case #"<<count<<": ";
        work();
        //printf("\n");
        cout<<endl;
    }
    return 0;
}