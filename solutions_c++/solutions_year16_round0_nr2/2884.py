#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int c;
	cin >> c;
	for (int cc = 1; cc <= c; cc++) {
		string s;
		cin >> s;
		s += "+";
		int cnt = 0;
		for (int i = 1; i < s.length(); i++)
			if (s[i - 1] != s[i])
				cnt++;
		cout << "Case #" << cc << ": " << cnt << endl;
	}
}