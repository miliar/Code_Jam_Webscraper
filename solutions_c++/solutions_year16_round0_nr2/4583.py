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
   int j,k,t,l,i,cnt,ans,end;
   char s[105],a,b;
   cin>>t;
   for(k=1;k<=t;k++)
   {
    ans=0;
    cin>>s;
    l=strlen(s);
    end=l-1;
    while(end>-1)
    {
        if(s[end]=='+')
            end--;
        else
        {
            if(s[0]=='+')
            {
                ans++;
                cnt=1;
                while(s[cnt]=='+')
                    cnt++;
                for(i=0;i<cnt;i++)
                    s[i]='-';
            }
            ans++;
            for(i=0;i<=end/2;i++)
            {
                a=s[i];
                b=s[end-i];
                if(a=='-')
                    s[end-i]='+';
                else
                    s[end-i]='-';
                if(b=='-')
                    s[i]='+';
                else
                    s[i]='-';
            }
        }
    }
    cout<<"Case #"<<k<<": "<<ans<<"\n";
   }

   return 0;
}