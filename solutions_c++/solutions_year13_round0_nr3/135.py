#include <gmpxx.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

mpz_class numbers[1000000];
int total = 0;

void output (const char* s)
{
    mpz_class number, squared;

    number = s;
    squared = number*number;

    std::string s2 = squared.get_str();

    // check pal
    for (int n = s2.size(), i = n/2; i >= 0; i--) {
        if (s2[i] != s2[n-1-i]) {
            return;
        }
    }

    numbers[total++] = squared;
}

void transform (long long unsigned value, int mpad, char* target)
{
    int length = 0;
    for (int t = value; t; t >>= 1) ++length;

    target[length+mpad+length] = 0;

    for (int i = 0; i < length; ++i) {
        target[length - 1 - i] =
        target[length + mpad + i] =
          (value&1) + '0';
        value >>= 1;
    }
}

bool good (long long unsigned value) {
    const long long unsigned mask = 0x3FF;
    while (value) {
        if ((value & mask) == mask) return false;
        value >>= 1;
    }
    return true;
}

void gen_even (int n)
{
    char target[512];
    for (long long unsigned i = 1LLU << (n-1); i < (1LLU << n); ++i) {
        if (!good(i)) continue;
        transform(i, 0, target);
        output(target);
    }

    string two(n*2, '0');
    two[0] = two[n*2-1] = '2';
    output(two.c_str());
}

void gen_odd (int n) {
    char target[512];
    for (long long unsigned int i = 1LLU << (n-1); i < (1LLU << n); ++i) {
        if (!good(i)) continue;
        transform(i, 1, target);

        target[n] = '0'; output(target);
        target[n] = '1'; output(target);
        target[n] = '2'; output(target);
    }

    string two(n*2+1, '0');
    two[0] = two[n*2] = '2';

    output(two.c_str());
    two[n] = '1'; output(two.c_str());
}

void gen(int n)
{
    if (n == 1) {
        output("1");
        output("2");
        output("3");
    }

    else if (n % 2 == 0)
        gen_even(n/2);
    else
        gen_odd(n/2);
}

void solve (int CASE)
{
    mpz_class a, b;
    cin >> a >> b;

    mpz_class* ap;
    mpz_class* bp;

    ap = std::lower_bound(numbers, numbers + total, a);
    bp = std::upper_bound(numbers, numbers + total, b);

    printf("Case #%d: %ld\n", CASE, bp - ap);
}


int main ()
{
    fprintf(stderr, "Preloading..\n");
    for (int i = 1; i <= 51; i++) {
        cerr << i << endl;
        gen(i);
    }
    fprintf(stderr, "Preloaded %d thingamajigs.\n", total);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) solve(i);

    return 0;
}
