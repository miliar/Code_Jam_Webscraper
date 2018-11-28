#include <iostream>
#include <set>
#include <string>
#include <sstream>
using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int i = 1;  i < T+1; i++)
	{
		int j;
		cin >> j;
		set<int> numSeen;
		int k = 0;
		bool sleep = false;
		while (true)
		{
			k = k + j;
			if (k == 0)
			{
				break;
			}
			
			//parse digits
			string s = to_string(k);
			for (int n = 0; n < s.length(); n++)
			{
				int tmp = stoi(s.substr(n, 1));
				numSeen.insert(tmp);
			}
			if (numSeen.size() == 10)
			{
				cout << "Case #" << i << ": " << k << endl;
				sleep = true;
				break;
			}
		}
		if(!sleep)
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	}

}