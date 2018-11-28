#include<bits/stdc++.h>
#define sc(x) scanf("%lld", &x)
#define pf printf
#define ll long long int
using namespace std;
ll t, n;
set<int> st;
int main()
{
	sc(t);
	static int k = 1;
	while(t--)
	{
		sc(n);
		ll cnt = 0;
		st.clear();
		pf("Case #%d: ", k);
		k++;
		if(n>0)
		{
			ll i = 1, pdt = 1;
			while(cnt != 10)
			{
				pdt = i*n; i++;
			    ll tp =pdt;
			   while(tp)
			   {
			   	    int j = tp%10;
			   	    tp/=10;
			   	    
			   	     if(st.find(j)==st.end())
					 {
					 	st.insert(j);
					 	cnt++;
					 }
			   }	
			}
			pf("%lld\n", pdt);
		}
		else
		{
			pf("INSOMNIA\n");
		}
	}
}
