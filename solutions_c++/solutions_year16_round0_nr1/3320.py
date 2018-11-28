#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    long long int n,t,sv,dig[11],ct,ind,temp,rt,ans;
    scanf("%lld",&t);
    sv=t;

    while(t--)
    {
        memset(dig,0,sizeof(dig));
        ct=0; ind=1;
        scanf("%lld",&n);
        if(n==0)
        printf("Case #%lld: INSOMNIA\n",sv-t);
        else
        {
            while(ct<10)
            {
                temp=n*ind;
                ans=temp;
                while(temp>0)
                {
                    rt=temp%10;
                    if(dig[rt]==0)
                    {
                        dig[rt]=1;
                        ct++;
                    }
                    temp/=10;
                    if(ct==10)
                    break;
                }
                ind++;
            }

            printf("Case #%lld: %lld\n",sv-t,ans);
        }
    }

    return 0;
}
