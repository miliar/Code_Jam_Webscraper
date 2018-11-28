#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);

	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		string str;
		cin >> str;
		int count = 0;
		bool first = true;
		for (int i=0;i<str.size();i++) {
			if (str[i] == '-') {
				while (str[i] == '-' && i < str.size()) {
					str[i] = '+';
					i++;
				}
				count++;
				if (!first)
					count++;
			}
			first = false;
		}

		cout << "Case #" << (q + 1) << ": " << count << endl;
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}