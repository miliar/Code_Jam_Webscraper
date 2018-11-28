#pragma warning(disable:4996)

#include <stdio.h>
#include <vector>

using namespace std;

int get_divisor(long long x)
{
    for (long long i=2; i*i<=x; i++)
    {
        if (x%i == 0)
            return i;
    }
    return -1;
}

int main()
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);

    int n, j;
    scanf("%*d%d%d", &n, &j);
    printf("Case #1:\n");
    for (long long i = (1<<(n-1))+1; i < (1<<n) && j; i += 2)
    {
        vector<int> ans;
        for (int b=2; b<=10; b++)
        {
            long long mul = 1;
            long long x = 0;
            for (int k=0; k<n; k++)
            {
                int d = !!(i & (1<<k));
                x += mul * d;
                mul *= b;
            }

            int divisor = get_divisor(x);
            if (divisor == -1)
                break;
            ans.push_back(divisor);
        }

        if (ans.size() == 9)
        {
            vector<int> r;
            long long num=i;
            while (num)
                r.push_back(num%2), num/=2;
            for (int i=r.size()-1; i>=0; i--)
                printf("%d", r[i]);
            for (int i=0; i<ans.size(); i++)
                printf(" %d", ans[i]);
            printf("\n");
            j--;
        }
    }

    return 0;
}
