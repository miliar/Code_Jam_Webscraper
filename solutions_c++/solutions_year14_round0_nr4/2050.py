#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
#define pc putchar
using namespace std;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("outbig4.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int k=1; k<=t; k++)
    {
       int decpts,optpts,n,j;
       decpts=0;
       optpts=0;
       double naomi[1002],ken[1002];
       int i;
       scanf("%d",&n);
       for(i=0; i<n; i++)
       {
           scanf("%lf",&naomi[i]);
       }
       for(i=0; i<n; i++)
       {
           scanf("%lf",&ken[i]);
       }
       sort(naomi,naomi+n);
       sort(ken,ken+n);

        //Deceitful solution
        for(i=0,j=0;i<n;i++)
        {
            if(naomi[i]>ken[j])
            {
                decpts++;
                j++;
            }
        }

        //Optimal solution
        for(i=0,j=0; i<n; i++)
        {
            if(ken[i]>naomi[j])
            {
                optpts++;
                j++;
            }
        }
        printf("Case #%d: %d %d\n",k,decpts,n-optpts);
    }
    return 0;
}
