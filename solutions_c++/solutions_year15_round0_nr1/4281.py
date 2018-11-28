#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#define LL long long
#define ULL unsigned long long
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;

char in[102];
LL Smax;

void wczytaj()
{

    scanf("%d", &Smax);
    scanf("%s", in);
}
void wykonaj()
{
    int wynik=0;
    LL wstali = 0;
    FOR(a, Smax+1)
    {
        if(a>wstali)
        {
            wynik+= a-wstali;
            wstali=a;
        }
        wstali += in[a]-'0';
    }

    printf("%ld\n", wynik);
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        wczytaj();
        DI(t)
        printf("Case #%d: ",t);
        wykonaj();
    }
    return 0;
}
