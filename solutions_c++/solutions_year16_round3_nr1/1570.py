#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
	ll t, caseno = 0;
	cin>>t;
	while (t--)
	{
		caseno++;
		ll n, k, i, sum = 0, j, index;
		cin>>n;
		vector<ll> a;
		for (i=0; i<n; ++i)
		{
			cin>>k;
			a.push_back(k);
			sum += a.back();
		}
		cout << "Case #" << caseno << ": ";
		while (sum--)
		{
			j = -1;
			index = 0;
			for(i=0; i<n; ++i)
			{
				if (a[i] > j)
				{
					j = a[i];
					index = i;
				}
			}
			a[index]--;
			cout << char(65 + index);

			j = -1;
			index = 0;
			for(i=0; i<n; ++i)
			{
				if (a[i] > j)
				{
					j = a[i];
					index = i;
				}
			}
			//cout << "sum = " << sum << "index=" << index << "a[in]="<< a[index] << endl;
			if (sum != 0 && 2 * a[index] > sum)
			{
				cout << char(65 + index);
				a[index]--;
				sum--;
			}
			cout << " ";
		}
		cout << endl;
	}
	return 0;
}