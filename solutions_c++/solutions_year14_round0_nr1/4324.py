/*
 Petar 'PetarV' Velickovic
 Task: Magic Trick
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

#define DPRINTC(C) printf(#C " = %c\n", (C))
#define DPRINTS(S) printf(#S " = %s\n", (S))
#define DPRINTD(D) printf(#D " = %d\n", (D))
#define DPRINTLLD(LLD) printf(#LLD " = %lld\n", (LLD))
#define DPRINTLF(LF) printf(#LF " = %.5lf\n", (LF))

using namespace std;
typedef long long lld;
typedef unsigned long long llu;

int t;
int a1, a2;
int mat1[5][5], mat2[5][5];

map<int, int> mst;

int main()
{
    freopen("/Users/PetarV/CodeJam/A-small-attempt0.in.txt","r",stdin);
    freopen("/Users/PetarV/CodeJam/A-small-out1.txt","w",stdout);
    
    scanf("%d",&t);
    for (int f=1;f<=t;f++)
    {
        scanf("%d", &a1);
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf("%d", &mat1[i][j]);
            }
        }
        
        scanf("%d", &a2);
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                scanf("%d", &mat2[i][j]);
            }
        }
        
        mst.clear();
        
        for (int j=0;j<4;j++)
        {
            mst[mat1[a1-1][j]]++;
            mst[mat2[a2-1][j]]++;
        }
        
        int cnt = 0, sol = 0;
        
        map<int, int>::iterator it;
        
        for (it = mst.begin(); it != mst.end(); it++)
        {
            if (it -> second == 2)
            {
                cnt++;
                sol = it -> first;
            }
        }
        
        printf("Case #%d: ", f);
        
        if (cnt == 0) printf("Volunteer cheated!\n");
        else if (cnt > 1) printf("Bad magician!\n");
        else printf("%d\n", sol);
    }
    return 0;
}