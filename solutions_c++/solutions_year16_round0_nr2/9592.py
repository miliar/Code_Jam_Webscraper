#include<cstdio>
#include<cstring>

char s[128];
/*char ss[128];
int rezcur;
int costminb = 10000;
int n;*/

/*int test()
{
    for(int i = 0; i<n; ++i)
    {
        if(s[i] != '+')
        {
            return 0;
        }
    }

    return 1;
}*/

void flip(int id)
{
    int jum = id / 2;
    for(int i = 0; i<= jum; ++i)
    {
        char aux = s[i];
        s[i] = s[id - i];
        s[id - i] = aux;
    }

    for(int i = 0; i<=id; ++i)
    {
        if(s[i] == '+')
        {
            s[i] = '-';
        }
        else
        {
            s[i] = '+';
        }
    }
}

/*void backflip(int cost)
{
    if(cost < rezcur)
    {
        if(test())
        {
            costminb = cost;
            return;
        }
        for(int i = 0; i<n; ++i)
        {
            flip(i);
            backflip(cost + 1);
            flip(i);
        }
    }
}*/

void solve()
{
    memset(s, 0,sizeof(s));
    scanf("%s",s);

    int n = strlen(s);
    if(s[n-1] == '\n')
    {
        s[n-1] = 0;
        --n;
    }

    int mnrf = 0;
    int dr = n-1;

    while(dr >= 0)
    {
        while(s[dr] == '+' && dr >= 0)
        {
            --dr;
        }

        if(dr < 0)
        {
            break;
        }

        int st = 0;
        while(s[st] == '+')
        {
            st++;
        }

        if(st > 0)
        {
            flip(st - 1);
            mnrf++;
        }

        flip(dr);
        mnrf++;
    }

    printf("%d\n", mnrf);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);

    int t = 0;
    scanf("%d", &t);

    for(int i = 1; i<=t; ++i)
    {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
