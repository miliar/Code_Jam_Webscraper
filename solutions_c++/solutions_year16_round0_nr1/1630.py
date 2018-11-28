#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;

bool a[10];
bool check(int x)
{
    while(x/10)
    {
        a[x%10]=1;
        x/=10;
    }
    a[x%10]=1;
    for(int i=0;i<=9;i++)if(!a[i])return 0;
    return 1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++)
    {
        int n;
        scanf("%d",&n);
        //n=ca;
        int ans=-1;
        if(n!=0)
        {
            memset(a,0,sizeof a);
            for(int i=1;i<=210;i++)
            {
                int nn=n*i;
                if(check(nn)){ans=nn;break;}

            }
        }
        printf("Case #%d: ",ca);
        if(ans!=-1)printf("%d\n",ans);
        else printf("INSOMNIA\n");

    }



}
