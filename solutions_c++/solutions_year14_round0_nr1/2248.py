#include <cstdio>
#include <iostream>
#define pc putchar
using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("outsmall0.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int x,y;
    for(int k=1; k<=t; k++)
    {
        int p1[4]; int p2[4]; int re1,re2,re3,re4;
        scanf("%d", &x);

        for(int j=1; j<x; j++)
        {
            scanf("%d %d %d %d\n", &re1,&re2,&re3,&re4);

        }
        scanf("%d %d %d %d\n", &p1[0], &p1[1], &p1[2], &p1[3]);

        for(int j=x+1; j<=4; j++)
        {
            scanf("%d %d %d %d\n", &re1,&re2,&re3,&re4);

        }
        scanf("%d", &y);
        for(int j=1; j<y; j++)
        {
            scanf("%d %d %d %d\n", &re1,&re2,&re3,&re4);

        }
        scanf("%d %d %d %d\n", &p2[0], &p2[1], &p2[2], &p2[3]);

        for(int j=y+1; j<=4; j++)
        {
            scanf("%d %d %d %d\n", &re1,&re2,&re3,&re4);

        }
        int ctr=0, ans=0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if(p1[i]==p2[j])
                {
                    ans=p1[i];
                    ctr++;
                }
            }
        }
        if(ctr>1)
            printf("Case #%d: Bad Magician!\n", k);
        else if(ctr==0)
            printf("Case #%d: Volunteer cheated!\n", k);
        else
            printf("Case #%d: %d\n", k, ans);
        scanf("\n");
    }
	return 0;
}
