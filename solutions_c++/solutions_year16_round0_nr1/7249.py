#include<bits/stdc++.h>

using namespace std;
#define ll long long int
int main()
{
	
    freopen("largeInput.txt","r",stdin);
    freopen("largeOutput.txt","w",stdout);
	int t;
	cin >> t;
	for(int test = 1; test <= t; test ++)
	{
		ll n;
		cin >> n;
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n",test); 
			continue;
		}
		map<int, ll> m;
		ll pro = n, iter = 1;
		while(m.size() != 10)
		{
			iter ++;
			ll temp = pro;
			for(; temp; temp /= 10)
			{
				m[temp % 10] ++;
//				cout << "Digit : " << temp % 10 << " m[digit] : " << m[temp%10] << " m.size " << m.size() << '\n';
			}
			pro = iter*n;
		}
		printf("Case #%d: %lld\n",test,(iter - 1) * n);
	}
}
