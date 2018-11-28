#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
#define N 1009

double a[N],b[N];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("d1.out","w",stdout);
    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
        int n;
        scanf("%d",&n);

         for(int i=0;i<n;i++) scanf("%lf",&a[i]);
         for(int i=0;i<n;i++) scanf("%lf",&b[i]);
         sort(a,a+n);
         sort(b,b+n);

//         puts("*******\n");
//
//         for(int i=0;i<n;i++) printf("%.3lf ",a[i]);puts("");
//         for(int i=0;i<n;i++) printf("%.3lf ",b[i]);puts("");

         int ans1=0,ans2=0;
         int j=0;
         for(int i=0;i<n;i++)
         {
             while(b[j]<a[i] && j<n)
             {
                 j++;
             }
             if(j<n && b[j]>a[i]) ans2++,j++;
         }
         ans2=n-ans2;

         int x2=0;
         for(int i=0;i<n;i++)
         {
             if(a[i]>b[x2]) ans1++,x2++;
         }

         printf("Case #%d: %d %d\n",ca,ans1,ans2);
    }
    return 0;
}

