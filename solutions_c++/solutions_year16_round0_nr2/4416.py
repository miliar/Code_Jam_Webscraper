#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		cin >> s;
		if (s == "+")
			cout << "Case #" << (i+1) << ": " << 0 << "\n";
		else if (s == "-")
			cout << "Case #" << (i+1) << ": " << 1 << "\n";
		else {
			int count = 0;
			char current = s[0];
			for (int j = 0; j < s.size()-1; j++) {
				if (j == s.size() - 2) {
					if (current == '+' && s[j+1] == '-')
						count += 2;
					else if (current == '-' && s[j+1] == '-')
						count++;
					else if (s[j] == '-' && s[j+1] == '+')
						count++;
				} else {
					if (s[j+1] != current) {
						current = s[j+1];
						count++;
					}
				}
			}
			cout << "Case #" << (i+1) << ": " << count << "\n";
		}
	}
	return 0;
}
