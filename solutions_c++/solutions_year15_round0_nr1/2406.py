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
{   freopen("inp.txt","r",stdin);
	freopen("outputLarge.txt","w",stdout);
    ll t,n,m,i,k,count=0,temp;
    char str[1003];
    ll peo[1003];
    t=getn();
    for(i=1;i<=t;i++)
    {
        scanf("%d",&n);
		scanf("%s",str);
		for(k=0;k<=n;k++)
		{
			peo[k]=str[k]-48;
		}
		count=peo[0];
		temp=0;
		for(k=1;k<=n;k++)
		{
			if(count<k)
			{
				temp++;
				count++;
			}
			count+=peo[k];
		}
		printf("Case #%d: %d\n",i,temp);
    }
    fclose(stdout);
    return 0;
}


