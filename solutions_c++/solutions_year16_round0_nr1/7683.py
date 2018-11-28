#include <cstdio>
using namespace std;

typedef long long LL;

int d,n;

int ma[10];
int ile;

bool dodaj(LL num)
{
    while(num > 0)
    {
        int cyfra = num % 10;
        num /= 10;
        if(ma[cyfra] == 0)
        {
            ma[cyfra] = 1;
            ile++;
        }
    }
    return ile == 10;
}

int main() 
{
    scanf("%d",&d);
    for(int i=1;i<=d;i++)
    {
        ile = 0;
        for(int i2=0;i2<10;i2++)
            ma[i2] = 0;
            
        scanf("%d",&n);
        if(n == 0)
        {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        LL res = n;
        while(dodaj(res) == 0)
        {
            res += n;
        }
        
        printf("Case #%d: %lld\n", i, res);
    }
    return 0;
}

