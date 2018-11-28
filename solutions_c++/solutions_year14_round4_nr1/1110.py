#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int n,x;
int t;
int nums[10001];
bool taken[10001];
int discs;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large-ans.txt","w",stdout);

    int i,j,in;
    int test;
    int a;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d %d",&n,&x);

        memset(taken,false,sizeof(taken));
        discs=0;

        for (j=1;j<=n;j++)
        {
            scanf("%d",&nums[j]);
        }

        sort(nums+1,nums+1+n);

        for (j=n;j>=1;j--)
        {
            if (taken[j])
            continue;

            for (in=j-1;in>=1;in--)
            {
                if (taken[in])
                continue;

                if (nums[in]+nums[j]<=x)
                {
                    taken[in]=true;
                    break;
                }
            }

            taken[j]=true;

            discs++;
        }

        printf("Case #%d: %d\n",test,discs);
    }

    return 0;
}
