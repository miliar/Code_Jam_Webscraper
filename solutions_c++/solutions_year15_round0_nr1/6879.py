#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

typedef long long dlong;

dlong solve(vector<dlong> &dataset)
{
	dlong ans = 0;
	dlong total = 0;
	for (dlong i = 0; i < dataset.size(); i++)
	{
		total += dataset[i];
		dlong need = max(i + 1 - total, 0ll);
		ans += need;
		total += need;
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		dlong Smax;
		cin >> Smax;
		string str;
		cin >> str;
		dlong length = Smax + 1;
		vector<dlong> dataset(length);
		const char* head = str.c_str();
		for (int j = length - 1; 0 <= j; j--)
		{
			dataset[j] = head[j] - '0';
		}
		cout << "Case #" << i << ": " << solve(dataset) << endl;
	}
}