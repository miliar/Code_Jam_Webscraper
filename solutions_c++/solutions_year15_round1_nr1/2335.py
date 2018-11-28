#include<bits/stdc++.h>
#define Mod 1000000007
using namespace std;
#define ll long long int
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
ll rk[10000];
int main()
{   freopen("ram.txt","r",stdin);
	freopen("ans.txt","w",stdout);
    ll t,m,i,k;
    t=getn();
    for(k=1;k<=t;k++)
	{
        ll n,count=0,val=0,temp_max=0;
        n=getn();
        for(i=0;i<n;i++)
		{
            rk[i]=getn();
        }
        
        for(i=1;i<n;i++)
		{
            if(rk[i]-rk[i-1]<0)
			{
                count+=(rk[i-1]-rk[i]);
            }
            temp_max=max(temp_max,rk[i-1]-rk[i]);
        }
        for(i=0;i<n-1;i++)
		{
            if(rk[i]>=temp_max)
			   val+=temp_max;
            else 
			   val+=rk[i];
        }
        cout<<"Case #"<<k<<": "<<count<<" "<<val<<"\n";
    }
    fclose(stdout);
    return 0;
}


