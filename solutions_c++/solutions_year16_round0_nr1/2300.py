// Author: thecodekaiser
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void func(ll num, vector<bool> & flag, int & rem)
{
	while(num > 0)
	{
		int dig = num % 10;
		if(flag[dig] == false)
		{
			flag[dig] = true;
			rem--;
		}

		num /= 10;
	}
	return;
}

void solve(int CS)
{
	ll num;
	cin >> num;

	if(num == 0)
		printf("CASE #%d: INSOMNIA\n", CS);
	else
	{
		int rem = 10;

		vector<bool> flag(10, 0);
		ll cnt = 1;
		func(num * cnt, flag, rem);

		while(rem > 0)
		{
			cnt++;

			func(num * cnt, flag, rem);
		}

		printf("CASE #%d: %lld\n", CS, num * cnt);		
	}
	return;
}

int main()
{
	int t, CS = 1;
	cin >> t;

	while(t--)
	{
		solve(CS++);
	}

	return 0;
}