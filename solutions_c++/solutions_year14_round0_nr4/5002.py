#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#define inf 2000000000
#define ll long long
#define Max 12

using namespace std;
 double a[Max], b[Max];
 int indexb[Max]={0};

int getloc(double num, int t)
{
    int i;
    bool isfound = false;
    for( i=0; i<t;i++)
    {
        if(b[i] > num && indexb[i] != -1 )
        {
            isfound = true;
            indexb[i] = -1;
            break;
        }

    }
    if(isfound)
        return i;
    else
        return -1;
}

int getweight(double num, int t)
{
    int i;
    bool isfound= false;
    for( i=0; i<t; i++)
    {
        if(a[i] > num && indexb[i] != -1)
        {
            isfound = true;
            indexb[i] = -1;
            break;
        }
    }
    if(isfound == false )
    {
        for(i=0; i<t;i++)
        {
            if(indexb[i] !=-1)
                indexb[i] = -1;
            return -1;
        }
    }
    return 1;
}

int main()
{
    int n,t;
    freopen("input.in","r",stdin);
     freopen("out.in","w",stdout);
    scanf("%d", &n);
    for(int i=0; i<n;i++)
    {

        int cb=0,ca=0,p=0,q;

        scanf("%d",&t);
         for(int j=0; j<t;j++)
         indexb[j]=0;
        q=t-1;
        for(int j=0; j<t;j++)
            scanf("%lf",&a[j]);
         for(int j=0; j<t;j++)
            scanf("%lf",&b[j]);
        sort(a,a+t);
        sort(b,b+t);
        for(int j= t-1; j>=0; j--)
        {
            if(getloc(a[j],t) == -1 )
            {
                indexb[p] = -1;
                p++;
                cb++;
            }

        }
        for(int j=0; j<t;j++)
         indexb[j]=0;

         for(int j=t-1; j>=0;j--)
         {
             if(getweight(b[j],t) == 1)
                ca++;

         }



        printf("Case #%d: %d %d\n",i+1,ca, cb);



    }

    return 0;
}
