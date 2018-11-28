#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
	int t; cin >> t;
	char c;
	
	for (int i = 1; i <= t; i++) 
	{
		string s; cin >> s;
		c = s[0];
		int count = 0;

		if (s[s.size() - 1] == '-') count++;

		for (int j = 1; j < s.size(); j++)
		{
			if (s[j] != c) {
				count++;
				c = s[j];
			}
		}
		
		cout <<  "Case #" << i << ": " << count << "\n";
	}

	return 0;
}