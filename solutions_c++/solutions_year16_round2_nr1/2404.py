#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <iomanip>


using namespace std;
string s;
int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("small.out", "w", stdout);
	//ios_base::sync_with_stdio(0);
	int tests;
	cin >> tests;
	cin >> ws;
	vector<int> letters(26, 0);
	vector<int> digits(10, 0);
	for (int t = 1; t <= tests; ++t)
	{
		
		letters.assign(26, 0);
		digits.assign(10, 0);
		s = "";
		getline(cin,s);
		//cout << s;
		int len = s.size();
		for (int i = 0; i < len; ++i)
		{
			letters[s[i] - 'A']++;
		}
		string ans = "";
		while (letters['Z'-'A'] > 0)
		{
			letters['Z' - 'A']--;
			letters['E' - 'A']--;
			letters['R' - 'A']--;
			letters['O' - 'A']--;
			digits[0]++;
		}
		while (letters['W'-'A'] > 0)
		{
			letters['T' - 'A']--;
			letters['W' - 'A']--;
			letters['O' - 'A']--;
			digits[2]++;
		}
		while (letters['G' - 'A'] > 0)
		{
			letters['E' - 'A']--;
			letters['I' - 'A']--;
			letters['G' - 'A']--;
			letters['H' - 'A']--;
			letters['T' - 'A']--;
			digits[8]++;
		}
		while (letters['U' - 'A'] > 0)
		{
			letters['F' - 'A']--;
			letters['O' - 'A']--;
			letters['U' - 'A']--;
			letters['R' - 'A']--;
			digits[4]++;
		}
		while (letters['O' - 'A'] > 0)
		{
			letters['O' - 'A']--;
			letters['N' - 'A']--;
			letters['E' - 'A']--;
			digits[1]++;
		}
		while (letters['F' - 'A'] > 0)
		{
			letters['F' - 'A']--;
			letters['I' - 'A']--;
			letters['V' - 'A']--;
			letters['E' - 'A']--;
			digits[5]++;
		}
		while (letters['V' - 'A'] > 0)
		{
			letters['S' - 'A']--;
			letters['E' - 'A']--;
			letters['V' - 'A']--;
			letters['E' - 'A']--;
			letters['N' - 'A']--;

			digits[7]++;
		}
		while (letters['X' - 'A'] > 0)
		{
			letters['S' - 'A']--;
			letters['I' - 'A']--;
			letters['X' - 'A']--;
			
			digits[6]++;
		}
		while (letters['I' - 'A'] > 0)
		{
			letters['N' - 'A']--;
			letters['I' - 'A']--;
			letters['N' - 'A']--;
			letters['E' - 'A']--;

			digits[9]++;
		}
		while (letters['E' - 'A'] > 0)
		{
			letters['T' - 'A']--;
			letters['H' - 'A']--;
			letters['R' - 'A']--;
			letters['E' - 'A']--;
			letters['E' - 'A']--;

			digits[3]++;
		}
		cout << "Case #" << t << ": ";
		for (int i = 0; i < 10; ++i)
		{
			for (int j = 0; j < digits[i]; ++j)
			{
				printf("%d", i);
			}
		}
		cout << endl;
	}
	//system("pause");
	//in.close();
	//out.close();
	return 0;
}