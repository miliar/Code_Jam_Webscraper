#include<iostream>
#include<algorithm>
#include<stdio.h>

using namespace std;

#define D double

int main()
{
    int T;
    int cas=1;
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        D arr1[n];
        D arr2[n];
        for(int i=0;i<n;i++) {
                scanf("%lf",&arr1[i]);
        }
        for(int i=0;i<n;i++) {
            scanf("%lf",&arr2[i]);
        }
        sort(arr1,arr1+n);
        sort(arr2,arr2+n);
        int cnt1=0,cnt2=0;
        int j=n-1;
        for(int i=n-1;i>=0 && j>=0;i--) {
            if(arr2[j]>arr1[i]) {cnt1++;j--;}
        }
        j=n-1;
        for(int i=n-1;i>=0 && j>=0;i--) {
            if(arr1[j]>arr2[i]) {cnt2++;j--;}
        }
        printf("Case #%d: %d %d\n",cas,cnt2,n-cnt1);
        cas++;
    }
    return 0;
}
