#include <cstdio>
#include <iostream>

using namespace std;

int db[27];
int num[10];

inline int ind(char x)
{
	return (int) (x - 'A');
}

int n;
string s;

int main()
{
	ios_base::sync_with_stdio(false);
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < 26; j++)
		{
			db[j] = 0;
		}
		for (int j = 0; j < 10; j++)
		{
			num[j] = 0;
		}
		cin >> s;
		for (int j = 0; j < s.length(); j++)
		{
			db[ind(s[j])]++;
			//cerr << s[j] << ' ' << db[ind(s[j])] << endl;
		}
		//cerr << "ZZZ" << db[ind('Z')] << endl;
		num[0] = db[ind('Z')];
		db[ind('Z')] -= num[0];
		db[ind('E')] -= num[0];
		db[ind('R')] -= num[0];
		db[ind('O')] -= num[0];
		num[6] = db[ind('X')];
		db[ind('S')] -= num[6];
		db[ind('I')] -= num[6];
		db[ind('X')] -= num[6];
		num[7] = db[ind('S')];
		db[ind('S')] -= num[7];
		db[ind('E')] -= num[7];
		db[ind('V')] -= num[7];
		db[ind('E')] -= num[7];
		db[ind('N')] -= num[7];
		num[5] = db[ind('V')];
		db[ind('F')] -= num[5];
		db[ind('I')] -= num[5];
		db[ind('V')] -= num[5];
		db[ind('E')] -= num[5];
		num[4] = db[ind('F')];
		db[ind('F')] -= num[4];
		db[ind('O')] -= num[4];
		db[ind('U')] -= num[4];
		db[ind('R')] -= num[4];
		num[3] = db[ind('R')];
		db[ind('T')] -= num[3];
		db[ind('H')] -= num[3];
		db[ind('R')] -= num[3];
		db[ind('E')] -= num[3];
		db[ind('E')] -= num[3];
		num[2] = db[ind('W')];
		db[ind('T')] -= num[2];
		db[ind('W')] -= num[2];
		db[ind('O')] -= num[2];
		num[1] = db[ind('O')];
		db[ind('O')] -= num[1];
		db[ind('N')] -= num[1];
		db[ind('E')] -= num[1];
		num[8] = db[ind('G')];
		db[ind('I')] -= num[8];
		//most a tobbit kihagyom
		num[9] = db[ind('I')];
		cout << "Case #" << i << ": ";
		for (int j = 0; j <= 9; j++)
		{
			//cerr << j << ' ' << num[j] << endl;
			for (int k = 1; k <= num[j]; k++)
			{
				cout << j;
			}
		}
		cout << endl;
	}
	return 0;
}
