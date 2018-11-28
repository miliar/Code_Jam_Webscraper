    //ALL HAIL MEGATRON

using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define scanll(l) scanf("%lld", &l)
#define scanllu(u) scanf("%llu", &u)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define printll(l) printf("%lld\n", l)
#define printllu(u) printf("%llu\n", u)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int
#define PB push_back

ll has[10], ans[1000005];

bool see(ll x)
{
	ll y = x,z;
	while(y)
	{
		z = y%10;
		has[z]++;
		y/=10;
	}

	ll i;
	bool flag = 1;
	fl(i,0,10)
	{
		if(has[i]==0)
		{
			flag = 0;
			break;
		}
	}

	return flag;
}

void banao()
{
	ll i=1,j,n,cur;
	fl(j,1,1000005)
	{
		n = j;
		i = 1;
		cur = i*n;
		memset(has,0,sizeof(has));
		while(1)
		{
			if(see(cur))
			{
				ans[j] = cur;
				break;
			}
			i++;
			cur = i*n;
		}
	}
}


int main()
{
	int I,t;
	scan(t);
	banao();
	fl(I,1,t+1)
	{
		ll n,cur,i=1;
		scanll(n);

		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",I);
			continue;
		}
		
		printf("Case #%d: %lld\n",I,ans[n]);
	}
	return 0;
}
