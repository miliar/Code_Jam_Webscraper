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

		string s;
		cin >> s;


		int numGroups = 0;
		for (int i = 0; i < s.size(); )
		{
			int j = i;
			while (j < s.size() && s[j] == s[i])
				++j;
			i = j;
			++numGroups;
		}
		if (s[s.size()-1] == '+')
			--numGroups;
		cout << numGroups << endl;
	}

	return 0;
}