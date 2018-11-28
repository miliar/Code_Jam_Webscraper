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
	ll t, n, i, j, k, x, num, c, m;
	sl(t);
	rep(i, t)
	{
		sl(n);
		if(n == 0)
		{
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		ll hash[10] = {0};
		j = 1;
		while(1)
		{
			x = n * (j++);
			num = x;
			while(x > 0)
			{
				m = x % 10;
				x = x / 10;
				hash[m]++;
			}
			if(hash[0] >= 1 && hash[1] >= 1 && hash[2] >= 1 && hash[3] >= 1 && hash[4] >= 1 && hash[5] >= 1 && hash[6] >= 1 && hash[7] >= 1 && hash[8] >= 1 && hash[9] >= 1)
			{
				break;
			}
		}
		cout << "Case #" << i+1 << ": " << num << endl;
	}	
    rt 0;
}