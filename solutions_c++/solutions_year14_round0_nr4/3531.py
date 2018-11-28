#include <cstdio>
#include <algorithm>
using namespace std;

double a1[1000];
double a2[1000];

int main()
{
    int kase;
    scanf("%d",&kase);
    for (int k=1; k<=kase; k++)
    {
        int N;
        scanf("%d",&N);
        int ans1 = 0;
        int ans2 = 0;
        for (int i = 0; i<N; i++)
            scanf("%lf", &a1[i]);
        for (int i = 0; i<N; i++)
            scanf("%lf", &a2[i]);

        sort(a1,a1+N);
        sort(a2,a2+N);

        int j;
        for (int i = j = 0; i <N && j<N ; j++)
        {
            while (a1[i] <= a2[j] && i <N)
                i++;
            if (i>=N)
                break;
            if (a1[i] > a2[j])
                ans1++;
            i++;
        }
        for (int i = j = 0; i <N && j<N ; j++)
        {
            while (a2[i] <= a1[j] && i <N)
                i++;
            if (i>=N)
                break;
            if (a2[i] > a1[j])
                ans2++;
            i++;
        }

        printf("Case #%d: %d %d\n",k, ans1, N-ans2);

    }

    return 0;
}
