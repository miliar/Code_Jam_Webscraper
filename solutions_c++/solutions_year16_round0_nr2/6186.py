/*
--+-+--
+++-+--
---++--
+++++--
--+++++
+++++++
2 + 2 + 1 = 2*(n-1)+1 = 2*n-1

+--+-+--
-+++-+--
++++-+--
----++--
++++++--
------++
++++++++
1+2+2+1 = 2*(n-1)+2 = 2*n
* */

#include<bits/stdc++.h>

typedef long long int ll;

char s[200];

int main()
{
	ll nt;
	scanf(" %lld",&nt);
	for(ll t=1; t<=nt; t++)
	{
		printf("Case #%lld: ",t);
		scanf(" %s",s);
		bool ini_ = (s[0]=='-');
		ll n_ = ini_;
		for(int i=1; s[i]; i++)
			n_ += ll(s[i]=='-' and s[i-1]=='+');
		printf("%lld\n",2*n_-ll(ini_));
	}
	return 0;
}
