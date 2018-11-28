#include <bits/stdc++.h>

using namespace std;

int a[50] , s[50] , sol[50];
int t , n , j , S;

bool prime(int x)
{
    for (int i = 2 ; i * i <= x ; ++i)
    if (x % i == 0) return false;

    return true;
}

void bkt(int k)
{
    if (k == n)
    {
        int check = 1;

        for (int i = 2 ; i <= 10 ; ++i)
        sol[i] = 0;

        for (int base = 2 ; base <= 100 ; ++base)
        if (prime(base))
        {
            for (int i = 2 ; i <= 10 ; ++i)
            {
                s[i] = 0;
                for (int j = 1 ; j <= n ; ++j)
                s[i] = (i * s[i] + a[j]) % base;

                if (s[i] == 0) sol[i] = base;
            }
        }

        for (int i = 2 ; i <= 10 ; ++i)
        if (sol[i] == 0) return;

        for (int i = 1 ; i <= n ; ++i)
        printf("%d" , a[i]);

        printf(" ");

        for (int i = 2 ; i <= 10 ; ++i)
        printf("%d " , sol[i]);

        printf("\n");
        S++;
        if (S == j) exit(0);

        return ;
    }

    a[k] = 1;
    bkt(k + 1);
    a[k] = 0;
    bkt(k + 1);
}

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

scanf("%d" , &t);
scanf("%d" , &n);
scanf("%d" , &j);

printf("Case #1:\n");

a[1] = a[n] = 1;
bkt(2);

return 0;
}
