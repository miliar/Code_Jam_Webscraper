#include <cstdio>
#include <iostream>
using namespace std;

char tab[1001];
int t, s, a, wynik, suma;

int main()
{
    scanf("%d", &t);
    while(t--)
    {
        suma=wynik=0;
        a++;
        scanf("%d %s", &s, tab);
        for(int i=0;i<=s;i++)
        {
            if(suma<i)
            {
               wynik+=i-suma;
               suma=i;
            }
            suma+=tab[i]-'0';
        }
        printf("Case #%d: %d\n", a, wynik);
    }
    return 0;
}
