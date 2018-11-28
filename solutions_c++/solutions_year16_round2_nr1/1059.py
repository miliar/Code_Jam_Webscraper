#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;
string dig[] = { "ZERO", "ONE", "WTO", "RTHEE", "UFOR", "VFIE", "XSI", "SEVEN", "GEIHT", "INNE" };

bool findl(string& s, const int ind)
{
	for (auto c : dig[ind])
	{
		if (find(s.begin(), s.end(), c) == s.end())
			return false;
	}
	for (auto c : dig[ind])
	{
		auto it = find(s.begin(), s.end(), c);

		s.erase(it);
	}

	return true;
}

void testcase()
{
	string s;

	cin >> s;

	vector<int> res(10, 0);

	int order[] = { 0,2,6,8,7,5,4,3,1,9 };

	int curind = 0;
	while (s.size() > 0)
	{
		while (s.size() > 0 && findl(s, order[curind]))
			res[order[curind]]++;
		curind++;
	}

	for (int i = 0; i < 10; ++i)
		for (int j = 0; j < res[i]; ++j)
			cout << i;

	cout << endl;
} 

int main()
{
  int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
    cout << "Case #" << i + 1 << ": ";
		testcase();
	}
	
	return 0;
}