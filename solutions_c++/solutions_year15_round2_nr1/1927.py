#include<bits/stdc++.h>
using namespace std;
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define ss(n) scanf(" %s",n)
#define s2(a,b) scanf("%d %d",&a,&b)
#define pb push_back
#define mp make_pair
#define vi vector<int>
#define ii pair<int,int>
#define F first
#define S second
#define P printf
#define E <<endl
#define ll long long

ll rev(ll number)
{
     ll t=0;
     for( ; number!= 0 ; )
   {
      t = t * 10;
      t = t + number%10;
      number = number/10;
   }

   return t;
}
ll a[1000001];
int main()
{
  freopen("A-small-attempt2.in", "r",stdin);
     freopen("cc-op1.txt", "w" ,stdout);
    ll i;
       for(i=1;i<20;i++)
          a[i]=i;


       for(i=20;i<=1000000;i++)
       {

         if(i%10==0)
         a[i]=a[i-1]+1;
         else
         {
         	ll tmp=rev(i);
         	a[i]=1+min(a[i-1],tmp<i?a[tmp]:1000001);
         }
       }
     int t,c;
     s(t);
     for(c=1;c<=t;c++)
     {
       ll n,i;
       sl(n);

        P("Case #%d: %lld\n",c,a[n]);
     }

}

