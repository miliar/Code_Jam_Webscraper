#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#define mp make_pair
#define ll long long
#define s second
#define f first
#define pii pair<int,int>
#define pll pair<ll,ll>
using namespace std;
const ll c=2000,inf=2000000000ll;
bool pal(ll n)
{
     string s="";
     while (n)
     {
           s+=char(n%10+'0');
           n/=10;
     }
     for (int i=0; 2*i<s.size(); i++)
         if (s[i]!=s[s.size()-i-1])
            return 0;
     return 1;
}
ll value(string s)
{
   ll res=0;
   for (int i=0; i<s.size(); i++)
       res=10*res+s[i]-'0';
   return res;
}
bool nine(string s)
{
     for (int i=0; i<s.size(); i++)
         if (s[i]!='9')
            return 0;
     return 1;
}
ll next_pal(ll n)
{
     string s="";
     int k;
     while (n)
     {
           s+=char(n%10+'0');
           n/=10;
     }
     k=s.size();
     if (nine(s))
        {
         s="1";
         for (int i=1; i<k; i++)
             s+="0";
         s+="1";
         return value(s);
        }
     else {
           int x=0;
           while (!nine(s.substr(x,k-2*x)))
                 x++;
           x--;
           int q=s[x]+1;
           s[x]=s[k-x-1]=char(q);
           for (int i=x+1; i<k-x-1; i++)
               s[i]='0';
           return value(s);
          }
}
int main()
{
    //ios_base::sync_with_stdio(0);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int u=1; u<=t; u++)
    {
        ll A,B;
        ll res=0;
        cin>>A>>B;
        ll x,y;
        x=(ll) sqrt(A);
        y=(ll) sqrt(B);
        while (x*x<A || !pal(x))
              x++;
        for (ll n=x; n<=y; n=next_pal(n))
        {
            if (pal(n*n))
               res++;
        }
        printf("Case #%d: %d\n",u,res);
    }
    //system("pause");
    return 0;
}
