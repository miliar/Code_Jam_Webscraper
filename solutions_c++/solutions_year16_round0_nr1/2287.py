# include <bits/stdc++.h>
using namespace std;
ifstream fi("a.in");
ofstream fo("a.out");
int T[10];
int Do(int x)
{
    if (!x) {int cnt = T[0];T[0] = 1;return 1 - cnt;}
    int sum = 0;
    while (x)
    {
        sum += !T[x%10];
        T[x%10] = 1;
        x /= 10;
    }
    return sum;
}
int main(void)
{
    int t;
    fi>>t;
    for (int cs = 1;cs <= t;++cs)
    {
        fo << "Case #" << cs << ": ";
        int n;
        fi>>n;
        int sum = 0;
        for (int k = 0;k <= 9;++k) T[k] = 0;
        int ans = 0;
        for (int k = 1;k <= 2e3 && sum != 10;++k)
        {
            ans = k;
            sum += Do(k * n);
        }
        if (ans != 2e3) fo << (ans * n) << '\n';
        else fo << "INSOMNIA" << '\n';
    }
}
