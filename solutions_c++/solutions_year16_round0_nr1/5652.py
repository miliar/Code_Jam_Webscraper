#include <iostream>
#include <algorithm>
#include <map>
#include <stack>
#include <time.h>
#include <vector>
#include <set>
#include <string>
#include <fstream>

using namespace std;

#define ll long long
#define pii pair<ll, ll>
#define endl "\n"


ifstream in("input.txt");
ofstream out("output.txt");

#define cin in
#define cout out
/**/

vector<int> dig(int n)
{
	vector<int> ans;
	while (n)
	{
		ans.push_back(n % 10);
		n /= 10;
	}

	return ans;
}

int main()
{
	ios_base::sync_with_stdio(0);

	int ttt;
	cin >> ttt;
	int t = 0;
	while (ttt--)
	{
		++t;
		cout << "CASE #" << t << ": ";

		int n;
		cin >> n;

		if (n == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;	
		}

		vector<int> c(10, 0);

		for (int i = 1; i <= 200; ++i)
		{

			vector<int> ans = dig(i * n);
			for (int j = 0; j < ans.size(); ++j)
				c[ans[j]] = 1;

			bool good = true;
			for (int j = 0; j < 10; ++j)
				if (c[j] == 0)
					good = false;

			if (good)
			{
				cout << i * n << endl;
				break;
			}
		}
	}

	return 0;
}