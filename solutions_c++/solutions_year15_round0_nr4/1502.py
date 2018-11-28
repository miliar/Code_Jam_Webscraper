#include <stdio.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <string.h>

#include <bits/stdc++.h>        //include every c++ library
                                //fgets(array_name,array_size,stdin);
                                //FLT_MAX FLT_MIN INT_MAX INT_MIN DBL_MAX DBL_MIN
#define mod 1000000007
#define ll long long int
using namespace std;

struct point
{
     ll X;
     ll Y;
};

bool operator<(point const& n1, point const& n2)
{
    return n1.X<n2.X || (n1.X==n2.X && n1.Y<n2.Y);
}

void check(ll A[], ll N)
{
    ll i;
    for(i=0; i<N; i++)
        printf("%lld ",A[i]);
    printf("\n");
}


int main()
{
    ll T,k;
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out","w",stdout);

    scanf("%lld",&T);

    for(k=1; k<=T; k++)
    {
        printf("Case #%lld: ",k);
        ll X, R, C, i, j, ans = 0;
        scanf("%lld%lld%lld",&X,&R,&C);
        if(X == 1)
        {
            printf("GABRIEL\n");
        }
        else if(X == 2)
        {
            if((R*C)%2==0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
        else if(X == 3)
        {
            if((R == 3 || C == 3) && (R != 1 && C != 1))
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");

        }
        else if(X == 4)
        {
            if((R ==  4 && C == 4)|| (R*C == 12))
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");

        }
        else{}
        printf("");
    }
     fclose(stdin);
    fclose(stdout);

    return 0;
}
