#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll b[10005];
ll a[100][100];
int main()
{
    ll t,n,p,i,j,r,c=1,x;

    freopen("B-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld",&n);
        vector<ll> ans;


        memset(b,0,sizeof(b));
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%lld",&x);
                b[x]++;
            }
        }
        //printf("%lld\n",b[1]);
        for(i=1;i<=2500;i++)
        if(b[i]%2==1)
        ans.push_back(i);
        sort(ans.begin(),ans.end());
        printf("Case #%lld:",c++);
        for(i=0;i<n;i++)
        {
            printf(" %lld ",ans[i]);
        }
        printf("\n");

    }
    return 0;
}
