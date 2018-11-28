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
int N;
int CN;
int i;
vector<bool> cyfry;

void wczytaj()
{
    cyfry = {false,false,false,false,false,false,false,false,false,false};
    scanf("%d", &CN);
    N = CN;
}

bool isAsleep()
{
    for(int i =0;i<10;++i)
        if(cyfry[i]==false)
            return false;

    return true;
}

void wypelnij(int N)
{
    while(N)
    {
        cyfry[N%10] = true;
        N/=10;
    }
}

void wykonaj()
{
    if(N == 0)
    {
        printf("%s\n", "INSOMNIA");
        return;
    }
    while(1)
    {
        wypelnij(N);
        if(isAsleep())
        {
            printf("%d\n", N);
            break;
        }
        N+=CN;
    }

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
