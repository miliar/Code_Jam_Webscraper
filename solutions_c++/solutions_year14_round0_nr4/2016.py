#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, tc;
    int N;
    double naomi[1100], ken[1100];
    int i, j;
    int naomiLicik, kenLicik;

    cin >> T;

    for(tc=1;tc<=T;tc++)
    {
        cin >> N;

        for(i=0;i<N;i++)
        {
            scanf("%lf", &naomi[i]);
        }
        for(i=0;i<N;i++)
        {
            scanf("%lf", &ken[i]);
        }
        sort(naomi, naomi+N);
        sort(ken, ken+N);

        naomiLicik = 0;
        kenLicik = 0;

        //naomi licik
        i = 0; j = 0;

        while(i<N && j<N)
        {
            for(;i<N;i++)
            {
                if(naomi[i] > ken[j])
                {
                    naomiLicik++;
                    break;
                }
            }
            i++; j++;
        }

        //ken licik
        i = 0; j = 0;

        while(i<N && j<N)
        {
            for(;i<N;i++)
            {
                if(ken[i] > naomi[j])
                {
                    kenLicik++;
                    break;
                }
            }
            i++; j++;
        }

        printf("Case #%d: %d %d\n", tc, naomiLicik, N-kenLicik);
    }


    return 0;
}

