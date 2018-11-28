#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;

int main(void)
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	
	ll t,n,tmp,i,prev,x;
	x=1;
	scanf("%llu",&t);
	while(x<=t)
	{
		set<ll> st;
		i=1;
		scanf("%llu",&n);
		if(n==0)
		{
		cout << "Case #" << x << ": " <<  "INSOMNIA\n";	
		x++;
		continue;
		}
		while(st.size()!=10)
		{
			tmp=i*n;
			prev=tmp;
			while(tmp)
			{
				st.insert(tmp%10);
				tmp/=10;
			}
			i++;
		}
		cout << "Case #" << x << ": " <<  prev << "\n";
		x++;
	
	}
	return 0;
}