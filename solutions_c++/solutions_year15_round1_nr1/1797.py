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
    ll T,z;
 //   freopen("A-large.in","r",stdin);
 //   freopen("A-largeout.txt","w",stdout);

    scanf("%lld",&T);
    for(z=1; z<=T; z++)
    {
        ll N, i, j, ans = 0, ma=0, t,ans1=0;
        scanf("%lld",&N);
        ll A[N];
        for(i=0; i<N; i++)
            scanf("%lld",&A[i]);
        for(i=1; i<N; i++)
        {
            if(A[i-1] - A[i]>0){
                ans = ans + A[i-1] - A[i];
                ma = ma > A[i-1] - A[i] ? ma : A[i-1] - A[i];
            }
        }
        for(i=0; i<N-1; i++)
        {
            t =  A[i]>ma ? ma : A[i];
            ans1 = ans1+ t;
        }
        printf("Case #%lld: %lld %lld\n",z,ans,ans1);
    }

    return 0;
}
