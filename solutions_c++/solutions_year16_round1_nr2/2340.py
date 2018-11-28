#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <cstring>
using namespace std;
/*
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
}*/
int main()
{
	freopen("B-small-attempt0gcj.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		int n;
		cin >> n;
		int a[2501];
		memset(a, 0, sizeof(a));
		
		for (int i = 0; i < 2 * n - 1; ++i)
		{
			for (int j = 0; j < n; ++j)
			{
				int value;
				cin >> value;
				for (int k = 1; k <= 2501; ++k)
				{
				
					if (value == k)
					{
						a[k]++;
					}
				}
			}
		}
		for (int i =0; i <2501; i++)
		{
			if (a[i] %2==1)
			{
				cout << i << " ";
			}
		}
		cout << endl;


	}
}