//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)

#define si(n) scanf("%d", &n)
#define sll(l) scanf("%lld",&l)
#define ss(s) scanf("%s", s)
#define sc(c) scanf("%c", &c)
#define sd(f) scanf("%lf", &f)

#define pi(n) printf("%d\n", n)
#define pll(l) printf("%lld\n", l)
#define ps(s) printf("%s\n", s)
#define pc(c) printf("%c\n", c)
#define pd(f) printf("%lf\n", f)

#define debug(x) cout<<"\n#("<<x<<")#\n"
#define nline printf("\n")

#define mem(a,i) memset(a,i,sizeof(a))

#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define PB push_back
#define SZ size
#define MP make_pair
#define fi first
#define sec second

int mark[11];

int main()
{
	ll i, j;

	int cases;
	int caseNo = 1;

	si(cases);

	wl(cases)
	{

		mem(mark,0);
		ll ans = -1;

		ll n;
		sll(n);


		fl(i,1,1000006)
		{
			ll ele = i * n;
			/*if(n != 0)
				cout<<ele<<" ";*/
			ll sum = 0;

			while(ele)
			{
				ll dig = ele % 10;
				mark[dig] = 1;
				ele /= 10;
			}

			fl(j,0,10)
			{
				sum += mark[j];
			}

			if(sum == 10)
			{
				ans = i * n;
				break;
			}
		}

		cout<<"Case #"<<caseNo<<": ";
		caseNo++;

		if(ans == -1)
		{
			cout<<"INSOMNIA";
		}
		else
		{
			cout<<ans;
		}
		nline;

	}


	return 0;
}
/*
	Powered by Buggy Plugin
*/
