#include<iostream>
#include<fstream>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath> 
using namespace std;
int test,l;
char a[8][8];
int solve (int t)
{
    
    int i,j,x=1,o=1;
    
    // vertical
    for (i=0;i<4;i++)
    {
        x=1;
        o=1;
        for (j=0;j<4;j++)
        {
            if (a[i][j]=='O'||a[i][j]=='.')x=0;
            if (a[i][j]=='X'||a[i][j]=='.')o=0;
        }
        //cout<<1<<endl;
        if (x==1)return 1;
        else if (o==1)return 2;
    }
    
    //horizontal
    for (i=0;i<4;i++)
    {
        x=1;
        o=1;
        for (j=0;j<4;j++)
        {
            if (a[j][i]=='O'||a[j][i]=='.')x=0;
            if (a[j][i]=='X'||a[j][i]=='.')o=0;
        }
        //cout<<2<<endl;
        if (x==1)return 1;
        else if (o==1)return 2;
    }
    
    if (a[0][0]!='.'&&a[1][1]!='.'&&a[2][2]!='.'&&a[3][3]!='.')
    {
        //cout<<3<<endl;
        if (a[0][0]!='O'&&a[1][1]!='O'&&a[2][2]!='O'&&a[3][3]!='O')return 1;
        if (a[0][0]!='X'&&a[1][1]!='X'&&a[2][2]!='X'&&a[3][3]!='X')return 2;
    }
    
    if (a[0][3]!='.'&&a[1][2]!='.'&&a[2][1]!='.'&&a[3][0]!='.')
    {
        //cout<<4<<endl;
        if (a[0][4]!='O'&&a[1][3]!='O'&&a[2][1]!='O'&&a[3][0]!='O')return 1;
        if (a[0][4]!='X'&&a[1][3]!='X'&&a[2][1]!='X'&&a[3][0]!='X')return 2;
    }
    
    if (l==1)return 3;
    return 4;
}
int main()
{
    int k=0,i,j;
    cin>>test;
    ofstream fout("test.txt");
    for (k=0;k<test;k++)
    {
        l=0;
        for (i=0;i<4;i++)
        for (j=0;j<4;j++)
        {
            cin>>a[i][j];
            if (a[i][j]=='.')l=1;
        }
        if (solve(k+1)==1)fout<<"Case #"<<k+1<<": X won"<<endl;
        else if (solve(k+1)==2)fout<<"Case #"<<k+1<<": O won"<<endl;
        else if (solve(k+1)==3)fout<<"Case #"<<k+1<<": Game has not completed"<<endl;
        else if (solve(k+1)==4)fout<<"Case #"<<k+1<<": Draw"<<endl;
    }
    return 0;
}