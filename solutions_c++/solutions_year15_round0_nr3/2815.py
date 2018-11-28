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

int L, X;
char tab[10001];
int tab2[10001];
int q[4][4] = {{1,2,3,4},
               {2,-1,4,-3},
               {3,-4,-1,2},
               {4,3,-2,-1}};

void wczytaj()
{
    scanf("%d", &L);
    scanf("%d", &X);
    scanf("%s", tab);
    FOR(a, L)
        tab2[a] = tab[a]-'i'+2;// i<=>2,j<=>3,k<=>4
}

int mul(int a, int b)
{
    int w = 1;
    if(a*b<0)
        w*=-1;
    if(a<0)a*=-1;
    if(b<0)b*=-1;
    w*=q[a-1][b-1];

    return w;
}

int find_i(int start, int ostatni_wynik = 2)
{
    ++start;
    for(;start<L*X; ++start)
    {
        ostatni_wynik = mul(ostatni_wynik, tab2[start%L]);
        if(ostatni_wynik == 2)
            return start;
    }
    return -1;
}

int find_k(int start, int ostatni_wynik = 4)
{
    --start;
    for(;start>0; --start)
    {
        ostatni_wynik = mul(tab2[start%L], ostatni_wynik);
        if(ostatni_wynik == 4)
            return start;
    }
    return -1;
}

bool czy_j(int start, int koniec)
{
    int w = 1;
    start++;
    while(start < koniec)
    {
        w=mul(w, tab2[start%L]);
        start++;
    }
    return w==3;
}

void wykonaj()
{
    int i = find_i(-1, 1);
    int k = find_k(L*X, 1);
    if(i<0 || k<0 || k<=i+1)
    {
        printf("NO\n");
        return;
    }
    while(true)
    {
        while(true)
        {
            if(czy_j(i,k))
            {
                printf("YES\n");
                return;
            }
            i = find_i(i);
            if(i < 0 || i+1>=k)
                break;
        }
        k = find_k(k);
        if(i+1>=k)
            break;
    }
    printf("NO\n"); // "YES" / "NO"
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
