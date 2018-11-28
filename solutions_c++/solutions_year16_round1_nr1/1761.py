#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i<numCases; i++)
	{
		string str;
		cin >> str;

		string res = "";
		res += str[0];
		for (int i = 1; i < str.size(); i++)
		{
			char tmp_start = res[0];
			if (str[i] >= tmp_start)
				res.insert(res.begin(), str[i]);
			else
				res += str[i];
		}
		
		cout << "Case #" << i + 1 << ": " << res << endl;
	}

	return 0;
}