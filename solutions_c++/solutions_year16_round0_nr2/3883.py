//B.cpp

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t) {
		string s;
		cin >> s;

		char curr = s[0];
		int times = 1;
		for (int i = 1; i < s.length(); ++i)
		{
			char c = s[i];
			if (c != curr) {
				curr = c;
				times ++;
			}
		}

		cout << "Case #" << t+1 << ": " << ( (curr=='-')?times:times-1 ) << endl;
	}

	return 0;
}
