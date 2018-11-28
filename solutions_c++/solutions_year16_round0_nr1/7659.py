#include <bits/stdc++.h>

using namespace std;

void fun(long long num)
{
	bool present[10] = {false};
	int count = 0;
	for(int i = 1; i <= 10000; i++)
	{
		long long n = i * num;
		while(n != 0)
		{
			int r = n%10;
			if(!present[r])
			{
				present[r] = true;
				count++;
			}
			n /= 10;
		}
		if(count >= 10)
		{
			cout << i * num << endl;
			return;
		}
	}
	cout << "INSOMNIA" << endl;

}

inline void solve()
{
	int n;
	cin >> n;
	fun(n);
}

int main()
{
	int t, i;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
    return 0;
}