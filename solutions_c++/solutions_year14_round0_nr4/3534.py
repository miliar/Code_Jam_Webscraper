#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int n;
double a[1010],b[1010];

int main()
{
    freopen("D-large.in","rb",stdin);
    freopen("test.out","wb",stdout);
    int T,cas=1;scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",cas++);
        scanf("%d",&n);
        for(int i=0;i<n;++i) scanf("%lf",&a[i]);
        for(int i=0;i<n;++i) scanf("%lf",&b[i]);
        sort(a,a+n);sort(b,b+n);
        int ans1=0,ans2=0;
        for(int i=n-1,j=n-1;i>=0;--i,--j){
            for(;j>=0;--j)
                if(a[i]>b[j]){
                    ++ans1;
                    break;
                }
                else continue;
        }
        for(int i=n-1,j=n-1;i>=0;--i,--j){
            for(;j>=0;--j)
                if(b[i]>a[j]){
                    ++ans2;
                    break;
                }
                else continue;
        }
        printf("%d %d\n",ans1,n-ans2);
    }
    return 0;
}
