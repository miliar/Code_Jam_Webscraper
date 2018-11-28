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

std::vector<pair<char,int> > v;

int main()
{
	int i, j;

	int cases;

	int caseNo = 1;

	si(cases);

	wl(cases)
	{
		int n, tot = 0;

		v.clear();

		si(n);

		fl(i,0,n)
		{
			int temp;
			si(temp);
			tot += temp;
			v.PB(MP(temp,i));
		}

		cout<<"Case #"<<caseNo<<": ";
		caseNo++;

		while(v.SZ() > 2)
		{
			sort(v.begin(), v.end());
			reverse(v.begin(), v.end());

			printf("%c ",char(v[0].second+'A') );

			v[0].first--;
			tot--;

			if(v[0].first == 0)
				v.erase(v.begin());
		}

		if(v.SZ() != 2)
		{
			cout<<"ERROR!!";
			return 1;
		}

		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		while(v[0].first != 0)
		{
			printf("%c",char(v[0].second+'A') );
			printf("%c ",char(v[1].second+'A') );

			v[0].first--;
		}
			
		//cout<<char(v[0].second+'A')<<char(v[1].second + 'A');
		nline;


	}



	return 0;
}
/*
	Powered by Buggy Plugin
*/
