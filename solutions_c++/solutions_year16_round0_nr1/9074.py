#include <bits/stdc++.h>
using namespace std;

#define ll long long

void solve(int N)
{
	int n;
	scanf("%d", &n);

	if(n==0)
	{
		printf("Case #%d: INSOMNIA\n", N);
		return;
	}

	ll r;
	int ct = 0;
	int j = 1;

	bool stat[10];
	for(int i = 0 ; i<10 ; i++)
	{
		stat[i] = false;
	}
	int rem;
	while(ct!=10)
	{
		r = (ll)(n)*(ll)(j);
		while(r>0)
		{
			rem = r%10;
			r/=10;
			if(!stat[rem])
			{
				ct++;
				stat[rem] = true;
			}

		}

		j++;
	}

	j--;

	r = (ll)(n)*(ll)(j);

	printf("Case #%d: %lld\n",N, r);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;

	int i =1;

	while(t--)
	{
		solve(i);
		i++;
	}
}