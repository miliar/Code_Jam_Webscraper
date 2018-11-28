/* 
 * File:   main.cpp
 * Author: khairullah
 *
 * Created on April 13, 2013, 12:26 PM
 */

#include <cstdlib>
#include <cstdio>


int incomplete(char a[4][4])
{
    int i,j;
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
            if(a[i][j]=='.')
                return 1;
    }
return 0;    
}

int wins(char a[4][4],char ch)
{
    int i,j,row=0,col=0,d1=0,d2=0;
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
            if(!(a[i][j]=='T'||a[i][j]==ch))
            {
                row++;
                break;
            }
        for(j=0;j<4;++j)
            if(!(a[j][i]=='T'||a[j][i]==ch))
            {
                col++;
                break;
            }
        if(!(a[i][i]=='T'||a[i][i]==ch))
            d1=1;
        if(!(a[i][3-i]=='T'||a[i][3-i]==ch))
            d2=1;
    }
    if(d1==0||d2==0||row<4||col<4)
        return 1;
    return 0;
}

int main(int argc, char** argv) {
    int n;
    char a[4][4],garbage;
    int i,j,k;
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    scanf("%d",&n);
    for(k=1;k<=n;k++)
    {
        scanf("%c",&garbage);
        printf("Case #%d: ",k);
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
            scanf("%c",&a[i][j]);
        scanf("%c",&garbage);
    }
    if(wins(a,'O'))
        printf("O won\n");
    else
    if(wins(a,'X'))
        printf("X won\n");
    else
    if(incomplete(a))
        printf("Game has not completed\n");
    else
        printf("Draw\n");
    }
            return 0;
}

