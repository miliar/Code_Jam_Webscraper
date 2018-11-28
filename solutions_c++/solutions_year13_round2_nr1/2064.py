/*
 Petar 'PetarV' Velickovic
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
#define MAX_N 101
using namespace std;
typedef long long lld;

int t;
int a, n;
int niz[MAX_N];
int sol = 0;

int main()
{
    freopen("/Users/PetarV/CodeJam/A-small-attempt0.in.txt","r",stdin);
    freopen("/Users/PetarV/CodeJam/small-attempt0-out.txt","w",stdout);
    cin >> t;
    for (int f=1;f<=t;f++)
    {
        sol = 0;
        cin >> a >> n;
        for (int i=0;i<n;i++) cin >> niz[i];
        if (a == 1)
        {
            printf("Case #%d: %d\n",f,n);
            continue;
        }
        sort(niz,niz+n);
        int ii = 0;
        while (ii < n)
        {
            while (ii < n && a > niz[ii])
            {
                a += niz[ii++];
            }
            //cout << "ii = " << ii << ", a = " << a << endl;
            if (ii == n) break;
            int step1 = 0, step2 = n - ii;
            int test = a;
            while (test <= niz[ii])
            {
                test += test-1;
                step1++;
            }
            if (step1 < step2)
            {
                sol += step1;
                a = test + niz[ii++];
            }
            else
            {
                sol += step2;
                ii = n;
            }
        }
        printf("Case #%d: %d\n",f,sol);
        continue;
    }
    return 0;
}
