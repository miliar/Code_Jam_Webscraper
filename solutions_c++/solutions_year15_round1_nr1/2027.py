#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int TC, tcase;
    scanf("%d", &TC);
    for(tcase = 1;  tcase <= TC; tcase++)
    {
        int N;
        scanf("%d", &N);

        vector <int> update;

        int temp;

        for(int i = 0; i < N; i++)
        {
            scanf("%d", &temp);
            update.push_back(temp);
        }

        double max_rate = 0;
        int any = 0, cnst = 0;
        for(int i = 0; i < N-1; i++)
        {
            if(update[i] > update[i+1])
            {
                any+=abs(update[i] - update[i+1]);

                double rate = (abs(update[i] - update[i+1])) / 10.00;
                if(rate > max_rate)
                {
                    max_rate = rate;
                }
            }
        }
        for(int i = 0; i < N-1; i++)
        {
            double max_possible_per_ten = (max_rate*10.0);
            cnst+=min((int)max_possible_per_ten, update[i]);
        }

        printf("Case #%d: %d %d\n", tcase, any,cnst);
    }
    return 0;
}
