#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int b[5][5];
int T;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    getchar();
    int cas;
    for(cas = 1;cas <= T;++cas)
    {
    memset(b,-1,sizeof(b));
    char c;
    int numx,numo,numt,numdot;
    numdot = 0;
    for(int i = 1;i <= 4;++i)
    {
        for(int j = 1;j <= 4;++j)
        {
            scanf("%c",&c);
            if(c == 'X')b[i][j] = 1;
            else if(c == 'O')b[i][j] = 2;
            else if(c == 'T')b[i][j] = 3;
            else if(c == '.'){b[i][j] = 0;numdot++;}
        }
        getchar();
    }
    getchar();
    //printf("dot num = %d\n",numdot);
    int mkx = 0,mko = 0;
    numx = 0,numo = 0,numt = 0;
    for(int i = 1;i <= 4;++i)
    {
        numx = 0,numo = 0,numt = 0;
        for(int j = 1;j <= 4;++j)
        {
            if(b[i][j] == 1)numx++;
            else if(b[i][j] == 2)numo++;
            else if(b[i][j] == 3)numt++;
        }
        if(numx == 4 ||(numx == 3 && numt == 1)){mkx = 1;break;}
        if(numo == 4 ||(numo == 3 && numt == 1)){mko = 1;break;}
    }
    for(int j = 1;j <= 4;++j)
    {
        numx = 0,numo = 0,numt = 0;
        for(int i = 1;i <= 4;++i)
        {
            if(b[i][j] == 1)numx++;
            else if(b[i][j] == 2)numo++;
            else if(b[i][j] == 3)numt++;
        }
        if(numx == 4 ||(numx == 3 && numt == 1)){mkx = 1;break;}
        if(numo == 4 ||(numo == 3 && numt == 1)){mko = 1;break;}
    }
    numx = 0,numo = 0,numt = 0;
    for(int i = 1;i <= 4;++i)
    {
        if(b[i][i] == 1)numx++;
        else if(b[i][i] == 2)numo++;
        else if(b[i][i] == 3)numt++;
        if(numx == 4 ||(numx == 3 && numt == 1)){mkx = 1;break;}
        if(numo == 4 ||(numo == 3 && numt == 1)){mko = 1;break;}
    }
    numx = 0,numo = 0,numt = 0;
    for(int i = 1;i <= 4;++i)
    {
        if(b[i][5 - i] == 1)numx++;
        else if(b[i][5 - i] == 2)numo++;
        else if(b[i][5 - i] == 3)numt++;
        if(numx == 4 ||(numx == 3 && numt == 1)){mkx = 1;break;}
        if(numo == 4 ||(numo == 3 && numt == 1)){mko = 1;break;}
    }
    /*
    for(int i = 1;i <= 4;++i)
    {
        for(int j = 1;j <= 4;++j)
        {
            printf("%d",b[i][j]);
        }
        printf("\n");
    }
    printf("\n");*/
    printf("Case #%d: ",cas);
    if(mkx)printf("X won\n");
    else if(mko)printf("O won\n");
    else if(mkx == 0 && mko == 0 && numdot == 0)printf("Draw\n");
    else printf("Game has not completed\n");

    }
    return 0;
}
/*
6
XXXT
....
OO..
....
XOXT
XXOO
OXOX
XXOO
XOX.
OX..
....
....
OOXX
OXXX
OX.T
O..O
XXXO
..O.
.O..
T...
OXXX
XO..
..O.
...O
*/
