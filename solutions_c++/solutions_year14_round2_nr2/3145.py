#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<string.h>
using namespace std;

main()
{

    int i,j,k,n,m,t,ans=0,flag=0,a,b,k1;

    FILE *fin  = fopen ("input.in", "r");
    FILE *fout = fopen ("output.txt", "w");
    fscanf(fin,"%d",&t);
    for(k=1;k<=t;k++)
    {
        ans=0;
        fscanf(fin,"%d %d %d",&a,&b,&k1);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                n=i&j;
                if(n<k1)
                ans++;
            }
        }
        fprintf(fout,"Case #%d: %d\n",k,ans);
    }
    return 0;
}
