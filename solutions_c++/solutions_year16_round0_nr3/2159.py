#include <bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;

ll pw(ll x, ll y, ll z)
{
    if(y==0) return 1;
    if(y==1) return x%z;
    ll ans= pw(x, y/2, z);
    ans*=ans;
    ans%=z;

    if(y%2) ans*=x;
    ans%=z;
    return ans;
}

vector<int> v, v2[20005];
int used[200005];

void sv()
{
    for(int i=2; i<100000; i++)
    {
        if(used[i]==0)
        {
            used[i]=1;
            v.pb(i);
//            printf("%d\n",i);
            for(int j=i+i; j<100000; j+=i)
            {
                used[j]=1;
            }
        }
    }
}


int main()
{
    sv();

    freopen("C-large.in", "r", stdin);
    freopen("out.txt","w", stdout);

    int t,n,K;

    scanf("%d",&t);

    while(t--)
    {
        printf("Case #1: \n");
        scanf("%d %d",&n,&K);
        int q=0;

        for(ll i=0; i<1ll<<(n-2); i++)
        {
//            printf("%d %lld\n",q,i);
            v2[q].pb(i);
            for(int j=2; j<11; j++)
            {
                for(int k=0; k<v.size(); k++)
                {
                    if(n==16)
                    {
                        ll y=1;
                        for(int kk=0; kk<n; kk++)
                        {
                            if(i&(1ll<<kk))
                            {
                                y+= pw(j, kk+1, 1000000000000000000);
                            }
                        }
                        y+= pw(j, n-1, 1000000000000000000);
                        if(y==v[k]) break;
                    }
//                    printf(" %d %d %lld %d   %d %d\n",k, v.size(),i,j, v2[q].size(), v[k]);
                    ll x=1;

                    for(int l=0; l<n; l++)
                    {
//                        printf("%lld %d %d %d\n",i,j,k,l);
                        if(i&(1ll<<l))
                        {
                            x+= pw(j, l+1, v[k]);
                            x%=v[k];
                        }
                    }
                    x+= pw(j,n-1, v[k]);
                    x%=v[k];

//                    if(x==0)printf("%d %d %lld\n",j,v[k],x);
                    if(x==0)
                    {
                        v2[q].pb(v[k]);
                        break;
                    }
                }
            }
//            printf("%d\n",q);
            if(v2[q].size()==10)
            {
                q++;
//                printf("  q %d %d\n",q,K);
                if(q==K) break;
            }
            v2[q].clear();
        }

        char s[100];

        for(int i=0; i<K; i++)
        {
            ll x=v2[i][0];
            int y=n-2;
            while(y>0)
            {
                s[y]= x%2+ '0';
                x/=2;
                y--;
            }
            s[0]='1';
            s[n-1]= '1';
            s[n]='\0';
            printf("%s",s);

            for(int j=1; j<10; j++)
            {
                printf(" %d", v2[i][j]);
            }
            printf("\n");
        }
    }
}
