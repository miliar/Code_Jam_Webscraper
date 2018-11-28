#include <bits/stdc++.h>
using namespace std;

const int maxN = 1001;

char in[maxN];
bool end_of_flip[maxN];

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        scanf ("%s", in);
        int n = strlen(in), k;
        scanf ("%d", &k);

        bool flipped = false;
        int res = 0;

        for (int i=0; i<n; i++)
        {
            if (flipped xor in[i] == '-')
            {
                if (i > n - k)
                {
                    res = -1;
                    break;
                }

                res++;
                flipped = !flipped;
                end_of_flip[i + k - 1] = true;
            }

            if (end_of_flip[i])
                flipped = !flipped;
        }

        printf("Case #%d: ", test);
        res == -1 ? printf("IMPOSSIBLE\n") : printf("%d\n", res);
        fill(end_of_flip, end_of_flip + n, false);
    }

    return 0;
}