/*
Name:: Vivek Kumar Yadav
Language:: C++
Handle:: vivekjnv93
*/
#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

#define fori(i,n) for(i=0;i<n;++i)
#define forn(i,n) for(i=n-1;i>=0;--i)
#define nil NULL
#define itr iterator
#define MAX(a,  b) ((a) > (b) ? (a) : (b))
#define MIN(a,  b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SQ(X) ( (X) * (X) )
//#define getchar getchar_unlocked

typedef long int li;
typedef long long int lli;
typedef long double ld;

/*------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++Source Code+++++++++++++++++++++++++++++++++++++
------------------------------------------------------------------------------*/
//Functions and Global variables
//main

int main()
{
    int t,k;
    double c,f,x,initial=0,est=0,rate,aft=0,tc;
    FILE *fi= fopen("in.txt","r");
    FILE *fo= fopen("out.txt","w");
    fscanf(fi,"%d",&t);
    k=0;
    while(t--)
    {
        k++;
        //initial = 0;
        rate = 2;
        tc=0;
        fscanf(fi,"%lf%lf%lf",&c,&f,&x);
        while(1)
        {
            est = tc+x/rate;
            aft = tc+c/rate+x/(rate+f);
            if(est>aft)
            {
                tc = tc+c/rate;
                rate = rate+f;
                continue;
            }
            else
            {
                break;
            }
        }
        fprintf(fo,"Case #%d: %.7lf\n",k,est);
        //printf("Case #%d: %.7lf\n",k,est);
    }
    return 0;




}
