#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int T;
int A, N, index;
int m[102];
long long S, yes, no, ans;

int main()
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    scanf("%d", &T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d", &A, &N);
        for(int i = 0; i < N; i++)
            scanf("%d", &m[i]);
        sort(m, m + N);

/*
        for(int i = 0; i < N; i++)
            printf("%d ", m[i]);
        printf("\n");
*/
        if (A == 1)
        {
            printf("Case #%d: %d", t, N);
            if (t < T)
                printf("\n");
            continue;
        }

        yes = 0;
        S = A;
        index = 0;

        while (true)
        {
            //cout<<"___DB: S = "<<S<<", m[i] = "<<m[index]<<"\n";
            no = N - index + yes;

            if (S > m[index])
            {
                S += m[index];
            }
            else
            {
                while (S <= m[index])
                {
                    S += (S - 1);
                    yes++;
                }
                S += m[index];
            }

            //cout<<"___DB: S = "<<S<<", m[i] = "<<m[index]<<", yes = "<<yes<<", no = "<<no<<"\n";

            if (yes >= no)
            {
                ans = no;
                break;
            }

            no--;
            index++;
            if (index == N)
            {
                ans = yes;
                break;
            }
        }
        printf("Case #%d: %d", t, ans);
        if (t < T)
                printf("\n");
    }
    return 0;
}
