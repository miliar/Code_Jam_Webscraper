#include <iostream>
using namespace std;

const int size = 39;

long long array[size]= {
    1LL, 
    4LL, 
    9LL, 
    121LL, 
    484LL, 
    10201LL, 
    12321LL, 
    14641LL, 
    40804LL, 
    44944LL, 
    1002001LL, 
    1234321LL, 
    4008004LL, 
    100020001LL, 
    102030201LL, 
    104060401LL, 
    121242121LL, 
    123454321LL, 
    125686521LL, 
    400080004LL, 
    404090404LL, 
    10000200001LL, 
    10221412201LL, 
    12102420121LL, 
    12345654321LL, 
    40000800004LL, 
    1000002000001LL, 
    1002003002001LL, 
    1004006004001LL, 
    1020304030201LL, 
    1022325232201LL, 
    1024348434201LL, 
    1210024200121LL, 
    1212225222121LL, 
    1214428244121LL, 
    1232346432321LL, 
    1234567654321LL, 
    4000008000004LL, 
    4004009004004LL
};

int count(long long num)
{
    int ans = 0;

    for (int i = 0; i < size; ++i)
    {
        if (array[i] <= num)
        {
            ++ans;
        }
        else
        {
            break;
        }
    }

    return ans;
}

//3 6
int main ()
{
    int kase, ncase = 0;
    long long begin, end;

    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    scanf("%d", &kase);
    while (kase--)
    {
        scanf("%lld %lld", &begin, &end);
        printf("Case #%d: %d\n", ++ncase, count(end) - count(begin - 1));
    }

    return 0;
}
