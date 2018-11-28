#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <deque>
#define FOR(x,z) for(int x=0;x<(z);++x)
#define DS(i) fprintf(stderr, "DEBUG: %s\n",i);
#define DI(i) fprintf(stderr, "DEBUG: %d\n",i);
#define DF(i) fprintf(stderr, "DEBUG: %f\n",i);
using namespace std;
int wynik;

void wczytaj()
{
    wynik = 0;
    bool rev = false;
    string s;
    cin >> s;
    for(int i = s.size()-1; i>=0; --i)
    {
        if(!rev)
        {
            if(s[i] == '+')
            {
                continue;
            }
            else
            {
                wynik++;
                rev = true;
            }
        }
        else
        {
            if(s[i] == '-')
            {
                continue;
            }
            else
            {
                wynik++;
                rev = false;
            }
        }
    }
}
void wykonaj()
{
    printf("%d\n",wynik);
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
