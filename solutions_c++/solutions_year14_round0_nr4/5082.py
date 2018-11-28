#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

double Naomi[11];
double Ken[11];
int n;
int t;
int perm[11];
bool taken[11];

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int test;
    int i,j;
    int WarAns;
    int DecWarAns;
    int CurWarAns;
    int CurDecWarAns;
    bool KenWin;
    bool TrickShot;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d",&n);

        for (i=1;i<=n;i++)
        {
            cin>>Naomi[i];
        }

        for (i=1;i<=n;i++)
        {
            cin>>Ken[i];
        }

        sort(Ken+1,Ken+1+n);

        for (i=1;i<=n;i++)
        {
            perm[i]=i;
        }

        WarAns=0;
        DecWarAns=0;

        do
        {
            CurWarAns=0;
            CurDecWarAns=0;

            memset(taken,false,sizeof(taken));

            for (i=1;i<=n;i++)
            {
                KenWin=false;

                for (j=1;j<=n;j++)
                {
                    if (!taken[j] && Ken[j]>Naomi[ perm[i] ])
                    {
                        taken[j]=true;
                        KenWin=true;
                        break;
                    }
                }

                if (!KenWin)
                {
                    CurWarAns++;

                    for (j=1;j<=n;j++)
                    {
                        if (!taken[j])
                        {
                            taken[j]=true;
                            break;
                        }
                    }
                }
            }

            memset(taken,false,sizeof(taken));

            for (i=1;i<=n;i++)
            {
                KenWin=false;
                TrickShot=false;

                for (j=1;j<=n;j++)
                {
                    if (!taken[j])
                    {
                        if (Ken[j]<Naomi[ perm[i] ])
                        {
                            CurDecWarAns++;
                            taken[j]=true;
                            TrickShot=true;
                        }
                        break;
                    }
                }

                if (TrickShot)
                continue;

                for (j=n;j>=1;j--)
                {
                    if (!taken[j] && Ken[j]>Naomi[ perm[i] ])
                    {
                        taken[j]=true;
                        KenWin=true;
                        break;
                    }
                }

                if (!KenWin)
                {
                    CurDecWarAns++;

                    for (j=1;j<=n;j++)
                    {
                        if (!taken[j])
                        {
                            taken[j]=true;
                            break;
                        }
                    }
                }
            }

            if (CurWarAns>WarAns)
            WarAns=CurWarAns;

            if (CurDecWarAns>DecWarAns)
            DecWarAns=CurDecWarAns;

        }while( next_permutation(perm+1,perm+1+n) );

        printf("Case #%d: %d %d\n",test,DecWarAns,WarAns);
    }

    return 0;
}
