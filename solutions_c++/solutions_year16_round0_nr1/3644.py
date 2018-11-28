#include <iostream>
#include <bitset>

using namespace std;
using ll = long long;

int main()
{
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; ++test)
    {
        printf("Case #%d: ", test);

        ll N;
        scanf("%lld", &N);

        if (N == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }

        bitset<11> digits;
        ll next = 0;

        while (digits.count() < 10)
        {
            next += N;
            ll temp = next;
        
            while (temp)
            {
                int d = temp % 10;
                temp /= 10;

                digits[d] = 1;
            }
        }

        printf("%lld\n", next);
    }

    return 0;
}
