#include <iostream>
using namespace std;

int work()
{
	int n;
	cin >> n;
	string a;
	cin >> a;
	int now = 0, ans = 0;
	for (int i = 0; i <= n; ++ i)	if (a[i] != '0')
	{
		if (now < i)	ans += i - now, now = i;
		now += a[i] - '0';
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++ t)
	{
		cout << "Case #" << t << ": " << work() << endl;
	}
	return 0;
}