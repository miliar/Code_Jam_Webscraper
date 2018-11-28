#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int n,m;
int prim(ll x)
{
    if (x<2) return 0;
    for (int i=2;i<=sqrt(x);i++)
    if (x%i==0) return 0;
    return 1;
}

int pan(ll x)
{
    int a[1234]={0};
    int t=0;
    while (x)
    {
        a[++t]=x%2;
        x/=2;
    }
    if (a[1]!=1||a[t]!=1) return 0;
    for (int p=2;p<=10;p++){
        ll tmp=0;
        for (int i=t;i>=1;i--)
        tmp=tmp*p+a[i];
        if (prim(tmp)) return 0;
    }
    return 1;
}

int fuck(ll x)
{
    for (int i=2;i<=sqrt(x);i++)
    if (x%i==0) return i;
}

void ok(ll x)
{
    int a[1234]={0};
    int t=0;

    while (x)
    {
        a[++t]=x%2;
        x/=2;
    }
    for (int i=t;i>=1;i--) printf("%d",a[i]);

    for (int p=2;p<=10;p++){
          ll tmp=0;
    for (int i=t;i>=1;i--)
        tmp=tmp*p+a[i];
        printf(" %d",fuck(tmp));

    }
    printf("\n");
}

void test(int x)
{
    int b[1234]={0};
    int t=0;
    while(x)
    {
        b[++t]=x%10;
        x/=10;
    }
    for (int i=2;i<10;i++)
    {
        int tmp=0;
        for (int j=t;j>=1;j--)
             tmp=tmp*i+b[j];
        cout<<tmp<<" ";
    }
}

int main()
{
    int T;
 // test(100001);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for (int _=1;_<=T;_++){
         cin>>n>>m;
         printf("Case #%d:\n",_);
         int ans=0;
         for (ll j=(1ll<<(n-1));j<(1ll<<n);j++)
         {
             ll tmp=j;
             if (pan(tmp))  {
                    ok(tmp);
                    ans++;
             }
             if (ans==m) break;
          }
     }
    return 0;
}
