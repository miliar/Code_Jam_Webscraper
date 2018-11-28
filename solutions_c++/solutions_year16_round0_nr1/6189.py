#include <iostream>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define ll long long
int T,cnt;
ll N, last;
bool ok[10];
void count(ll n)
{
    string s = to_string(n);
    for (auto & c : s)
    {
        if (!ok[c-'0'])
            ++cnt;
        ok[c-'0'] = 1;
    }
}
void solve(int N)
{
    int i;
    for (i = 1;cnt!=10;++i)
        count(N*i);
    last = N*(i-1);
}
int main()
{
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cin >> N;
        cnt = 0;
        memset(ok, 0, sizeof(ok));
        if (N == 0)
            printf("Case #%d: INSOMNIA", i);
        else
        {
            solve(N);
            if (cnt != 10)
                printf("Case #%d: INSOMNIA", i);
            else
                printf("Case #%d: %lld", i, last);
        }
        printf("\n");

    }
}
