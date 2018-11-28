#include <string>
#include <iostream>

using namespace std;

int main() {
	int t; cin >> t;

	for (int i = 0; i < t; ++i)
	{
		string line; cin >> line;
		while (line.back() == '+') {
			line.pop_back();
		}
		int count = 0; 
		if (line.length() > 0) {
			count++;
			char prev = line[0];
			for (auto c : line)
			{
				if (c != prev)
					count ++;
				prev = c;
			}
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}