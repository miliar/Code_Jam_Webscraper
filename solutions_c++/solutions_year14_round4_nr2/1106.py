#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int t;
int nums[11];
int org[11];
int perm[11];
int n;

int Evaluate()
{
    int i,j;
    int inv=0;

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=n;j++)
        {
            if (nums[i]==org[j])
            {
                perm[j]=i;
                break;
            }
        }
    }

    for (i=1;i<=n;i++)
    {
        for (j=1;j<=i-1;j++)
        {
            if (perm[i]<perm[j])
            inv++;
        }
    }

    return inv;
}

bool Check()
{
    int i;
    bool firstpart=true;

    for (i=2;i<=n;i++)
    {
        if (nums[i]>nums[i-1])
        {
            if (!firstpart)
            return false;
        }
        else if (nums[i]<nums[i-1])
        {
            firstpart=false;
        }
    }


    return true;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-ans.txt","w",stdout);

    int test;
    int i;
    int cur,best;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d",&n);

        for (i=1;i<=n;i++)
        {
            scanf("%d",&nums[i]);
            org[i]=nums[i];
        }

        sort(nums+1,nums+1+n);

        best=-1;
        do
        {
            if (!Check())
            continue;

            cur=Evaluate();

            if (best==-1 || cur<best)
            best=cur;

        }while(next_permutation(nums+1,nums+1+n));

        printf("Case #%d: %d\n",test,best);

        fprintf(stderr,"Test %d done\n",test);
    }

    return 0;
}
