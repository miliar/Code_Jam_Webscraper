#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long LL;
LL a[1000010];
LL aa[1000010];
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int n,p,q,r,s;scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
        aa[0] = 0;
        for(LL i=0;i<n;i++)
        {
            a[i] = (i*p+q)%r + s;
            aa[i+1] = aa[i] + a[i];
            //printf("%I64d ",a[i]);
        }
        LL ret = aa[n];
        for(int R=1;R<=n;R++)//[L,R]
        {
            LL SL = aa[R];
            int LL = lower_bound(aa,aa+R+1,SL/2.0) - aa;
            for(int L=max(LL-2,1);L<=min(R,LL+2);L++)
            {
                ret = min(ret, max(aa[L-1],max(aa[R]-aa[L-1],aa[n]-aa[R])));
            }
        }
        printf("Case #%d: %.11f\n",ca,1-ret*1./aa[n]);
    }
}
