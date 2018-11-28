#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> vPossible;

void getWinningWord(string word, string process)
{
	if (word.length() > 0)
	{
		if (word[0] >= process[0])
		{
			getWinningWord(word.substr(1, word.length() - 1), word.substr(0, 1) + process);
		}
		else
		{
			getWinningWord(word.substr(1, word.length() - 1), process + word.substr(0, 1));
		}
	}
	else
	{
		vPossible.push_back(process);
	}
}

int main()
{
	int T = 0;
	string word;

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> word;

		vPossible.clear();
		getWinningWord(word.substr(1, word.length() - 1), word.substr(0, 1));
		/*
		for (int a = 0; a < vPossible.size(); a++)
		{
			for (int b = a + 1; b < vPossible.size(); b++)
			{
				for (int l = 0; l < vPossible[a].length(); l++)
				{
					if (vPossible[a][l] > vPossible[b][l])
					{
						vPossible.erase(vPossible.begin() + b);
						b--;
						break;
					}
					else if (vPossible[a][l] < vPossible[b][l])
					{
						vPossible.erase(vPossible.begin() + a);
						a--;
						break;
					}
				}

				if (a < 0)
					break;
			}
		}
		*/
		cout << "Case #" << t << ": " << vPossible[0] << endl;
	}

	getchar();
	getchar();
	return 0;
}
