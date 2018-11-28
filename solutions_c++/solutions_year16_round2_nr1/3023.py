#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <cstring>
#include <unordered_map>
#include <string>
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
}
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
int main()
{
	freopen("test.txt", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	while (test_case--)
	{
		cout << "Case #" << ++index << ": ";
		int n;
		cin >> n;
		vector<int> a(n+1);
		for (int i = 1; i <= n; ++i)
		{
			int value;
			cin >> value;
			a[i] = value;
		}
		int max_len = -1;
		int len = -1;
		bool used[10001];
		for (int i = 1; i <= n; ++i)
		{
			memset(used, false, sizeof(used));
			int k = i;
			used[k] = true;
			len = 1;
			while (!used[a[k]])
			{
				k = a[k];
				len++;
				used[k] = true;
			}
			//if (a[k]==i)
			max_len = max(len, max_len);
			

		}
		cout <<max_len<< endl;


	}
}*/
int main()
{
	freopen("A-largefuck.in", "r", stdin);
	freopen("result.txt", "w", stdout);
	int test_case;
	cin >> test_case;
	int index = 0;
	string d[] = { "ZERO", "TWO", "FOUR", "SIX", "THREE", "FIVE", "SEVEN", "EIGHT", "NINE", "ONE" };
	int num[] = { 0, 2, 4, 6, 3, 5, 7, 8, 9, 1 };
	vector<string> digit(d, d + 10);
	
	while (test_case--)
	{
		vector<int> result;
		cout << "Case #" << ++index << ": ";
		if (test_case == 2) 
			int fuck = 0;
		string s;
		cin >> s;
		unordered_map<char, int> mp,backup;
		for (int i = 0; i < s.size(); ++i)
		{
			mp[s[i]]++;
		}
		for (int i = 0; i < digit.size(); )
		{
			bool isword = true;
			backup = mp;
			for (int j = 0; j < digit[i].size(); ++j)
			{
				if (mp.find(digit[i][j]) != mp.end() && mp[digit[i][j]] >= 1)
				{
					mp[digit[i][j]]--;
					isword = true;
				}
				else
				{
					isword = false;
					break;
				}
			}
			if (isword == true)
			{
				result.push_back( num[i]);
				
			}
			else
			{
				mp = backup;
				++i;
			}
		}
		sort(result.begin(), result.end());
		for (int i = 0; i < result.size(); ++i)
		{
			cout << result[i];
		}
		cout << endl;
	
	



	}
	fclose(stdin);
	fclose(stdout);
	system("result.txt");
}

