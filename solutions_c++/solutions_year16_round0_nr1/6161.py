#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int hulululu(int num)
{
    int found[10] = {0};
    int i,j;
    for(i=1;;i++)
    {
        long long int n = num*i;
        while(n>0)
        {
            found[n%10] = 1;
            n /= 10;
        }
        bool yobro = true;
        for(j=0;j<10;j++)
        {
            if(found[j]==0)
            {
                yobro = false;
                break;
            }
        }
        if(yobro)
        {
            return i;
        }
    }
}

int main()
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&j);
        if(j==0)
        {
            printf("Case #%d: INSOMNIA\n",i+1);
        }
        else
        {
            printf("Case #%d: %d\n",i+1,hulululu(j)*j);
        }
    }
}
