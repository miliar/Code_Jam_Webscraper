#include<cstdio>
#include<algorithm>
#define N 26
using namespace std;

struct Party
{
    char c;
    int num;
    bool operator<(const Party& a){ return num > a.num; }
}party[N];
int main()
{
    int Case;
    scanf("%d", &Case);
    for (int t = 1; t <= Case; t++)
    {
        int n, i, j, sum = 0;
        scanf("%d", &n);

        for (i = 0; i < n; i++)
        {
            party[i].c = 'A' + i;
            scanf("%d", &party[i].num);
            sum += party[i].num;
        }

        printf("Case #%d:", t);
        sort(party, party + n);

        int max, idx1 = 0, idx2 = n - 1, half;
        while (sum)
        {
            putchar(' ');
            max = party[idx1].num;
            half = (sum - 1) / 2;
            if (max <= half)
            {
                party[idx2].num--;
                putchar(party[idx2].c);
                sum--;
            }
            else if (max - 1 >= party[idx1 + 1].num)
            {
                party[idx1].num--;
                putchar(party[idx1].c);
                sum--;
            }
            else
            {
                putchar(party[idx1].c);
                putchar(party[idx2].c);
                party[idx1].num--;
                party[idx2].num--;
                sum -= 2;
            }

            if (!party[idx2].num)
                idx2--;

            if (!party[idx1].num)
                idx1++;

        }

        putchar('\n');
    }
    return 0;
}