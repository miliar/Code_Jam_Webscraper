#include <iostream>
using namespace std;

const int N = 100;

inline bool chk(bool (&a)[10])
{
	for(int j = 0; j < 10; ++j)
	{
		if(!a[j]) return false;
	}
	return true;
}

int f(int n)
{
	if(n == 0) return 0;
	bool a[10] = {};
	for(int i = 1; i < N; ++i)
	{
		for(int t = i * n; t; t /= 10)
		{
			a[t % 10] = true;
		}
		if(chk(a)) return i * n;
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		int n;
		cin >> n;
		cout << "Case #" << i << ": ";
		int ans = f(n);
		if(ans)
		{
			cout << ans << endl;
		}
		else
		{
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}