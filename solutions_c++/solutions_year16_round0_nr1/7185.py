#include <iostream>
#include <cstdio>

using namespace std;

bool num[12];

bool test()
{
    for(int i = 0 ; i <= 9 ; i++)
        if(num[i] == 0)
            return 0;
    return 1;
}

void wpisz(int k)
{
    while(k > 0)
    {
        num[k%10] = 1;
        k /= 10;
    }
}


void solve()
{
    for(int i = 0 ; i <= 9 ; i++) num[i] = 0;
    int n, sum = 0;
    scanf("%d", &n);
    if(n == 0)
    {
        printf("INSOMNIA\n");
        return;
    }
    while(test() == 0)
    {
        sum += n;
        wpisz(sum);
    }
    printf("%d\n", sum);
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1 ; i <= t ; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
}
