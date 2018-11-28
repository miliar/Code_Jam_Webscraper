#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int i = 1; i <= T; ++i) {
		string s;
		cin >> s;

		string last_string = "";
		last_string.push_back(s[0]);

		for(int j = 1; j < s.size(); ++j) {
			if(s[j] < last_string.front())
				last_string.push_back(s[j]);
			else
				last_string.insert(0, s.substr(j, 1));
		}

		cout << "Case #" << i << ": " << last_string << endl;
	}

	return 0;
}