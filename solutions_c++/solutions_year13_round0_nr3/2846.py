#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool isPalindrome(long long x)
{
    vector<int> a;
    long long t = x;
    while (t) {
        a.push_back(t % 10);
        t /= 10;
    }

    int n = a.size();
    for (int i = 0; i <= n / 2; ++i) {
        if (a[i] != a[n-1-i]) return false;
    }
    return true;
}

void solve(int caseNum)
{
    // SOLVE TASK HERE!

    // read input
    long long a, b;
    scanf("%lld%lld", &a, &b);

    a = static_cast<long long>(ceil(sqrt(a)));
    b = static_cast<long long>(floor(sqrt(b)));

    long long count = 0;
    for (long long i = a; i <= b; ++i) {
        if (isPalindrome(i) && isPalindrome(i * i)) {
            ++count;
        }
    }

    // output module
    printf("Case #%d: %lld\n", caseNum, count);
}

int main()
{
    int T;
    scanf("%d\n", &T);

    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        solve(caseNum);
    }

    return 0;
}

