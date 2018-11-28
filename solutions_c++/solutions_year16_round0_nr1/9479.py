#include<cstdio>
#include<cstring>

int cif[10];

void addCif(int cif[], int whatCif, int &foundCif)
{
    if(!cif[whatCif])
    {
        cif[whatCif] = 1;
        foundCif++;
    }
}

int solve()
{
    memset(cif, 0 , sizeof(cif));
    int foundCif = 0;
    int n;
    scanf("%d", &n);

    if(n == 0)
    {
        printf("INSOMNIA\n");
        return 0;
    }

    int i = 0;
    while(foundCif < 10)
    {
        ++i;
        long long nn = i * (long long)n;
        while(nn)
        {
            int cf = nn%10;
            addCif(cif, cf, foundCif);
            nn /=10;
        }
    }

    long long rez = i * (long long)n;
    printf("%I64d\n", rez);
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);


    int t = 0;
    scanf("%d",&t);

    for(int i = 0; i < t; ++i)
    {
        printf("Case #%d: ", (i+1));
        solve();
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
