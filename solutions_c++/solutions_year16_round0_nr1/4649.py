#include<bits/stdc++.h>
using namespace std;

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d %d",&x,&y);
#define slld(x) scanf("%lld",&x)
#define rep(i,x,y) for(i=x;i<y;i++)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 1000000007

int f[100];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;
    sd(t);

    for(int q=1;q<=t;q++)
    {
        for(i=0;i<10;i++)
            f[i]=0;
        int n;
        sd(n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",q);
            continue;
        }
        int x=1;
        int ans;
        while(1)
        {
            int a=n*x;

            while(a!=0)
            {
                f[a%10]++;
                a=a-a%10;
                a=a/10;
            }
            int temp=0;
            for(i=0;i<10;i++)
            {
                if(f[i]==0)
                {
                    temp=1;
                    break;
                }
            }
            if(temp==0)
            {
                ans=n*x;
                break;
            }
            x++;
        }


        printf("Case #%d: %d\n",q,ans);
    }


}



