#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int F[1000+1][1000+1];
int NowEat,Ans,NowTrans;
int P[1001],MaxP;
int T,D;

int main()
{
    for (int i=1;i<=1000;i++)
        for (int j=1;j<=i;j++)
            F[i][j]=ceil(static_cast<double>(i)/j)-1;
            //精度问题? 是否要减掉eps?

    scanf("%d",&T);
    for (int TestCase=1;TestCase<=T;TestCase++)
    {
        scanf("%d",&D);MaxP=0;
        for (int i=1;i<=D;i++)
        {
            scanf("%d",&P[i]);
            MaxP=max(MaxP,P[i]);
        }
        Ans=88888;//=INF
        for (NowEat=1;NowEat<=MaxP;NowEat++)
        {
            NowTrans=0;
            for (int i=1;i<=D;i++)
                if (NowEat<P[i])
                    NowTrans+=F[P[i]][NowEat];
            Ans=min(Ans,NowTrans+NowEat);
        }
        printf("Case #%d: %d\n",TestCase,Ans);
    }

    return 0;
}
