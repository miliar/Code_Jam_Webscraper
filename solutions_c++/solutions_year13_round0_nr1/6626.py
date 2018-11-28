#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
char m[10][10];
int W;
void row()
{
    int ca=0,cb=0;
    for(int i=0; i<4; i++)
    {
        ca=0,cb=0;
        for(int j=0; j<4; j++)
        {
            if(m[i][j]=='T'||m[i][j]=='O')
                ca++;
            if(m[i][j]=='T'||m[i][j]=='X')
                cb++;
        }
        if(ca==4)
            W=1;
        if(cb==4)
            W=-1;
    }
}
void colom()
{

    int ca=0,cb=0;
    for(int i=0; i<4; i++)
    {
        ca=0,cb=0;
        for(int j=0; j<4; j++)
        {
            if(m[j][i]=='T'||m[j][i]=='O')
                ca++;
            if(m[j][i]=='T'||m[j][i]=='X')
                cb++;
        }
        if(ca==4)
            W=1;
        if(cb==4)
            W=-1;
    }
}
void dragon()
{
    int ca=0,cb=0;
    for(int i=0; i<4; i++)
    {
        if(m[i][i]=='T'||m[i][i]=='O')
            ca++;
        if(m[i][i]=='T'||m[i][i]=='X')
            cb++;
    }

    if(ca==4)
        W=1;
    if(cb==4)
        W=-1;
    ca=0,cb=0;
    for(int i=0; i<4; i++)
    {
        if(m[i][3-i]=='T'||m[i][3-i]=='O')
            ca++;
        if(m[i][3-i]=='T'||m[i][3-i]=='X')
            cb++;
    }
    if(ca==4)
        W=1;
    if(cb==4)
        W=-1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int C=1; C<=cas; C++)
    {
        W=0;
        int uncovered=0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf(" %c",&m[i][j]);
                if(m[i][j]=='.')
                    uncovered++;
            }
        }
        printf("Case #%d: ",C);
        row();
        colom();
        dragon();
        if(W==1)
            printf("O won\n");
        if(W==-1)
            printf("X won\n");
        if(W==0)
        {
            if(uncovered>0)
                printf("Game has not completed\n");
            else printf("Draw\n");
            }
    }
    return 0;
}
