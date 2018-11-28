#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <functional> // For less<> greater<>
#include <algorithm>

using namespace std;

bool isIn(char &c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main()
{
	int case_count;
	cin >> case_count;

	for (int i = 0; i < case_count; i++)
	{
		// Do whatever you want here
		string letter;
		cin >> letter;

		int n;
		cin >> n;

		// Call Solve function with your parameters
		cout << "Case #" << i + 1 << ": ";
		/* SOLVE */
		string temp = "";
		int total = 0;
		int k = 0;
		for (int i = 0; i < letter.size(); i++)
		{
			if (!isIn(letter[i]))
			{
				bool isCons = true;
				int j;
				if (i + n > letter.size())
					continue;
				for (j = i + 1; j < i + n; j++)
				{
					isCons &= !isIn(letter[j]);
					if (isCons == false)
						break;
				}

				if (isCons == true)
				{
					int count = (i + 1 - k) * (letter.size() - j + 1);
					total += count;
					k++;
				}
			}
		}
		cout << total;
		/* SOLVE */
		cout << endl;
	}

	getchar();
	return EXIT_SUCCESS;
}