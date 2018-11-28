#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
using namespace std;

const int N = 10000001;
int num[N];

bool check(long long k)
{
    int n = 0, a[20];
    while (k)
    {
        a[n++] = k % 10;
        k /= 10;
    }
    for (int i = 0; i * 2 < n; ++i)
        if (a[i] != a[n - 1 - i]) return false;
    return true;
}

int main()
{
    int T;
    long long a, b;
    
    freopen("C-large-1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    memset(num, 0, sizeof(num));
    for (long long i = 1; i < N; ++i)
        if (check(i) && check(i * i)) ++num[i];
    for (int i = 1; i < N; ++i) num[i] += num[i - 1];
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        cin >> a >> b;
        printf("Case #%d: ", cas);
        cout << num[(int)sqrt(b)] - num[(int)sqrt(a - 1)] << "\n";
    }
    return 0;
}
