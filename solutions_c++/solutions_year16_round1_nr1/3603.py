#include <iostream>

using namespace std;

int main()
{
	int t; cin >> t;
	string line;
	getline(cin, line);
	for (int i = 1; i <= t; i++)
	{
		getline(cin, line);
		string lw;
		lw.reserve(line.size());
		char last = line[0];
		lw.push_back(last);
		for (size_t j = 1; j < line.size(); j++)
		{
			if (line[j] >= last)
			{
				lw.insert(lw.begin(), line[j]);
				last = line[j];
			}
			else lw.push_back(line[j]);
		}
		cout << "Case #" << i << ": " << lw << endl;
	}
    return 0;
}
