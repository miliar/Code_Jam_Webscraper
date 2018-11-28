#include <cstdio>
#include <cmath>
#include <vector>

std::vector<long long> vec;

long long a = 0LL;
long long b = 100000000000000LL;

int check(long long val)
{
    char buf[32]; 
    int len = sprintf(buf, "%lld", val);
    for (int i = 0; i < len / 2; ++i) {
        if (buf[i] != buf[len - i - 1])
            return 0;
    }
    return 1;
}

int getnum(long long a, long long b)
{
    int res = 0;
    for (std::vector<long long>::iterator it = vec.begin(); it != vec.end(); ++it) {
        if (*it >= a && *it <= b) {
            ++res;
        }
    }
    return res;
}

int main()
{
    /* pre-populate */
    long long sqrta = sqrt(a);
    long long sqrtb = sqrt(b);
    for (long long i = sqrta; i <= sqrtb; ++i) {
        long long sqr = i * i;
        if (sqr >= a && sqr <= b && check(i) && check(sqr)) {
            vec.push_back(sqr);
        }
    }

    int testnum;

    FILE * fd = fopen("input", "r");
    fscanf(fd, "%d", &testnum);
    for (int test = 1; test <= testnum; ++test) {
        fscanf(fd, "%lld %lld", &a, &b);
        printf("Case #%d: %d\n", test, getnum(a, b));
    }
}

