#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int test;
    scanf("%i", &test);

    for(int t = 1; t <= test; t++)
    {
        printf("Case #%i: ", t);
        int x, n, m;
        scanf("%i %i %i", &x, &n, &m);

        if(x > max(n, m)) printf("RICHARD\n");
        else if((n * m) % x) printf("RICHARD\n");
        else if(x == 1 || x == 2) printf("GABRIEL\n");
        else if(x == 3) printf("%s\n", min(n, m) > 1 ? "GABRIEL" : "RICHARD");
        else
        {
            if(n < m) swap(n, m);
            if(n < 4 && m < 4) printf("RICHARD\n");
            else if(m <= 2) printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
    }

    return 0;
}
