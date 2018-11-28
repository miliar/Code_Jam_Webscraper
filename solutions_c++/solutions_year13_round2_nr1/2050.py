#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
using namespace std;
int ans,m,n,T,a[102],A,mot;
bool pos(int m)
{
    int cnt,i;
    cnt=0;mot=A;
    for(i=0;i<n;i++)
    {
        if(mot>a[i])mot+=a[i];
        else
        {
            while(a[i]>=mot && mot!=1 && cnt<=m)
            {
                mot+=mot-1;cnt++;
            }
            mot+=a[i];
        }
        if(cnt>m)return 0;
        if(cnt+n-i-1<=m)return 1;
    }
    return cnt<=m;
}
int main()
{
    int i,j,cs,hi,lo,mid;
    freopen("Ain.txt","r",stdin);
    freopen("Aout.txt","w",stdout);
    scanf("%d",&T);
    for(cs=1;cs<=T;cs++)
    {
        scanf("%d %d",&A,&n);
        for(i=0;i<n;i++)scanf("%d",&a[i]);
        sort(a,a+n);

        lo=0;hi=n;
        while(lo<hi)
        {
            mid=(lo+hi)/2;
            if(pos(mid))hi=mid;
            else lo=mid+1;
        }
        if(A==1)hi=n;
        //printf("%d %d\n",A,n);for(i=0;i<n;i++)printf("%d ",a[i]);puts("");
        printf("Case #%d: %d\n",cs,hi);
    }
    return 0;
}

