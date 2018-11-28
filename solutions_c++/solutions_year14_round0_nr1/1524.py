#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define MAX 28

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int t;
    int r;
    int resp[2][4];

    int carta, carta_escolhida;
    int possib;

    scanf("%d", &t);
    for(int ncaso=1; ncaso<=t; ncaso++)
    {
        scanf("%d", &r);

        for(int i=1; i<=4; i++)
        {
            if (i != r)
            {
                for(int j=0; j<4; j++)
                    scanf("%d", &resp[0][j]);
            }
            else
            {
                for(int j=0; j<4; j++)
                    scanf("%d", &resp[1][j]);
            }
        }

        possib = 0;
        scanf("%d", &r);
        for(int i=1; i<=4; i++)
        {
            if (i != r)
            {
                for(int j=0; j<4; j++)
                    scanf("%d", &resp[0][j]);
            }
            else
            {
                for(int j=0; j<4; j++)
                {
                    scanf("%d", &carta);

                    if (carta==resp[1][0] || carta==resp[1][1] || carta==resp[1][2] || carta==resp[1][3])
                    {
                        carta_escolhida = carta;
                        possib++;
                    }
                }
            }
        }
        if (possib == 0) printf("Case #%d: Volunteer cheated!\n", ncaso);
        else if (possib == 1) printf("Case #%d: %d\n", ncaso, carta_escolhida);
        else printf("Case #%d: Bad magician!\n", ncaso);
    }

    return 0;
}
