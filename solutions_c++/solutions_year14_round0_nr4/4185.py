/*
 Petar 'PetarV' Velickovic
 Task: Deceitful War
*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>

#define MAX_N 1001

#define DPRINTC(C) printf(#C " = %c\n", (C))
#define DPRINTS(S) printf(#S " = %s\n", (S))
#define DPRINTD(D) printf(#D " = %d\n", (D))
#define DPRINTLLD(LLD) printf(#LLD " = %lld\n", (LLD))
#define DPRINTLF(LF) printf(#LF " = %.5lf\n", (LF))

using namespace std;
typedef long long lld;
typedef unsigned long long llu;

int t, n;
double nb[MAX_N];
double kb[MAX_N];

int main()
{
    freopen("/Users/PetarV/CodeJam/D-large.in.txt","r",stdin);
    freopen("/Users/PetarV/CodeJam/D-large-out1.txt","w",stdout);
    
    scanf("%d", &t);
    
    for (int f=1;f<=t;f++)
    {
        scanf("%d", &n);
        for (int i=0;i<n;i++) scanf("%lf", &nb[i]);
        for (int i=0;i<n;i++) scanf("%lf", &kb[i]);
        sort(nb, nb+n);
        sort(kb, kb+n);
        
        // War - ken will always pick the smallest one that trumps naomi.
        // if none trumps naomi, he will pick the smallest he has.
        
        int j = 0;
        int ptsWar = 0;
        for (int i=0;i<n;i++)
        {
            while (j < n && kb[j] < nb[i]) j++;
            if (j == n) ptsWar++;
            else j++;
        }
        
        // Deceitful war - Naomi will force Ken to get rid of his best blocks.
        int jl = 0, jr = n-1;
        int ptsDWar = 0;
        
        for (int i=0;i<n;i++)
        {
            if (nb[i] < kb[jl] && nb[i] < kb[jr]) jr--;
            else
            {
                ptsDWar++;
                if (nb[i] > kb[jr]) jr--;
                else jl++;
            }
        }
        
        printf("Case #%d: %d %d\n", f, ptsDWar, ptsWar);
    }
    
    return 0;
}