#include<cstdio>
#include<string>
#define ull unsigned long long

using namespace std;

bool key[10];

void initiate()
{
    for (int i=0;i<=9;i++)
        key[i]=false;
}

bool mustSleep ()
{
    for (int i=0;i<=9;i++)
        if (!(key[i]))
            return(false);
    return(true);
}

void checkdigit (ull n)
{
    while (n>0)
    {
        key[n%10]=true;
        n/=10;
    }
}

main()
{

    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int c,t,n;

    ull x;
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        initiate();
        scanf("%d",&n);

        if (n==0)
        {
            printf("Case #%d: INSOMNIA\n",i);
        }
        else
        {
            c=1;
            x=n;
            while (!(mustSleep()))
            {
                x=n*c;
                checkdigit(x);
                c++;
            }
            printf("Case #%d: %llu\n",i,x);
        }

    }

}
