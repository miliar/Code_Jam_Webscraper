#include <iostream>
#include <string>
using namespace std;

int f(int n, string s)
{
	for(int i = 0; i <= n; ++i)
	{
		s[i] -= '0';
	}

	int ans = 0, sum = 0;
	for(int i = 0; i <= n; ++i)
	{
		if(!s[i]) continue;
		if(sum < i)
		{
			ans += i - sum;
			sum = i;
		}
		sum += s[i];
	}
	return ans;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int u = 1; u <= T; ++u)
	{
		int n, y;
		string s;

		cin >> n >> s;
		
		y = f(n, s);
		
		cout << "Case #" << u << ": " << y << endl;
	}
	return 0;
}