#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <string>
using namespace std;

int main()
{
	freopen("A-largegcj.in", "r", stdin);
	freopen("resultlarge.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		string word;
		cin >> word;
		int len = word.size();
		string new_word;
		for (int i = 0; i < word.size(); ++i)
		{
			if (new_word.empty())
			{
				new_word.push_back(word[i]);
			}
			else
			{
				if (word[i] >= new_word.front())
				{
					new_word.insert(new_word.begin(),word[i]);
				}
				else{
					new_word.push_back(word[i]);
				}
			}
		}
		cout << new_word << endl;


	}
}