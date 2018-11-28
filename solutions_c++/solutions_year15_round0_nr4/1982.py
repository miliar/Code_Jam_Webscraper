#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstdlib>
#include <set>
#include <map>
#include <fstream>
#include <bitset>

#define PI 3.14159265359

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    //Note: all made by hand as there are only 4*4*4=64 possibilities and we can use symmetry an R*C grid is same as a C*R grid.
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        printf("Case #%d: ", kras);
        int x, r, c;
        scanf("%d %d %d", &x, &r, &c);
        if(r>c)
        {
            swap(r, c);
        }
        if(x==1)
        {
            printf("GABRIEL\n");
        }
        if(x==2)
        {
            if(r==1)
            {
                if(c%2 == 0)
                {
                    printf("GABRIEL\n");
                }
                else
                {
                    printf("RICHARD\n");
                }
            }
            if(r==2)
            {
                printf("GABRIEL\n");
            }
            if(r==3)
            {
                if(c==3)
                {
                    printf("RICHARD\n");
                }
                else
                {
                    printf("GABRIEL\n");
                }
            }
            if(r==4)
            {
                printf("GABRIEL\n");
            }
        }

        if(x==3)
        {
            if(r==1)
            {
                printf("RICHARD\n");
            }
            if(r==2)
            {
                if(c==2)
                {
                    printf("RICHARD\n");
                }
                if(c==3)
                {
                    printf("GABRIEL\n");
                }
                if(c==4)
                {
                    printf("RICHARD\n");
                }
            }
            if(r==3)
            {
                if(c==3)
                {
                    printf("GABRIEL\n");
                }
                if(c==4)
                {
                    printf("GABRIEL\n");
                }
            }
            if(r==4)
            {
                printf("RICHARD\n");
            }
        }

        if(x==4)
        {
            if(r==1)
            {
                printf("RICHARD\n");
            }
            if(r==2)
            {
                if(c==2)
                {
                    printf("RICHARD\n");
                }
                if(c==3)
                {
                    printf("RICHARD\n");
                }
                if(c==4)
                {
                    printf("RICHARD\n");
                }
            }
            if(r==3)
            {
                if(c==3)
                {
                    printf("RICHARD\n");
                }
                if(c==4)
                {
                    printf("GABRIEL\n");
                }
            }
            if(r==4)
            {
                printf("GABRIEL\n");
            }
        }
    }
    return 0;
}
