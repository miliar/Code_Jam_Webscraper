#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#define s(x) scanf("%d",&x)
using namespace std;

int main()
{
    int t,i;
    s(t);
    int k;
    for(k=1;k<=t;k++)
    {
        int r,c,w;
        s(r);s(c);s(w);
        int ans=0;
        if(w>c)
            ans=0;
        else
        {
            int cou=w;
            int s=w;
            while(s<c)
            {
                s+=w;
                cou++;
            }
            ans=cou;   
        }
        printf("Case #%d: %d\n",k,ans*r);
    }
    return 0;
}  