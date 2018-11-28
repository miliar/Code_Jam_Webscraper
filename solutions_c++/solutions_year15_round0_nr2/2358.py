#include<bits/stdc++.h>
#define Mod 1000000007
using namespace std;
#define ll int
#define gc getchar
#define pc putchar

inline ll getn()
{
  ll n=0, c=gc();

  while(c < '0' || c > '9') c = gc();

  while(c >= '0' && c <= '9')
   n = (n<<3) + (n<<1) + c - '0', c = gc();

  return n;
}
inline void fastWrite(ll a)
{
   char snum[20];
   ll i=0;

   do
    {
     snum[i++]=a%10+48;
     a=a/10;
   }while(a!=0);

   i=i-1;

   while(i>=0)
    pc(snum[i--]);

   pc('\n');
}
int main()
{   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    ll t,n,rk[1003],i,j,k,increm,l,count=0;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
	{
       scanf("%d",&n);
        l=0;
        for(i=0;i<=n-1;i++)
		{
            scanf("%d",&rk[i]);
            l=max(l,rk[i]);
        }
        count=1000000;
        for(i=1;i<=l;i++)
		{
            increm=0;
            for(j=0;j<=n-1;j++)
			{
                if(rk[j]%i==0) increm+=(rk[j]/i)-1;
                else{increm+=rk[j]/i;}
            }
            count=min(count,increm+i);
        }
       cout<<"Case #"<<k<<": "<<count<<endl;
       
    }
    fclose(stdout);
    return 0;
}


