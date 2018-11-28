#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int i,j,k,l,m,n;
    int f;
    freopen("D-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    float arr1[10000];
    float arr2[10000];
    int ans1,ans2;
    int count = 0;
    int c=0;
    int test;
    int flag[10000];
    scanf("%d",&test);
    while(test--)
    {
        c=0;
        printf("Case #");
        printf("%d: ",++count);
        scanf("%d",&n);
        for(i=0;i<n;i++)
            flag[i]=0;
        for(i=0;i<n;i++)
            scanf("%f",&arr1[i]);
        for(i=0;i<n;i++)
            scanf("%f",&arr2[i]);
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        ///////////////////
    /*    printf("\n");
        for(i=0;i<n;i++)
        printf("%f ",arr1[i]);
        printf("\n");
        for(i=0;i<n;i++)
        printf("%f ",arr2[i]);
        printf("\n");*/
        ///////////////////
        ans2 = 0;
        i=0;
        j=0;
        while(j<n)
        {
            if(arr2[j]>arr1[i])
            {
                i++;j++;
                ans2++;
            }
            else
                j++;
        }
        ans2 = n-ans2;

        //////
        ans1 = 0;
        i=0;
        j=0;
        while(j<n)
        {
            if(arr1[j]>arr2[i])
            {
                i++;j++;
                ans1++;
            }
            else
                j++;
        }
        ans1 = ans1;

        ////

        printf("%d %d\n",ans1,ans2);

    }
    return 0;
}
