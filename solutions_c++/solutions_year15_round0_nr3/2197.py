#include <iostream>
#include <cstdio>
using namespace std;

//i - 2 j - 3 k - 4
int tab[5][5]={
                {0, 0, 0, 0, 0},
                {0, 1, 2, 3, 4},
                {0, 2, -1, 4, -3},
                {0, 3, -4, -1, 2},
                {0, 4, 3, -2, -1}
                };
char tab2[10001];
int t, x, l, a, wyn, licz;

int main()
{
    scanf("%d", &t);
    while(t--)
    {
        a++;
        licz=0;
        wyn=1;
        scanf("%d%d %s", &l, &x, tab2+1);
        for(int i=0;i<x;i++)
        {
            for(int j=1;j<=l;j++)
            {
                int y=tab2[j]-'g';
                if(wyn>0)
                    wyn=tab[wyn][y];
                else
                    wyn=(-1)*tab[wyn*(-1)][y];
                if(licz==0&&wyn==2)
                    licz++, wyn=1;
                if(licz==1&&wyn==3)
                    licz++, wyn=1;
                if(licz==2&&wyn==4)
                    licz++, wyn=1;
            }
        }
        printf("Case #%d: ", a);
        printf(wyn==1&&licz==3 ? "YES\n" : "NO\n");
    };
    return 0;
}


