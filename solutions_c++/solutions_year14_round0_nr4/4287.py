#include <stdio.h>
#include <algorithm>

using namespace std;

int main ()
{
    int T;
    int N, war, deceitful;
    double naomi[1000], ken[1000];
    bool nused[1000], kused[1000];
    scanf("%d", &T);
    for (int t = 0; t < T; ++t)
    {
        scanf("%d", &N);
        war = 0, deceitful = 0;

        for (int i = 0; i < N; ++i)
        {
            scanf("%lf", &naomi[i]);
        }

        for (int i = 0; i < N; ++i)
        {
            scanf("%lf", &ken[i]);
        }

        sort(naomi, naomi + N);
        sort(ken, ken + N);

        // deceitful war
        for (int i = 0; i < N; ++i)
        {
            nused[i] = false;
            kused[i] = false;
        }

        for (int i = 0; i < N; ++i)
        {
            nused[i] = true;
            double nchosen = naomi[i];
            double kchosen = 0;
            int kindex = -1;
            // get smallest available ken
            for (int j = 0; j < N && kchosen == 0; ++j)
            {
                if (!kused[j])
                {
                    kchosen = ken[j];
                    kindex = j;
                }
            }

            // If nchosen is less than all ken, get biggest available ken, else keep smallest available ken
            if (nchosen < kchosen)
            {
                bool stop = false;
                for (int j = N-1; j >= 0 && !stop; --j)
                {
                    if (!kused[j])
                    {
                        kchosen = ken[j];
                        kindex = j;
                        stop = true;
                    }
                }
            }
            kused[kindex] = true;

            if (nchosen > kchosen)
            {
                deceitful++;
            }
        }

        // war
        for (int i = 0; i < N; ++i)
        {
            nused[i] = false;
            kused[i] = false;
        }

        for (int i = 0; i < N; ++i)
        {
            nused[i] = true;
            double nchosen = naomi[i];
            double kchosen = 0;
            for (int j = 0; j < N && kchosen == 0; ++j)
            {
                if (ken[j] > nchosen && !kused[j])
                {
                    kused[j] = true;
                    kchosen = ken[j];
                }
            }

            if (kchosen == 0)
            {
                for (int j = 0; j < N && kchosen == 0; ++j)
                {
                    if (!kused[j])
                    {
                        kused[j] = true;
                        kchosen = ken[j];
                    }
                }
            }

            if (nchosen > kchosen)
            {
                war++;
            }
        }

        printf("Case #%d: %d %d\n", t+1, deceitful, war);
    }
}
