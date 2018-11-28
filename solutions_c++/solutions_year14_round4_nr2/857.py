#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#define LB(x) ((x)&(-(x)))
using namespace std;
int n,s[1005],T,a[1005],b[1005]; map<int,int> hash;
void inc(int x,int y) {while(x<=n) {s[x]+=y; x+=LB(x);}}
int sum(int x) {int t=0; while(x) {t+=s[x]; x-=LB(x);} return t;}
int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    scanf("%d",&T);
    for(int I=1;I<=T;++I)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;++i) {scanf("%d",&a[i]); b[i]=a[i];}
        sort(b+1,b+n+1); hash.clear(); int ans=0;
        for(int i=1;i<=n;++i) hash[b[i]]=i;
        for(int i=1;i<=n;++i) a[i]=hash[a[i]];
        /*
        for(int i=1;i<=n;++i)
        {
            int cnt;
            for(int j=1;j<=n;++j) if(a[j]==n)
            {
                if(j<=i)
                {
                    for(int k=1;k<j;++k) b[k]=a[k];
                    for(int k=j;k<i;++k) b[k]=a[k+1];
                    b[i]=a[j];
                    for(int k=i+1;k<=n;++k) b[k]=a[k];
                }
                else
                {
                    for(int k=1;k<i;++k) b[k]=a[k];
                    b[i]=a[j];
                    for(int k=i+1;k<=j;++k) b[k]=a[k-1];
                    for(int k=j+1;k<=n;++k) b[k]=a[k];
                }
                cnt=abs(j-i); break;
            }
            memset(s,0,sizeof(s));
            for(int j=1;j<i;++j) {cnt+=sum(n)-sum(b[j]); inc(b[j],1);}
            memset(s,0,sizeof(s));
            for(int j=n;j>i;--j) {cnt+=sum(n)-sum(b[j]); inc(b[j],1);}
            ans=min(ans,cnt);
        }
        */
        for(int i=1;i<=n;++i)
        {
            int l=0,r=0;
            for(int j=1;j<i;++j) if(a[j]>a[i]) ++l;
            for(int j=i+1;j<=n;++j) if(a[j]>a[i]) ++r;
            ans+=min(l,r);
        }
        printf("Case #%d: %d\n",I,ans);
    }
    return 0;
}
