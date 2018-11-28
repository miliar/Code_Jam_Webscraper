#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
	int T, t;
	cin >> T;
	t = 1;
	while (T >= t)
	{
		string S;
		int count[26] = { 0, };
		int res[10] = { 0, };
		cin >> S;
		
		for (int i = 0; i < S.size(); i++)
		{
			count[S[i] - 'A']++;
		}

		// ZERO count
		while (count['Z' - 'A'])
		{
			count['Z' - 'A']--;
			count['E' - 'A']--;
			count['R' - 'A']--;
			count['O' - 'A']--;
			res[0]++;
		}
		// TWO count
		while (count['W' - 'A'])
		{
			count['W' - 'A']--;
			count['O' - 'A']--;
			count['T' - 'A']--;
			res[2]++;
		}
		// EIGHT count
		while (count['G' - 'A'])
		{
			count['E' - 'A']--;
			count['I' - 'A']--;
			count['G' - 'A']--;
			count['H' - 'A']--;
			count['T' - 'A']--;
			res[8]++;
		}
		// FOUR count
		while (count['U' - 'A'])
		{
			count['F' - 'A']--;
			count['O' - 'A']--;
			count['U' - 'A']--;
			count['R' - 'A']--;
			res[4]++;
		}
		// ONE count
		while (count['O' - 'A'])
		{
			count['O' - 'A']--;
			count['N' - 'A']--;
			count['E' - 'A']--;
			res[1]++;
		}
		// SIX count
		while (count['X' - 'A'])
		{
			count['S' - 'A']--;
			count['I' - 'A']--;
			count['X' - 'A']--;
			res[6]++;
		}
		// SEVEN count
		while (count['S' - 'A'])
		{
			count['V' - 'A']--;
			count['S' - 'A']--;
			count['E' - 'A']--;
			count['E' - 'A']--;
			count['N' - 'A']--;
			res[7]++;
		}
		// THREE count
		while (count['T' - 'A'])
		{
			count['T' - 'A']--;
			count['H' - 'A']--;
			count['R' - 'A']--;
			count['E' - 'A']--;
			count['E' - 'A']--;
			res[3]++;
		}
		// FIVE count
		while (count['F' - 'A'])
		{
			count['F' - 'A']--;
			count['I' - 'A']--;
			count['V' - 'A']--;
			count['E' - 'A']--;
			res[5]++;
		}
		// NINE count
		while (count['N' - 'A'])
		{
			count['N' - 'A']--;
			count['I' - 'A']--;
			count['N' - 'A']--;
			count['E' - 'A']--;
			res[9]++;
		}

		cout << "Case #" << t << ": ";
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < res[i]; j++)
				cout << i;
		}
		cout << endl;
		t++;
	}
}