#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
//string a1[200],a2[200];
//string ans1,ans2;
//int b1[100005],b2[100005],n;

int min1=INT_MAX;
typedef pair<int,int> ii;

ll gcd(ll a,ll b)
{
    ll r=1;
    while(a%b!=0)
    {
        r=a%b;
        a=b;
        b=r;
    }
    return b;
}
ll modexp(ll base,ll pow1,ll mod)
{
    ll res=1;
    for(;pow1>0;pow1=pow1>>1)
    {
        if(pow1&1)
        {
            res=(res*base)%mod;
        }
        base=(base*base)%mod;
    }
    return res;
}
char a[1005];
int main()
{
    ll t,p,i,j,r,c=1,k,n,s=0,max1=0,m;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    //getchar();
    while(t--)
    {
        scanf("%s%lld",&a,&k);
        //printf("%s %lld\n",a,k);

        n=strlen(a);
        ll count1=0;
        for(i=0;i<=n-k;i++)
        {
            if(a[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    if(a[j]=='-')
                    a[j]='+';
                    else
                    a[j]='-';
                }
                count1++;
            }
            else
            continue;
        }
        int flag=1;
        for(i=0;i<n;i++)
        {
            if(a[i]=='-')
            {
                flag=0;
                break;
            }
        }
        printf("Case #%lld: ",c++);
        if(flag==1)
        {
            printf("%lld\n",count1);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
      //  printf("%s\n",ans);

        // printf("\n");

            //printf("%lld\n",p);


    }
    return 0;
}
