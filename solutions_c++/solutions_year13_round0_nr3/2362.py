// GCJ2013_QR_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
using namespace std;

vector<__int64> fsn;

int main(int argc, char* argv[])
{
    int i, j, T;
    __int64 A, B;
    for(i=1;i<=10000000;i++)
    {
        __int64 x=(__int64)i*i;
        int a[20]={0};
        int idx=0;
        while(x)
        {
            a[idx++]=x%10;
            x/=10;
        }
        int head=0, tail=idx-1;
        bool isPalindromes=true;
        while(head<tail)
        {
            if(a[head++]!=a[tail--])
            {
                isPalindromes=false;
                break;
            }
        }
        idx=0;
        x=i;
        while(x)
        {
            a[idx++]=x%10;
            x/=10;
        }
        head=0, tail=idx-1;
        while(head<tail)
        {
            if(a[head++]!=a[tail--])
            {
                isPalindromes=false;
                break;
            }
        }

        if(isPalindromes)
        {
            fsn.push_back((__int64)i*i);
            //printf("%I64d\n", (__int64)i*i);
        }
    }
    freopen("c:/txt/C-large-1.in","r",stdin);
    freopen("c:/txt/2013-QR-C-large.txt","w",stdout);
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        scanf("%I64d %I64d",&A, &B);
        int s=0, e=0;
        for(j=0;j<fsn.size();j++)
        {
            if(fsn[j]>=A)
            {
                s=j;
                break;
            }
        }
        for(j=0;j<fsn.size();j++)
        {
            if(fsn[j]<=B)
            {
                e=j;
            }
        }
        printf("Case #%d: %d\n", i+1, e-s+1);
    }
    return 0;
}

