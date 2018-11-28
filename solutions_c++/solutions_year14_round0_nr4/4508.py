#include<cstdio>
#include<algorithm>
using namespace std;
double a[1100],b[1100];
int main()
{
    int i,j,n,r,q,x,y;
    scanf("%d",&q);
    for(r=1;r<=q;r++){
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);    sort(b,b+n);
        for(i=n-1,x=0,j=n;i>=0;i--){
            for(j--;j>=0&&b[j]>=a[i];j--);
            if(j>=0) x++;
        }
        for(i=0,y=0,j=-1;i<n;i++){
            for(j++;j<n&&b[j]<a[i];j++);
            if(j>=n) y++;
        }
        printf("Case #%d: %d %d\n",r,x,y);
    }
    return 0;
}
