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
#define pcase(i) printf("Case #%d: ", i + 1)
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

string numtostr(ll n)
{
	string str = "";
	ll x;
	while(n > 0)
	{
		x = n % 10;
		n = n / 10;
		str = ((char)('0' + x)) + str;
	}
	rt str;
}

ll strtonum(string str)
{
	ll num = 0, i;
	rep(i, str.size())
	{
		num = num * 10 + (str[i] - '0');
	}
	return num;
}

int main()
{
	int t, n, i, num_stand, count, j;
	string str;
	s(t);
	rep(i, t)
	{
		s(n);
		ci(str);
		int arr[n + 1];
		rep(j, str.length())
		{
			arr[j] = str[j] - '0';
		}
		num_stand = 0;
		count = 0;
		rep(j, n + 1)
		{

			if(num_stand >= j)
			{
				num_stand += arr[j];
			}
			else
			{
				count += (j - num_stand);
				num_stand += (arr[j] + (j - num_stand));
			}
			//co(j);sp;co(num_stand);nl;

		}
		pcase(i);p(count);nl;
	}
	rt 0;
}