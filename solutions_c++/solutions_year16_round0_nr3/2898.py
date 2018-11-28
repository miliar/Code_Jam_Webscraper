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

ll primecheck(ll n)
{
ll i;
   if(n%2==0)
    return 2;

   ll k=sqrt(n);
   for(i=3;i<=k;i+=2)
   {
     if(n%i==0)
      return i;
   }
   return -1;
}


int main()
{
  freopen("C-small-attempt0.in","r",stdin);
  freopen("output.txt","w",stdout);

ll t,p,n,j,temp1,temp2,z,i,temp3,k,b,x,newnum,y,c,m,o;

rd(t);
   for(p=1;p<t+1;p++)
   {
    // rd(t);
     rd(n);
     rd(j);

     temp1=pow(2,15)+1;
     temp2=pow(2,16)-1;
     z=0;
     printf("Case #1:\n");
     for(i=temp1;i<temp2;i+=2)
     {
        ll num[16];
        ll factors[11];
        factors[0]=factors[1]=0;
        temp3=i;
        k=15;
        while(temp3>0)
        {
          num[k]=temp3%2;
          temp3/=2;
          k--;
        }

        for(b=2;b<11;b++)
        {
          x=0;
          newnum=0;
          for(y=15;y>=0;y--)
          {
            newnum+= num[y]*pow(b,x);
            x++;
          }

          c=primecheck(newnum);
          if(c== -1)
           break;
          else
           {
             factors[b]=c;
           }

        }

        if(b==11)
         {
           z++;
           for(m=0;m<16;m++)
             printf("%lld",num[m]);
           cout<<" ";
           for(o=2;o<11;o++)
            printf("%lld ",factors[o]);

           printf("\n");
          // break;
         }

         if(z==j)
          break;
   }

   return 0;
}
}
