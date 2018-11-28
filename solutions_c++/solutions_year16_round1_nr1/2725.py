#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <iostream>
#include <deque>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;

string S;

void wczytaj()
{
    cin >> S;
}
void wykonaj()
{
    string wynik;
    for(auto& a : S)
        if(wynik[0] <= a)
            wynik = a + wynik;
        else
            wynik += a;

    cout << wynik << endl;
  //  printf("%s\n", "odpowiedz");
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
