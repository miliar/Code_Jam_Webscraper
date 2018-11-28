#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int table[10] = { 'Z' - 'A', 'W' - 'A', 'U' - 'A', 'X' - 'A', 'G' - 'A', 'O' - 'A', 'H' - 'A', 'F' - 'A', 'S' - 'A', 'I' - 'A' };
char number[10][7] = { "ZERO", "TWO", "FOUR","SIX", "EIGHT", "ONE", "THREE", "FIVE", "SEVEN", "NINE" };
char size_s[10] = { 4,3,4,3,5,3,5,4,5,4 };
int t[10] = { 0,2,4,6,8,1,3,5,7,9 };

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large_501.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		string str;
		int check[27] = { 0 };
		vector<int> v;
		cin >> str;
		for (int j = 0; str[j] != 0; ++j)
			check[str[j] - 'A']++;
		for (int j = 0; j < 10; ++j)
		{
			int tmp = check[table[j]];
			for (int k = 0; k < tmp; ++k)
				v.push_back(t[j]);
			for (int k = 0; k < size_s[j]; ++k)
			{
				for (int p = 0; p < tmp; ++p)
					check[number[j][k] - 'A']--;
			}
		}
		sort(v.begin(), v.end());
		printf("Case #%d: ", i);
		for (int j = 0; j < v.size(); ++j)
			printf("%d", v[j]);
		printf("\n");
	}
}