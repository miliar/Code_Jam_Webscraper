#include <iostream>
#include <string>

using namespace std;

int maxn = 1005;

int n;
string s;
int _t;


int main()
{
	cin >> _t;
	for (int _i = 0; _i < _t; ++_i)
	{
		cin >> n;
		cin >> s;
		int ans = 0;
		int t = 0;
		for  (int i = 0; i <= n; ++i)
		{
			if (i > t)
			{
				ans += i - t;
				t = i;
			}
			t += s[i] - '0';
		}
		cout << "Case #" << _i + 1 << ": " <<  ans << endl;
	}
	return 0;
}