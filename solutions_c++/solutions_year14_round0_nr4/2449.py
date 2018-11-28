#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
int t;
double a[1100],b[1100];
int n;
int main()
{
    freopen("D1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        for(int i=0;i<n;++i)
        {
            scanf("%lf",&a[i]);
        }
        for(int i=0;i<n;++i)
        {
            scanf("%lf",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        int k=0;
        int ans1=0,ans2=0;

//        for(int i=0;i<n;++i)
//        {
//            printf("%lf ",a[i]);
//        }
//        printf("\n");
//        for(int i=0;i<n;++i)
//        {
//            printf("%lf ",b[i]);
//        }
//         printf("\n");
        for(int i=0;i<n&&k<n;++i)
        {
            if(a[i]>b[k]){ans1++;k++;}
        }
        k=0;
        for(int i=0;i<n&&k<n;++i)
        {
            if(b[i]>a[k]){ans2++;k++;}
        }

        printf("%d %d\n",ans1,n-ans2);
    }

    return 0;
}
