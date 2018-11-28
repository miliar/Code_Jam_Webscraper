#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		bool flag = false;
		int x, n, m;
		cin >> x >> n >> m;
		if(m < n) swap(n, m);
		if((x + 1) / 2 > n) flag = true;
		if((n * m) % x) flag = true;
		if(x == 4 && n == 2) flag = true;
		if(n * m < x) flag = true;
		if(x == 1) flag = false;
		cout << "Case #" << test+1 <<": " << (flag ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}