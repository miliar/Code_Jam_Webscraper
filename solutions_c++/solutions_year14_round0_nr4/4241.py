#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
double a[1005];
double b[1005];
int war()
{
    int cnt =0;
    int L = 0;
    for(int i=0;i<n;i++)
    {
        while(L<n&&b[L]<a[i]) L++;
        if(L<n){
            cnt++;
            L++;
        }else{
            break;
        }
    }
    return n-cnt;
}
int deceitful()
{
    int L,R,re=0;
    L = 0;
    R = n-1;
    for(int i=0;i<n;i++)
    {
        if(b[R]!=1&&a[i]>b[L]){ 
            re++;
            L++;
        }
        else{
            R--;
        } 
    }
    return re;
}
int main ()
{
    freopen("D-large.in","r",stdin);
    freopen("out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int icase = 1;icase<=T;icase++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%lf",&a[i]);
        for(int i=0;i<n;i++)
        scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        printf("Case #%d: %d %d\n",icase,deceitful(),war());
    }
    return 0;
}
