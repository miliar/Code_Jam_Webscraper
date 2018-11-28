#include <cstdio>

int v[1010];

bool palin(int n)
{
    int dig=0;
    int num = n;

    int dig3 = num%10;
    num /= 10;
    int dig2 = num%10;
    num /= 10;
    int dig1 = num%10;

    if (dig1 == 0)
    {
        if (dig2 == 0)
            return(true);
        else
        {
            if (dig2==dig3)
                return(true);
            else
                return(false);
        }
    }
    else
    {
        if (dig1 == dig3)
            return(true);
        else
            return(false);
    }

}

void insert_palin(int n)
{
    for (int i=n; i<1001; i++)
        v[i]++;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int T;
    int A, B;

    for (int i=1; i<10; i++)
    {
        if (palin(i*i))
            insert_palin(i*i);
    }

    insert_palin(121);
    insert_palin(484);

    scanf("%d", &T);

    for (int i=1; i<=T; i++)
    {
        scanf("%d %d", &A, &B);
        printf("Case #%d: %d\n", i, v[B]-v[A-1]);
    }



    return(0);
}
