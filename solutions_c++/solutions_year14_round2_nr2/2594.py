#include <iostream>
#include <cstring>

using namespace std;
int main()
{
	int t, a, b, k;
	cin >> t;
	for(int i = 1;i <= t;++i)
	{
		cout << "Case #" << i << ": ";
		cin >> a >> b >> k;
		long long ans = 0;
		for(int j = 0;j < a;++j)
			for(int x = 0;x < b;++x)
			{
				//cout << j << ' ' << x << ' ' << (x&j) << ' ' << k << endl;
				if((x&j) < k and (x&j) >= 0)
				{
					//cout << j << ' ' << x << endl;
					ans++;
				}
			}
		cout << ans << endl;
	}
	return 0;
}