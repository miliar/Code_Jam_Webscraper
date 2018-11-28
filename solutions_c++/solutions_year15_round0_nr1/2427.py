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
    freopen("A-large.in","r",stdin);
    freopen("outlarge","w",stdout);
    scanf("%lld",&T);
    for(k=1;k<=T; k++)
    {
        ll S, i, j, ans = 0, c =0;
        scanf("%lld",&S);
        char A[S+5];
        scanf("%s",A);
        c = A[0] - '0';
        for(i=1;i<S+1;i++){
            if(i > c && A[i]!='0'){
                ans  = ans + i - c;
                c = i + A[i] - '0';
            }
            else{
                c = c + A[i] - '0';
            }
        }
        printf("Case #%lld: %lld\n",k,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
