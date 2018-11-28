#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("C:/1.txt", "r", stdin);
	freopen("C:/2.txt", "w", stdout);
	int ttt;
	cin >> ttt;
	vector<long long> great;
	for (long long x = 1; x <= 10000001; ++x)
	{
		long long u = x;
		string e;
		while (u) e+='a'+u%10, u/=10;
		string ee = e;
		reverse(e.begin(), e.end());
		if (e==ee)
		{
			long long u = x * x;
			string e;
			while (u) e+='a'+u%10, u/=10;
			string ee = e;
			reverse(e.begin(), e.end());
			if (e==ee) great.push_back(x * x);
		}
	}
	for (int go=1;go<=ttt;++go)
	{
		cout << "Case #" << go << ": ";
		long long a, b;
		cin >> a >> b;
		long long ans=0;
		for (long long x : great) if (a<=x && b>=x) ans++;
		cout << ans << endl;
	}
	return 0;
}
