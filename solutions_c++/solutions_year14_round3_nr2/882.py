#include <iostream>
#include <string>
#include <vector>

using namespace std;

int check(string &s)
{
	int count[26] = {0};
	char prev = 0;

	for (int i = 0; i < s.length(); i++) {
		char curr = s[i];

		if (prev != curr)
			count[curr - 'a']++;

		prev = curr;
	}

	for (int i = 0; i < 26; i++) {
		if (count[i] > 1)
			return 0;
	}

	return 1;
}

int solve(string s, vector<string>& vec) {
	if (vec.size() == 0)
		return check(s);

	int count = 0;

	for (int i = 0; i < vec.size(); i++) {
		string s2 = s + vec[i];
		vector<string> vec2(vec);

		vec2.erase(vec2.begin() + i);
		count += solve(s2, vec2);
	}

	return count;
}

int main()
{
	int cases;

	std::cin >> cases;

	for (int c = 1; c <= cases; c++) {
		int cars;

		cin >> cars;

		vector<string> vec;

		for (int i = 0; i < cars; i++) {
			string s;

			cin >> s;
			vec.push_back(s);
		}

		int count = solve("", vec);

		cout << "Case #" << c << ": " << count << endl;
	}

	return 0;
}
