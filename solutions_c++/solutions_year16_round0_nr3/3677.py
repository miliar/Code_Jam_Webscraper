#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll pri[1000005];
ll vis[1000005];
vector <ll> ans;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    /*int p=0;
    for(ll i=2; i<=1000000; i++)
    {
        if(!vis[i])
        {
            vis[i]=1;
            pri[p++]=i;
            for(ll j=i*i; j<=1000000; j+=i)
                vis[j]=1;
        }
    }*/
    int cas,c=1;
    scanf("%d",&cas);
    while(cas--)
    {
        int n,m,cnt=0;
        scanf("%d %d",&n,&m);
        printf("Case #%d:\n",c++);
        //for(int i=32769;i<=65535;i+=2)
        for(ll i=(1<<(n-1))+1; i<=(1<<n)-1; i+=2)
        {
            ll x=i;
            int tmp[20];
            memset(tmp,0,sizeof(tmp));
            ans.clear();
            for(int j=0; j<n; j++)
            {
                tmp[j]=x&1;
                x>>=1;
            }
            for(int j=2; j<=10; j++)
            {
                x=0;
                for(int k=n-1; k>=0; k--)
                {
                    x*=j;
                    x+=tmp[k];
                }
                //cout<<x<<endl;
                if(x%2==0)
                {
                    ans.push_back(2);
                }
                else
                {
                    for(ll k=3;k*k<=x;k++)
                    {
                        if(x%k==0&&x!=k)
                        {
                            ans.push_back(k);
                            break;
                        }
                    }
                }
            }
            if(ans.size()==9)
            {
                for(int j=n-1; j>=0; j--)
                    printf("%d",tmp[j]);
                for(int j=0;j<ans.size();j++)
                    printf(" %I64d",ans[j]);
                puts("");
                cnt++;
                if(cnt==m)
                    break;
            }
        }
    }
}
