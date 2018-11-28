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
ll X,R,C;
int main()
{   freopen("rk.txt","r",stdin);
	freopen("output.txt","w",stdout);
    ll T,n,m,i;
    cin>>T;
    for(ll k=1;k<=T;k++)
	 {
		scanf("%d %d %d", &X,&R,&C);
		ll temp = R*C;
		if(X == 1)
		{
			printf("Case #%d: GABRIEL\n", k);
		}else if(X == 2)
		{
			if(temp%2 == 0)
			{
				printf("Case #%d: GABRIEL\n", k);
			}
			else
			{
				printf("Case #%d: RICHARD\n", k);
			}
		}
		else if(X == 3)
		{
			if(temp == 6 || temp == 9 || temp == 12)
			{
				printf("Case #%d: GABRIEL\n", k);
			}
			else
			{
				printf("Case #%d: RICHARD\n", k);
			}
		}
		else
		{
			if(temp == 12 || temp == 16)
			{
				printf("Case #%d: GABRIEL\n", k);
			}
			else
			{
				printf("Case #%d: RICHARD\n", k);
			}
		}
	}
    fclose(stdout);
    return 0;
}


