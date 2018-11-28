#include <stdio.h>
#include <math.h>
#include <sched.h>
#include <queue>
#include <iostream>
#include <algorithm>

int MAX_ELEM = 1000;

void solve(std::vector<long double>& naomi, std::vector<long double>& ken, int num, int test)
{
    std::sort(naomi.begin(), naomi.begin()+num);
    std::sort(ken.begin(), ken.begin()+num);

    int ns = 0;
    int nf = num-1;

    int ks = 0;
    int kf = num-1;

    int fair_points = 0;

    // Fair game
    for (int i=0;i<num;++i)
    {
        if (naomi[nf]>ken[kf])
        {
            fair_points++;
            nf--;
            ks++;
        }
        else
        {
            nf--;
            kf--;
        }
    }

    ns = 0;
    nf = num-1;

    ks = 0;
    kf = num-1;

    int unfair_points = 0;

    // unfair game
    for (int i=0;i<num;++i)
    {
        if (naomi[ns]>ken[ks])
        {
            unfair_points++;
            ns++;
            ks++;
        }
        else
        {
            ns++;
            kf--;
        }
    }


    printf("Case #%d: %d %d\n", test+1, unfair_points, fair_points);
}

int main()
{
    struct sched_param param;
    param.sched_priority = 99;
    sched_setscheduler(0, SCHED_FIFO, &param);
    

    int T = 0;
    scanf("%d", &T);

    int num = 0;

    std::vector<long double> naomi;
    std::vector<long double> ken;

    naomi.reserve(MAX_ELEM);
    ken.reserve(MAX_ELEM);

    for (int i=0;i<T;++i)
    {
        scanf("%d", &num);
        
        for (int j=0;j<num;++j)
        {
            scanf("%Lf", &naomi[j]);
        }
        for (int j=0;j<num;++j)
        {
            scanf("%Lf", &ken[j]);
        }
        
        solve(naomi, ken, num, i);
    }
}
