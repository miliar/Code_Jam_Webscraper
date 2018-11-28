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

		int k, c,s;
		cin >> k >> c >> s;

		for (int i = 1; i <= k; ++i)
			cout << i << " ";
		cout << endl;
	}

	return 0;
}