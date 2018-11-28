#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <deque>
#include <iostream>
#include <math.h>
#include <sstream>
#include <assert.h>
#include <numeric>
#include <fstream>
#include <limits>
#include <bitset>
#define INF 0x3f3f3f3f
#define MAX 1000

using namespace std;

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int caso=1; caso<=t; caso++)
    {
        int a,b,mat1[4][4],mat2[4][4];

        scanf("%d",&a);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%d",&mat1[i][j]);
            }
        }

        scanf("%d",&b);
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                scanf("%d",&mat2[i][j]);
            }
        }

        int vet[16+1];
        memset(vet, 0, sizeof(vet));

        a--;
        b--;

        for(int i=0; i<4; i++)
        {
            vet[mat1[a][i]]++;
            vet[mat2[b][i]]++;
        }

        int counter=0, card;
        for(int i=1; i<=16; i++)
        {
            if(vet[i] == 2)
            {
                counter++;
                card=i;
            }
        }

        if(counter == 1)
        {
            printf("Case #%d: %d\n",caso,card);
        }
        else if(counter == 0)
        {
            printf("Case #%d: Volunteer cheated!\n",caso);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",caso);
        }
    }
    return 0;
}

