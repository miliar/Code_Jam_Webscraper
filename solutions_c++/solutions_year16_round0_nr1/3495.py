typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>

using namespace std;
int main()
{
    ll t,n,temp,i,r,flag,w=1,f[10],j;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        memset(f,0,sizeof(f));
        i=1;
        if(n==0)
        printf("Case #%lld: INSOMNIA\n",w++);
        else
        {
        while(1)
        {
        temp=i*n;
        while(temp!=0)
        {
            r=temp%10;
            f[r]++;
            temp/=10;
        }
        flag=0;
        for(j=0;j<=9;j++)
        {
            if(f[j]==0)
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
        break;
        i++;
        }
        printf("Case #%lld: %lld\n",w++,i*n);
        }
    }
	return 0;
}