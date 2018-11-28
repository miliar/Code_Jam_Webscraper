#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <ctime>
#include <cstdlib>
#include <stack>
#include <queue>
using namespace std;

long long M=1099511627776;

int main()
{
    long long P,Q;
    int t,T;
    freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("A-small-attempt0.out.txt","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%lld/%lld",&P,&Q);
        long long tmp=Q;
        while(tmp%2==0)
        {
            tmp/=2;
        }
        if(tmp!=1)
        {
            if(P==tmp)
            {
                P/=tmp;
                Q/=tmp;
            }
            else
            {
                printf("Case #%d: impossible\n",t);
                continue;
            }
        }
        P=P*(M/Q);
        tmp=M;
        int ans=-1;
        while(P!=0)
        {
            long long fl=P/tmp;
            P-=fl*tmp;
            tmp/=2;
            ans++;
            if(fl>0)break;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}