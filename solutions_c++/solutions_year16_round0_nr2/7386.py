#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define ll long long
#define SIZE 100

int main()
{
	int t = 0;
	int caseN = 1;
	string input;
	getline(cin, input);
	t = stoi(input);

	while (t--)
	{
		getline(cin, input);
		ll sz = input.size();
		bool startPos = true;
		if (input[0] == '-') startPos = false;
		ll i = 0;
		ll output = 0;
		ll negtive_count = 0;
		while (i < sz)
		{
			if (input[i] == '-')
			{
				negtive_count++;
				while (i < sz && input[i] == '-') i++;
			}
			else
			{
				while (i < sz && input[i] == '+') i++;
			}
		}

		if (startPos) output = negtive_count * 2;
		else
			output = negtive_count * 2 - 1;

		cout << "Case #" << caseN << ": " << output << '\n';
		caseN++;
	}
}