#include<bits/stdc++.h>

using namespace std;
typedef long long int ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;

#define all(x) (x).begin(),(x).end()
#define pb push_back
#define mp make_pair
#define tr(c,it) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rd(x) scanf("%lld",&x)
#define wr(x) printf("%lld\n",x)
#define rep(i,a,b) for(i=a;i<b;i++)
#define pi 3.141592653589793238462643383279
#define f first
#define s second
#define MOD 1000000007     // 10^9+7
#define INF 1000000008     // 10^9+8



int main()
{
 // freopen("A-large.in","r",stdin);
 // freopen("output.txt","w",stdout);

ll t,p,n,flag,i,j,temp1,temp2,k,ans;
rd(t);

//while(t--)
   rep(p,1,t+1)
   {
   bool arr[10];
   memset(arr,false,sizeof arr);
     rd(n);
     if(n==0)
     {
       printf("Case #%lld: INSOMNIA\n",p);
       continue;
     }
     flag=0;
     for(i=1;;i++)
     {
       temp1=n*i;
       temp2=temp1;
       while(temp2>0)
       {
         k=temp2%10;
         arr[k]=true;

         rep(j,0,10)
         {
           if(!arr[j])
            break;
         }
         if(j==10)
           {
             flag=1;
             ans=temp1;
             break;

           }

       // if()
         temp2/=10;
       }
       if(flag)
        break;

     }

     printf("Case #%lld: %lld\n",p,ans);

   }

   return 0;
}
