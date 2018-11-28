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
    ll T, k;
    freopen("B-large.in","r",stdin);
    freopen("out","w",stdout);
    scanf("%lld",&T);
    for(k=1; k<=T; k++)
    {
        ll D, i, j, ans = 0, ma, ma2, t, n, posm, posm2;
        scanf("%lld",&D);
        ll A[D], B[D];
        memset(B,0, sizeof(B));
        for(i=0; i<D; i++)
            scanf("%lld",&A[i]);
        sort(A ,A+D , greater<ll>());
        t = A[0];
        ma = A[0];
        ans = 0;

        for(i=ma;i>=0; i--)
        {
            ma = 0;
            ma2 = 0;
            for(j=0; j<D; j++)
            {
                n = A[j]/(B[j]+1);
                if(A[j]%(B[j]+1) !=0)
                    n++;
                if(ma < n)
                {
                    ma2 = ma;
                    posm2 = posm;
                    ma = n;
                    posm = j;
                }
                else if(ma2 < n)
                {
                    ma2 = n;
                    posm2 = j;
                }
            }
            n = A[posm]/(B[posm]+2);
            if(A[posm]%(B[posm]+2) !=0)
                    n++;
            if(max(n,ma2) + 1 + ans < t)
            {
                ans++;
                t = ans + max(ma/2 + ma%2,ma2);
                B[posm]++;
            }
            else
            {
                ans++;
                B[posm]++;

            }
        }
        printf("Case #%lld: %lld\n",k,t);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
