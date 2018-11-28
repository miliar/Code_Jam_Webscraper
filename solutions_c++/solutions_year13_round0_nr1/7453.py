#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
char m[4][4];
int jk()
{
    for(int i=0; i<4; i++)
    {
        if((m[i][0]=='X'||m[i][0]=='T')&&(m[i][1]=='X'||m[i][1]=='T')&&(m[i][2]=='X'||m[i][2]=='T')&&(m[i][3]=='X'||m[i][3]=='T'))
            return 1;
        if((m[i][0]=='O'||m[i][0]=='T')&&(m[i][1]=='O'||m[i][1]=='T')&&(m[i][2]=='O'||m[i][2]=='T')&&(m[i][3]=='O'||m[i][3]=='T'))
            return 2;
        if((m[0][i]=='X'||m[0][i]=='T')&&(m[1][i]=='X'||m[1][i]=='T')&&(m[2][i]=='X'||m[2][i]=='T')&&(m[3][i]=='X'||m[3][i]=='T'))
            return 1;
        if((m[0][i]=='O'||m[0][i]=='T')&&(m[1][i]=='O'||m[1][i]=='T')&&(m[2][i]=='O'||m[2][i]=='T')&&(m[3][i]=='O'||m[3][i]=='T'))
            return 2;
    }
    if((m[0][0]=='X'||m[0][0]=='T')&&(m[1][1]=='X'||m[1][1]=='T')&&(m[2][2]=='X'||m[2][2]=='T')&&(m[3][3]=='X'||m[3][3]=='T'))
        return 1;
    if((m[0][0]=='O'||m[0][0]=='T')&&(m[1][1]=='O'||m[1][1]=='T')&&(m[2][2]=='O'||m[2][2]=='T')&&(m[3][3]=='O'||m[3][3]=='T'))
        return 2;
    if((m[0][3]=='X'||m[0][3]=='T')&&(m[1][2]=='X'||m[1][2]=='T')&&(m[2][1]=='X'||m[2][1]=='T')&&(m[3][0]=='X'||m[3][0]=='T'))
        return 1;
    if((m[0][3]=='O'||m[0][3]=='T')&&(m[1][2]=='O'||m[1][2]=='T')&&(m[2][1]=='O'||m[2][1]=='T')&&(m[3][0]=='O'||m[3][0]=='T'))
        return 2;
    for(int i=0; i<4; i++)
    for(int j=0; j<4; j++)
        if(m[i][j]=='.')
            return 3;
    return 4;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,i,j,k=1;
    string s;
    cin>>t;
    while(t--)
    {
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
                cin>>m[i][j];
        }
        int ans=jk();
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
            {
                if(ans==1)
                    s="X won";
                else if(ans==2)
                    s="O won";
                else if(ans==3)
                    s="Game has not completed";
                else if(ans==4)
                    s="Draw";
            }
        printf("Case #%d: ",k++);
        cout<<s<<endl;
    }
    return 0;
}
