#include <iostream>
#include<fstream>
#include<math.h>
#include<memory.h>
#include<stdlib.h>
#include<time.h>
#include<algorithm>

using namespace std;

const char fi[]="vd.in";
const char fo[]="vd.out";

char a[5][5];int hangx[5],cotx[5],hango[5],coto[5];

void nhap()
{
    int i,j;
    memset(hangx,0,sizeof(hangx));
    memset(hango,0,sizeof(hango));
    memset(cotx,0,sizeof(cotx));
    memset(coto,0,sizeof(coto));
    for(i=1;i<=4;++i)
    {
        for(j=1;j<=4;++j)
        {
            cin>>a[i][j];
            if (a[i][j]=='X')
            {
                hangx[i]++;cotx[j]++;
            }
            else
            {
                if (a[i][j]=='O')
                {
                    hango[i]++;coto[j]++;
                }
                else
                {
                    if (a[i][j]=='T')
                    {
                        hangx[i]++;cotx[j]++;hango[i]++;coto[j]++;
                    }
                }
            }
        }
    }
}

bool dakt()
{
    int i,j;
    for(i=1;i<=4;++i)
    {
        for(j=1;j<=4;++j) if (a[i][j]=='.') return(0);
    }
    return(1);
}

void xuli(int t)
{
    int i;
    for(i=1;i<=4;++i)
    {
        if (hangx[i]==4 || cotx[i]==4)
        {
            printf("Case #%d: X won\n",t);return;
        }
        if (hango[i]==4 || coto[i]==4)
        {
            printf("Case #%d: O won\n",t);return;
        }
    }
    int j=0;
    for(i=1;i<=4;++i) if (a[i][i]=='X' || a[i][i]=='T') ++j;
    if (j==4)
    {
        printf("Case #%d: X won\n",t);return;
    }
    j=0;
    for(i=1;i<=4;++i) if (a[i][i]=='O' || a[i][i]=='T') ++j;
    if (j==4)
    {
        printf("Case #%d: O won\n",t);return;
    }
    j=0;
    for(i=1;i<=4;++i) if (a[i][5-i]=='O' || a[i][5-i]=='T') ++j;
    if (j==4)
    {
        printf("Case #%d: O won\n",t);return;
    }
    j=0;
    for(i=1;i<=4;++i) if (a[i][5-i]=='X' || a[i][5-i]=='T') ++j;
    if (j==4)
    {
        printf("Case #%d: X won\n",t);return;
    }
    if (dakt())
    {
        printf("Case #%d: Draw\n",t);return;
    }
    printf("Case #%d: Game has not completed\n",t);
}

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        nhap();xuli(i);
    }
}
