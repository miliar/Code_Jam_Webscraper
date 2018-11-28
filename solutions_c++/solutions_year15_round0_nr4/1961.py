#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#include <set>
#define LL long long
#define ULL unsigned long long
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;

int X, R, C;
string wynik = "RICHARD"; //GABRIEL

void wczytaj()
{
    scanf("%d", &X);
    scanf("%d", &R);
    scanf("%d", &C);
}

string wykonaj()
{
//    if(R*C < 2*X)
//        return "RICHARD";
    if((R*C)%X != 0)
        return "RICHARD";
    if(2*(C+1)-1 <= X || 2*(R+1)-1 <= X)
        return "RICHARD";
    if(X>=4 && 3*X > R*C)
        return "RICHARD";
//    if(X>=3 && (R*C <= X*X))
//        return "RICHARD";

    return "GABRIEL";
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
        wynik = wykonaj();
        //printf("%d %d %d: ",X, R, C);
        printf("%s\n", wynik.c_str());
    }
    return 0;
}
