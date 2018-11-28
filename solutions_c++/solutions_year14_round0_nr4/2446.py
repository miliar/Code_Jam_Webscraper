#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
int N;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%d", &N);

        vector<double> naomi;
        vector<double> ken;

        for(int i = 0; i < N; i++)
        {
            double truc;
            scanf("%lf", &truc);
            naomi.push_back(truc);
        }
        for(int i = 0; i < N; i++)
        {
            double truc;
            scanf("%lf", &truc);
            ken.push_back(truc);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        int ptsN = 0;
        int j = 0;

        for(int i = 0; i < N; i++)
        {
            while(j < N && naomi[j] < ken[i])
                j++;
            if(j==N) break;
            ptsN++;
            j++;
        }
        j=0;
        int ptsK = 0;
        for(int i = 0; i < N; i++)
        {
            while(j < N && ken[j] < naomi[i])
                j++;
            if(j==N) break;
            ptsK++;
            j++;
        }
        printf("Case #%d: %d %d\n", t, ptsN, N-ptsK);
    }

    return 0;
}
