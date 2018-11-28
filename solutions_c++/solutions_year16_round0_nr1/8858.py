#include <bits/stdc++.h>
using namespace std;

#define ll long long int

set <int> s;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("1large.out", "w", stdout);
    #endif // ONLINE_JUDGE
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;++j)
	{
		s.clear();
		ll n,i=1,temp,rem,res;
		scanf("%lld",&n);
		if(n==0)
			cout << "Case #" << j << ": "<< "INSOMNIA" <<endl;
		else
		{
			res = (ll)(i*n);
			temp = res;
			while(temp>0)
			{
				rem=temp%10;
				s.insert(rem);
				temp/=10;
			}
			while(s.size()!=10)
			{
				res = (ll)((i+1)*n);
				temp = res;
				while(temp>0)
				{
					rem=temp%10;
					s.insert(rem);
					temp/=10;
				}
				i++;
			}
			cout << "Case #" << j << ": "<< res <<endl;
		}
	}
}
