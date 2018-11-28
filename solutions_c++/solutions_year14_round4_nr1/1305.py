#include <cstdio>
#include<algorithm>

using namespace std;

const int N=10010;
int a[N];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,n,x;
    scanf("%d",&t);
    int cs=0;
    while(t--)
    {
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        int l=0,h=n-1;
        int ans=0;
        while(l<=h)
        {
            if(a[l]+a[h]<=x)
            {
                l++;
                h--;
            }
            else h--;
            ans++;
        }
        printf("Case #%d: %d\n",++cs,ans);
    }
    return 0;
}
