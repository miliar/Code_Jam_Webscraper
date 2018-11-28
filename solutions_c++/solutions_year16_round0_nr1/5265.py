#include <iostream>
#include <vector>

typedef long long ll;

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int q = 1; q <= t; ++q)
	{
		ll n, s = 0;
		cin >> n;

		vector<bool> v(10);
		int cnt = 0;
		for(int i = 0; i < 1e7 && cnt < 10; ++i)
		{
			s += n;
			ll ss = s;
			while(ss)
			{
				int last = ss % 10;
				ss /= 10;
				if(!v[last])
				{
					v[last] = true;
					++cnt;
				}
			}
		}

		cout << "Case #" << q << ": ";
		if(cnt == 10)
			cout << s << endl;
		else
			cout << "INSOMNIA" << endl;
	}
	return 0;
}