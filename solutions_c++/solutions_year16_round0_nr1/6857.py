#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

set<int> s;

void addd(long long x)
{
    while(x)
    {
        int a = x % 10;
        s.insert(a);
        x /= 10;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int oo;
    scanf("%d", &oo);
    for(int o = 0; o < oo; o++)
    {
        int n;
        scanf("%d", &n);
        s.clear();
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", o + 1);
        } else
        for(long long i = 0; i < 1000000000LL; i++)
        {
            long long y = i * n;
            addd(y);
            if(s.size() == 10)
            {
                cout << "Case #" << o + 1 << ": " << y << endl;
                break;
            }
        }
    }
}
