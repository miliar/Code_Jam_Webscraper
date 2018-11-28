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
#define Max 1005

using namespace std;
 double A[Max], B[Max];
 int indexB[Max]={0};

int getLocation(double num, int t)
{
    int i;
    bool isfound = false;
    for( i=0; i<t;i++)
    {
        if(B[i] > num && indexB[i] != -1 )
        {
            isfound = true;
            indexB[i] = -1;
            break;
        }

    }
    if(isfound)
        return i;
    else
        return -1;
}

int getWt(double num, int t)
{
    int i;
    bool isfound= false;
    for( i=0; i<t; i++)
    {
        if(A[i] > num && indexB[i] != -1)
        {
            isfound = true;
            indexB[i] = -1;
            break;
        }
    }
    if(isfound == false )
    {
        for(i=0; i<t;i++)
        {
            if(indexB[i] !=-1)
                indexB[i] = -1;
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
         indexB[j]=0;
        q=t-1;
        for(int j=0; j<t;j++)
            scanf("%lf",&A[j]);
         for(int j=0; j<t;j++)
            scanf("%lf",&B[j]);
        sort(A,A+t);
        sort(B,B+t);
        for(int j= t-1; j>=0; j--)
        {
            if(getLocation(A[j],t) == -1 )
            {
                indexB[p] = -1;
                p++;
                cb++;
            }

        }
        for(int j=0; j<t;j++)
         indexB[j]=0;

         for(int j=t-1; j>=0;j--)
         {
             if(getWt(B[j],t) == 1)
                ca++;

         }



        printf("Case #%d: %d %d\n",i+1,ca, cb);



    }

    return 0;
}
