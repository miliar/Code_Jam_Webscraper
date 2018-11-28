#include <cstdio>
#include<algorithm>
#include  <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <climits>
#define  elif else if
using namespace std;
main()
{freopen("A-small-attempt0.in","r",stdin);
freopen("a.ou","w",stdout);
    int t;
    char c[11][11];
    int xc[11],xh[11],yc[11],yh[11];
    bool k,dr;
    int x,y;
    scanf("%d",&t);
for(int l=1;l<=t;l++)    {
    x=0;y=0;
    printf("Case #%d: ",l);
       k=false;
    dr=true;
        for(int i=0;i<=4;i++)
        xc[i]=yc[i]=xh[i]=yh[i]=0;
        for(int i=1;i<=4;i++)
        scanf("%s",c[i]);
        for(int i=1;i<=4;i++)
        for(int j=0;j<4;j++)
        {
            if(c[i][j]=='O')
            {
                yc[j]++;
                yh[i]++;
            }
            elif(c[i][j]=='X')
            {
                xc[j]++;
                xh[i]++;
            }
            elif(c[i][j]=='T')
            {
                yc[j]++;
                yh[i]++;
                 xc[j]++;
                xh[i]++;
            }
            else k=true;
        }
        for(int i=0;i<=4;i++)
        if(xc[i]==4||xh[i]==4)
        {
            dr=false;
            k=false;
            printf("X won");
            break;
        }
        elif(yc[i]==4||yh[i]==4)
        {
            dr=false;
            k=false;
            printf("O won");
            break;
        }
        if(dr)
        {
            if ((c[1][0]==c[2][1]||c[1][0]=='T'||c[2][1]=='T')&&(c[2][1]==c[3][2]||c[3][2]=='T'||c[2][1]=='T')&&(c[3][2]==c[4][3]||c[3][2]=='T'||c[4][3]=='T'))
            {if(c[1][0]=='X'||c[1][0]=='O'||c[1][0]=='T'){
                dr=false;
            k=false;
            if(c[1][0]=='T')
            printf("%c won",c[3][2]);
            else printf("%c won",c[1][0]);}
            }
            elif ((c[1][3]==c[2][2]||c[1][3]=='T'||c[2][2]=='T')&&(c[2][2]==c[3][1]||c[3][1]=='T'||c[2][2]=='T')&&(c[3][1]==c[4][0]||c[3][1]=='T'||c[4][0]=='T'))
            {
                if(c[1][3]=='X'||c[1][3]=='O'||c[1][3]=='T'){
                dr=false;
            k=false;
            if(c[1][3]!='T')
            printf("%c won",c[1][3]);
            else
            printf("%c won",c[2][2]);}
            }
        }
        if(k) printf("Game has not completed");
        else if(dr) printf("Draw");
        printf("\n");

    }
}
