#include<bits/stdc++.h>
#include<iostream>
/* 
int iscompo(int n)
{
    int i,sq;
    sq=sqrt(n);
    for(i=2;i<=sq;i++)
    {
        if(n%i==0)
            return 1;
    }
    return 0;
}
int gcd(int x,int y){if(y==0)return x;return gcd(y,x%y);}
int pw(int x,int y){if(y==0)return 1;int z=pw(x,y/2);if(y%2==0)return z*z;return z*z*x;}
*/
#define sci(n) scanf("%d",&n)
#define scl(n) scanf("%lld",&n)
#define scf(n) scanf("%f",&n)
#define pri(n) printf("%d\n",n)
#define prl(n) printf("%lld\n",n)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define abs(a) (a>0?a:-a)
#define ll long long int
#define max_long LLONG_MAX
#define min_long LLONG_MIN
#define MOD 1000000007
/*struct price
{
    int x;
    int index;
};
bool my(price lhs,price rhs)
{
    return lhs.x<rhs.x;
}*/
using namespace std;
int main(){
   int c,s,t,i,j,k;
   unsigned long long int n,cnt;
   cin>>t;
   for(j=1;j<=t;j++)
   {
    cin>>k>>c>>s;
    cout<<"Case #"<<j<<": ";
    if(c==1)
    {
        if(s<k)
            cout<<"IMPOSSIBLE";
        else
            for(i=1;i<=k;i++)
                cout<<i<<" ";

    }
    else if(k==1)
    {
        if(s==0)
            cout<<"IMPOSSIBLE";
        else
            cout<<1;
    }
    else if(s<k-1)
        cout<<"IMPOSSIBLE";
    else
    {
        cnt=2;
        n=k+1;
        for(i=1;i<k;i++)
        {
            cout<<cnt<<" ";
            cnt+=n;
        }

    }
    cout<<endl;
   }
   return 0;
}