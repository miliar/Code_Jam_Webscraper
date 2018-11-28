#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
int A, B, K;

void wczytaj()
{
    scanf("%d %d %d", &A, &B, &K);
}
void wykonaj()
{
    int wynik=0;
    for(int i=0;i<A;i++)
        for(int j=0;j<B;j++)
        {
            if(int(i&j)<K)
            {
                wynik++;
               // printf("%d, %d\n",i,j);
            }
        }
    printf("%d\n", wynik);
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
