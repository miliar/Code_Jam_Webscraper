#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
#include <sstream>
#include <iomanip>

#include <limits.h>
#include <stdlib.h>

using namespace std;

string chars[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char specials[] = {'Z', '\0', 'W', '\0', 'U', 'F', 'X', 'S', 'G', 'I'};
char specials2[] = {'\0', 'N', '\0', 'T', '\0', '\0', '\0', '\0', '\0', '\0'};

int main() {
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; ++tc)
	{
		string s;
		cin >> s;

		short counts[10];
		for (int i=0; i<10; ++i)
		{
			counts[i] = 0;
		}
		for (int i=0; i<10; ++i)
		{
			if (specials[i])
			{
				if (s.find(specials[i]) != string::npos)
				{
					for (auto c : chars[i])
					{
						auto index = s.find(c);
						s.erase(index, 1);
					}
					++counts[i];
					--i;
				}
			}
		}
		for (int i=0; i<10; ++i)
		{
			if (specials2[i])
			{
				if (s.find(specials2[i]) != string::npos)
				{
					for (auto c : chars[i])
					{
						auto index = s.find(c);
						s.erase(index, 1);
					}
					++counts[i];
					--i;
				}
			}
		}
		cout << "Case #" << tc << ": ";
		for (int i=0;i<10;++i)
			for (int j=0;j<counts[i];++j)
				cout << i;
		cout << endl;
	}

	return 0;
}