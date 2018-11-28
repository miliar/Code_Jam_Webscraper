/* Copyright (c) 2015 Prateek Singhal */

#include <bits/stdc++.h>

#define ll long long
#define MOD 1000000007

#define s(n) scanf("%d",&n) 
#define sc(n) scanf("%c",&n)
#define sl(n) scanf("%lld",&n)
#define s64(n) scanf("%I64d",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s", n)
#define gc getchar()
#define gl(n) getline (cin,n)
#define ci(n) cin >> n

#define p(n) printf("%d",n) 
#define pl(n) printf("%lld",n) 
#define p64(n) printf("%I64d",n)
#define pd(n) printf("%lf", n)
#define ps(n) printf("%s", n)
#define nl printf("\n")
#define sp printf(" ")
#define pcase(i) printf("Case #%lld: ", i + 1)
#define pc(a) putchar(a)
#define co(n) cout << n

#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define rt return
#define nxtp next_permutation
#define bg begin()
#define end end()

#define strc(a, b) strcpy(a, b.c_str())
#define fill(a, v) memset(a, v, sizeof(a))
#define rev(n) reverse(n.bg, n.end)

#define rep(i, n) for(i = 0; i < n; i++)
#define _rep(i, a, b, c) for(i = a; i <= b; i = i + c)
#define repr(i, a, b, c) for(i = a; i >= b; i = i - c)

#define foreach(v, c) for( typeof( (c).begin()) v = (c).begin(); v != (c).end(); ++v)

using namespace std;

int main()
{
	ll t, n, i, j, f, c, f1;
	char ch; 
	string str;
	sl(t);
	rep(i, t)
	{
		ci(str);
		n = str.size();
		f = 0;
		c = 0;
		rep(j, n)
		{
			if(str[j] == '+')
			{
				f = 1;
				break;
			}
		}
		f1 = 0;
		if(f == 1)
		{
			rep(j, n)
			{
				ch = str[j];
				if(j == 0)
				{
					if(ch == '-')
						f1 = 1;
					else
						f1 = 2;
				}
				else if(str[j] == '-' && f1 == 2)
				{
					c++;
					f1 = 1;
				}
				else if(str[j] == '+' && f1 == 1)
				{
					c++;
					f1 = 2;
				}
			}
			if(str[n - 1] == '-')
				c++;
			cout << "Case #" << i+1 << ": " << c << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": 1" << endl;
		}
	}	
    rt 0;
}