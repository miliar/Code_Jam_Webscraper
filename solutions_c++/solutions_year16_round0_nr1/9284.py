#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

using namespace std;

int main()
{
	int found[10];
	ll t,n,i, total;
	cin >> t;
	for(int j=0; j<t; j++) 
	{
		cin >> n;
		if(n==0)
		{
			cout << "Case #" << j+1 << ": INSOMNIA" << endl;
			continue;
		}

		for(i=0; i<10; i++)
			found[i] = 0;
		int cnt = 0;
		total = 0;
		i = 0;
		while(1)
		{
			if(cnt==10)
				break;
			i++;
			total = n*i;
			while(total != 0)
			{
				if(found[total%10]==0)
				{
					found[total%10] = 1;
					cnt++;
				}
				total /= 10;

			}
		}

		cout << "Case #" << j+1 << ": " << n*i << endl;
	}
	return 0;
}