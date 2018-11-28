#include <iostream>
#include <cstdio>

using namespace std;

bool u[10];

int check(int x)
{
	if (!x) return -1;
	for (int i = 0;i < 10; i ++) u[i] = false;
	int d = 10;
	for (int i = x; ; i += x)
	{
		int j = i;
		while (j)
		{
			int t = j % 10;
			if (!u[t]) u[t] = true, d --;
			j /= 10;
		}
		if (!d) return i;
	}
}

int main()
{
	freopen ("b.in", "r", stdin);
	freopen ("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++)
	{
		int n;
		cin >> n;
		n = check(n);
		cout << "Case #"<< i << ": "; 
		if (n == -1) cout << "INSOMNIA" << endl;
		else cout << n << endl;
	}
	return 0;
}