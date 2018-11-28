#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<vpii> vvpii;
typedef vector<vpll> vvpll;
typedef vector<vl> vvl;
typedef vector<string> vs;
typedef unsigned long long ull;

#define rloop(i,a,b) for(i=a-1;i>=b;i--)
#define loop(i,a,b) for(i=a;i<b;i++)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define gc getchar   
#define rz resize
#define all(x) x.begin(),x.end()
#define sz size

double rd()
{
	double ret = 0.0;
	char c = gc();
	while( (c<'0' || c>'9') && c!='.') 
		c = gc();
	while(c>='0' && c<='9') 
	{
		ret = 10 * ret + c - 48;
		c = gc();
	}
	if (c=='.')
	{
		c = gc();
		ll ten = 10;
		while(c>='0' && c<='9') 
		{
		  ret += (double)(c-48)/(ten*1.0);
		  ten *= 10;
		  c = gc();
		}	
	}
	return ret;
}

int ri()
{
	char c = gc();
	while((c<'0' || c>'9') && c!='-')
		c = gc();
	int ret = 0, neg = 1;
	if(c == '-')
	{
		neg = -1;
		c = gc();
	}
	while(c>='0' && c<='9')
	{
		ret = 10 * ret + c - 48;
		c = gc();
	}
	return ret * neg;
}

ll rl()
{
	char c = gc();
	while((c<'0' || c>'9') && c!='-')
		c = gc();
	ll ret = 0, neg = 1;
	if(c == '-')
	{
		neg = -1;
		c = gc();
	}
	while(c>='0' && c<='9')
	{
		ret = 10 * ret + c - 48;
		c = gc();
	}
	return ret * neg;		
}

string rs()
{
	char c = gc();
	while(c=='\n' || c==' ')
		c=gc();
	string ret="";
	while(c!=10 && c!=' ')
	{
		ret+=c;
		c=gc();
	}
	return ret;
}

char rc()
{
	char c = gc();
	while(c=='\n' || c==' ')
		c=gc();
	return c;
}

vector <string> sols;

ll check_string(string &s)
{
	string t = s, a;

	ll i, j;
	while(t.size() > 1)
	{
		a.rz(0);
		loop (i, 0, t.size())
		{
			if (t[i] == 'R')
			{
				if (t[i + 1] == 'R')
					return 0;
				if (t[i + 1] == 'P')
					a.pb('P');
				else
					a.pb('R');
			}
			else if (t[i] == 'P')
			{
				if (t[i + 1] == 'P')
					return 0;
				if (t[i + 1] == 'R')
					a.pb('P');
				else
					a.pb('S');
			}
			else
			{
				if (t[i + 1] == 'S')
					return 0;
				if (t[i + 1] == 'P')
					a.pb('S');
				else
					a.pb('R');
			}
			i++;
		}
		t = a;
	}
	return 1;
}

void f(string a, ll l, ll r)
{
	ll i;
	char q;
	if (l == r)
	{
		if(check_string(a))
		{
			sols.pb(a);
			return;
		}
	}
	else
	{
		for (i = l; i <= r; i++)
		{
			q = a[l];
			a[l] = a[i];
			a[i] = q;

			f(a, l+1, r);
		
			q = a[l];
			a[l] = a[i];
			a[i] = q;
		}
	}

}

int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t = rl(), caseno = 0;
	while (t--)
	{
		caseno++;
		ll n = rl(), r = rl(), p = rl(), s = rl(), i, j, k;
		string x = "";
		while (p--)
			x.pb('P');
		while (r--)
			x.pb('R');
		while (s--)
			x.pb('S');
		cout << "Case #" << caseno << ": ";
		f(x, 0, x.size() - 1);
		if (sols.size() != 0)
		{
			sort(all(sols));
			cout << sols[0] << endl;
			sols.rz(0);
		}
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}