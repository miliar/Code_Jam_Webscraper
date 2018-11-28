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
int p[1000001];
int main()
{
      freopen("B-large.in", "r",stdin);
     freopen("B-op-large.txt", "w" ,stdout);
     int t,c;
     s(t);
     for(c=1;c<=t;c++)
     {
         int d,i;
         s(d);

         int mx=0,mi=-1;
         for(i=1;i<=d;i++)
         {
           	s(p[i]);
         	     if(p[i]>mx)
         	     {
         		     mx=p[i];
         		     mi=i;
         	     }
         }
         int q,r,cnt=0,j;
         int ans=mx;
         for(i=mx;i>=1;i--)
         {
              cnt=0;
              for(j=1;j<=d;j++)
              {
                   if(p[j]>i)
                   {
                       q=p[j]/i;
                       r=p[j]%i;

                       if(r!=0)
                        cnt+=q;
                       else
                         cnt+=q-1;





                   }
              }


              ans=min(ans,i+cnt);

         }
      P("Case #%d: %d\n",c,ans);
     }


}
