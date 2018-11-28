#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <queue>
#include <vector>

using namespace std;

double num1[1024],num2[1024];
bool used[1024];
int main()
{
    int cas,ca=1;
    int n,cnt1,cnt2;

    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&cas);
    while(cas--)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
           scanf("%lf",&num1[i]);
        for(int i=0;i<n;i++)
           scanf("%lf",&num2[i]);
        sort(num1,num1+n);
        sort(num2,num2+n);
        cnt1=cnt2=0;
        memset(used,false,sizeof(used));
        for(int i=n-1;i>=0;i--)
        {
            bool flag=false;
            for(int j=0;j<n;j++)
            {
                if(used[j])
                   continue;
                if(num2[j]>num1[i])
                {
                    flag=true;
                    used[j]=true;
                    break;
                }
            }
            if(!flag)
            {
                cnt2++;
                for(int j=0;j<n;j++)
                {
                    if(!used[j])
                    {
                        used[j]=true;
                        break;
                    }
                }
            }
        }
        memset(used,false,sizeof(used));
        for(int i=0;i<n;i++)
        {
            bool flag=false;
            for(int j=n-1;j>=0;j--)
            {
                if(used[j])
                   continue;
                if(num1[i]>num2[j])
                {
                    cnt1++;
                    flag=true;
                    used[j]=true;
                    break;
                }
            }
            if(!flag)
            {
                for(int j=n-1;j>=0;j--)
                {
                    if(!used[j])
                    {
                        used[j]=true;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",ca++,cnt1,cnt2);
    }
    return 0;
}
