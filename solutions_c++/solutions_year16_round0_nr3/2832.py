#include <cstdlib>
#include <algorithm>
#include <cstdio>

using namespace std;

int T;
int N,J;
int curcnt;
int tab[33];

bool check(bool print)
{
    if(print)
    {
        for(int i = 0; i < N; i++)
            putchar((char)(tab[i])+'0');
    }

    for(int base=2; base<=10;base++)
    {
        long long oki=-1;
        long long nb = 0;
        for(int i = 0; i < N; i++)
        {
            nb = base*nb + tab[i];
        }
        
        for(long long p = 2; p*p <= nb; p++)
        {
            if(nb % p == 0)
                oki=p;
        }
        if(oki==-1)
            return false;
        
        if(print)
            printf(" %lld", oki);
    }
    if(print)printf("\n");
    return true;
}

void compute(int pos)
{
    if(pos==N-1)
    {
        if(check(false))
        {
            check(true);
            curcnt++;
        }
    
        if(curcnt==J)
            exit(0);
        return;
    }
    
    tab[pos]=0;
    compute(pos+1);
    tab[pos]=1;
    compute(pos+1);
}

int main()
{   
    scanf("%d", &T);
    scanf("%d%d", &N, &J);
    
    printf("Case #1:\n");
    tab[0]=tab[N-1]=1;
    compute(1);
    
    return 0;
}

