#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <stdio.h>
#include <vector>
using namespace std;
int num[2000];
int T;
int ca=1;
vector<int> q;
int main()
{
    int n,P[2000];
    scanf("%d",&T);
    for(ca=1;ca<=T;ca++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&P[i]);
        sort(P,P+n);
        int cost=P[n-1];
        for(int i=P[n-1];i>=1;i--)
        {
            int mm=0;
            for(int j=n-1;j>=0;j--)
            {
                if(P[j]<=i)
                    break;
                if(P[j]%i==0)
                    mm+=P[j]/i-1;
                else
                    mm+=P[j]/i;
            }
            cost=min(cost,mm+i);
        }
        printf("Case #%d: %d\n",ca,cost);
    }
    return 0;
}
