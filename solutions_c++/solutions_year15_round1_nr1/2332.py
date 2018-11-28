#include <iostream>
#include<stdio.h>


int arr[100000];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tcase;
    scanf("%d",&tcase);

    int n,diff,maxdiff,i,case1,case2,casecount;

    casecount=0;

    while(tcase--)
    {
        scanf("%d",&n);

        diff=0;
        maxdiff=0;



        scanf("%d",&arr[0]);
        for(i=1;i<n;i++)
        {
            scanf("%d",&arr[i]);

            diff=arr[i-1]-arr[i];

            if(diff>0)
            {
                if(diff>maxdiff)
                    maxdiff=diff;
            }

        }
        // first case
        case1=0;

        for(i=0;i<n-1;i++)
        {
            if(arr[i+1]<arr[i])
                case1=case1+(arr[i]-arr[i+1]);
        }


        // second case

        case2=0;

        for(i=0;i<n-1;i++)
        {
            if(arr[i+1]>=arr[i])
            {
                case2=case2+std::min(maxdiff,arr[i]);
            }
            else
                case2=case2+std::min(maxdiff,arr[i]);
        }

        casecount++;
        printf("Case #%d: %d %d\n",casecount,case1,case2);

    }
    return 0;
}
