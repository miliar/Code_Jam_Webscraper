#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

#define debug if(1)

using namespace std;

int main()
{
    int t,caseno=1,ans1,ans2,n,lost;
    double arr1[1005],arr2[1005];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        ans1=ans2=0;
        for (int i = 0; i < n; i++) 
        {
            scanf("%lf",&arr1[i]);
        }
        for (int i = 0; i < n; i++) 
        {
            scanf("%lf",&arr2[i]);
        }
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        /*for (int i = n-1; i > 0; i--) 
        {
            if(arr1[i]>arr2[i])
                ans2++;
        }*/
        int i=n-1,j=n-1;
        while(i>-1&&j>-1)
        {
            while(j>-1)
            {
                if(arr2[i]>arr1[j--])
                {ans2++;break;}
            }
            i--;
        }
        //printf("%d\n",n-ans2);
        int lts=0,gts=0;
        for (i = 0; arr1[i] < arr2[0]&&i<n; i++) 
        {
            lts++;
        }
        for (i = n-1; arr2[i] > arr1[n-1]&&i>-1; i--) 
        {
            gts++;
        }
        lost = gts>lts?gts-lts:lts-gts;
        i = j = n-1;
        while(i>-1&&j>-1)
        {
            while(j>-1)
            {
                if(arr1[i]>arr2[j--])
                {ans1++;break;}
            }
            i--;
        } 
        printf("Case #%d: %d %d\n",caseno++,ans1,n-ans2);
    }
    return 0;
}
