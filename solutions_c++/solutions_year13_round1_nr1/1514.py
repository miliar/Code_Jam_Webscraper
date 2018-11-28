#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>
#include <deque>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %ld\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;

unsigned long long r,t,p,rpop;
int wynik;
void wczytaj()
{
    wynik=0;
    r=t=0;
    cin >> r >> t;
    //scanf("%ld %ld",&r,&t);

}
void wykonaj()
{

    //rpop=r;
   // r++;
    //p=
    while(1)
    {
        p=2*r+1;
        //DI(p)
        if(t>=p)
        {
            wynik++;
        }
        else
        {
            break;
        }
        t-=p;
        r+=2;
    }
    cout << wynik << endl;
    //printf("%d\n", wynik);
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        wczytaj();
        printf("Case #%d: ",t);
        wykonaj();
    }
    return 0;
}
