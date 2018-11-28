#include <cstdio>
#include <vector>
#include <string>
using namespace std;

const long long LIM = 100000000000000LL;

vector <long long> fairsqr;

void generate()
{
    int digits[16];
    int len;
    long long tmp;
    bool good;

    for (long long i=1; i*i<=LIM; ++i)
    {
        tmp = i;

        len = 0;

        do
        {
            digits[len++] = tmp % 10;
            tmp /= 10;
        }
        while (tmp);

        good = true;

        for (int j=0; j<len; ++j)
        {
            if (digits[j] != digits[len - j - 1])
            {
                good = false;
                break;
            }
        }

        if (!good)
            continue;

        tmp = i*i;
        len = 0;

        do
        {
            digits[len++] = tmp % 10;
            tmp /= 10;
        }
        while (tmp);

        good = true;

        for (int j=0; j<len; ++j)
        {
            if (digits[j] != digits[len - j - 1])
            {
                good = false;
                break;
            }
        }

        if (good)
        {
            fairsqr.push_back(i*i);
        }

    }
}

int count(long long n)
{
    if (n < 1) return 0;
    if (n > fairsqr.back()) return fairsqr.size();

    int low = 0, high = fairsqr.size() - 1, mid;
    while (low < high)
    {
        mid = (low + high + 1) / 2;
        if (fairsqr[mid] <= n)
            low = mid;
        else high = mid - 1;
    }
    return low + 1;
}

int main()
{

    freopen("cbig.in", "r", stdin);
    freopen("cbig.out", "w", stdout);


    generate();

    int tests;
    long long a, b;

    scanf("%d", &tests);
    for (int case_no = 1; case_no <= tests; ++case_no)
    {
        printf("Case #%d: ", case_no);
        scanf("%lld %lld", &a, &b);
        printf("%d\n", count(b) - count(a - 1));
    }
}

