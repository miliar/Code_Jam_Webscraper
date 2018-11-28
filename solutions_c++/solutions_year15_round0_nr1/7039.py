#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define ll long long
ll ans;
ll hav;
ll s[1005];
char str[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int kase=1;
    cin>>t;
    while(t--)
    {
        ans=0;
        hav=0;
        int n;
        scanf("%d%s",&n,str);
        for(int i=1;i<=n+1;i++)
        {
            int ti=i-1;
            int si=(int)(str[ti]-'0');
            int tmp;
            if(ti-hav<=0)
            {
                tmp=0;
            }
            else
                tmp=ti-hav;
            ans+=tmp;
            hav+=(si+tmp);
        }
        printf("Case #%d: ",kase++);
        cout<<ans<<endl;
        memset(str,0,sizeof(str));
    }
    return 0;
}
