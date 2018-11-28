#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
using namespace std;

#define inf 0x3f3f3f3f
typedef long long LL;
typedef pair<int,int> PII;

#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define first A
#define second B
LL ans[37],B;
LL getans(LL l,int n)
{
    LL now=0,fee=0;
    for(int i=0;i<n;i++)
    {
        if(l-ans[i]<0)return -1;
        now+=l-ans[i];
    }
    for(int i=n;ans[i]<=l;i++)
    {
        fee+=l-ans[i]+1;
    }
    if(now+fee>B)return -1;
    return 36*now-(now+fee)*n;
}
bool getcan(LL l,int n)
{
    LL now=0,fee=0;
    for(int i=0;i<n;i++)
    {
        if(l-ans[i]<0)continue;
        now+=l-ans[i];
    }
    for(int i=n;ans[i]<=l;i++)
    {
        fee+=l-ans[i]+1;
    }
    return now+fee<=B;
}
LL getR(int n)
{
    LL l=0,r=1.2e12;
    while(l+1<r)
    {
        LL mid=(l+r)>>1;
        if(getcan(mid,n))
        {
            l=mid;
        }
        else r=mid;
    }
    return l;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int ti;scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int n;
        cin >> B >> n;
        memset(ans,0,sizeof(ans));
        for(int i=0;i<n;i++)cin >> ans[i];
        sort(ans,ans+37);
        double profit=0;
        for(int i=1;i<37;i++)
        {
            LL L=ans[i-1];
            LL R=getR(i);
            //cout << i<<" " << L << " "<< R << endl;
            while(L+5<R)
            {
                LL mid=(L+R)/2;
                LL midmid=(L+mid)/2;
                if(getans(mid,i)<getans(midmid,i))
                {
                    R=mid;
                }
                else
                {
                    L=midmid;
                }
            }
            for(int w=-10;w<=15;w++)
                profit=max(profit,1.*getans(L+w,i)/i);
        }
        printf("Case #%d: %.10f\n",ca,profit);
    }
    return 0;
}
