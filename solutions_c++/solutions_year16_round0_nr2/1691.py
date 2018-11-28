#include <iostream>
#include <string>

using namespace std;

int main()
{
	string line;
	int t;
	cin >> t;
	getline(cin, line);
	for (int i = 1; i <= t; i++)
	{
		getline(cin, line);
		int transitions = 0;
		char cchar = line[0];
		for (size_t j = 1; j < line.size(); j++)
		{
			if (cchar == line[j]) continue;
			transitions++;
			cchar = line[j];
		}
		if (cchar == '-') transitions++;
		cout << "Case #" << i << ": " << transitions << endl;
	}
}
