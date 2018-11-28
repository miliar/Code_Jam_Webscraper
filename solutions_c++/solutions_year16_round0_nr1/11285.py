/*Useful info
__builtin_popcount(n) counts number of active bits.
__builtin_popcountl(n) for long and ll for long long

to_string(n): Converts a number from int to string*/

//My shortcuts
#include<bits/stdc++.h>
#define ll long long int
#define sf(n) scanf("%d",&n);
#define sf2(a,b) scanf("%d %d",&a,&b);
#define sf3(a,b,c) scanf("%d %d %d",&a,&b,&c);
#define sf4(a,b,c,d) scanf("%d %d %d %d",&a,&b,&c,&d);
#define sfl(n) scanf("%lld",&n);
#define sful(n) scanf("%llu",&n);
#define pf(n) printf("%d",n);
#define pfl(n) printf("%lld",n);
#define pful(n) printf("%llu",n);
#define ps printf(" ");
#define pn printf("\n");
#define put(a) printf("%s",a);
#define cut(n,val) memset(n,val,sizeof(n));
#define pub push_back()
#define ln size()
#define mpr make_pair()
#define bpop(n) __builtin_popcount(n)
#define fo(in,out) for(int i=in;i<out;i++)
#define st(n) to_string(n) //Works only in c++11
const long long int mod=1e9+7;
using namespace std;
//FAST IO->
//Advisable to use scanf and printf since it passes most time limits.
/*inline void readll(ll &a)
{
  register int c;
  a = 0;
  do c = getchar_unlocked(); while (c < '0');
  do{
    a = (a << 1) + (a << 3) + c - '0';
    c = getchar_unlocked();
  } while (c >= '0');
}
inline void printll(ll a)
{
  int s[25], t = -1;
  do
  {
    s[++t] = a % 10 + '0';
    a /= 10;
  } while (a > 0);
  while (t >= 0)putchar_unlocked(s[t--]);
  putchar_unlocked('\n');
}
inline ll readstr(char s[])
{
  register ll i = 0, c;
  do c = getchar_unlocked(); while (c < '0' || c > '9');
  do{
    s[i++] = c;
    c = getchar_unlocked();
  } while (c >= '0' && c <= '9');
  s[i] = '\0';
  return i;
}*/
//Functions->

//Driver program->
int main()
{
	int t;
	sf(t);
	for(int j=0;j<t;j++)
	{
		bool num[11];
		cut(num,false);
		
		ll n;
		sfl(n);
		
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",j+1);
			continue;
		}
		
		ll g,f;
		g=n;
		f=n;
		while(1)
		{
			int c=0;
			while(f!=0)
			{
				int k=f%10;
				num[k]=true;
				f=f/10;
			}
			
			for(int i=0;i<10;i++)
				if(num[i]==true)
					c++;
					
			if(c==10)
			{
				printf("Case #%d: %lld\n",j+1,n); 
				break;
			}
			n=n+g;
			f=n;
		}
	}
	return 0;
}
