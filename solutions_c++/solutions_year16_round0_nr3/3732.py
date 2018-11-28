#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int divisors[16] = { 0 };
vector<int> digits;

bool is_valid(int i)
{
    digits.clear();
    while (i)
    {
        digits.push_back(i % 2);
        i /= 2;
    }

    for (int base = 2; base <= 10; base++)
    {
        long long val = 0;
        for (int i = digits.size() - 1; i >= 0; i--)
            val = val * base + digits[i];

        bool found_div = false;
        for (long long i = 2; i * i <= val; i++)
            if (val % i == 0)
            {
                found_div = true;
                divisors[base] = i;
            }

        if (!found_div)
            return false;
    }

    return true;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int cnt_cases;
    scanf("%d", &cnt_cases);
    for (int current_case = 1; current_case <= cnt_cases; current_case++)
    {
        int n, j;
        scanf("%d%d", &n, &j);

        printf("Case #%d:\n", current_case);
        for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2)
        {
            if (is_valid(i))
            {
                for (int i = digits.size() - 1; i >= 0; i--)
                    printf("%d", digits[i]);
                for (int i = 2; i <= 10; i++)
                    printf(" %d", divisors[i]);
                printf("\n");

                j--;
                if (j == 0)
                    break;
            }
        }
    }
    return 0;
}
